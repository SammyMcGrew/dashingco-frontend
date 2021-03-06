# -*- coding: utf-8 -*- #
# Copyright 2014 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Create cluster command."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from apitools.base.py import exceptions as apitools_exceptions

from googlecloudsdk.api_lib.compute import metadata_utils
from googlecloudsdk.api_lib.compute import utils
from googlecloudsdk.api_lib.container import api_adapter
from googlecloudsdk.api_lib.container import kubeconfig as kconfig
from googlecloudsdk.api_lib.container import util
from googlecloudsdk.calliope import actions
from googlecloudsdk.calliope import arg_parsers
from googlecloudsdk.calliope import base
from googlecloudsdk.calliope import exceptions
from googlecloudsdk.command_lib.container import constants
from googlecloudsdk.command_lib.container import container_command_util as cmd_util
from googlecloudsdk.command_lib.container import flags
from googlecloudsdk.command_lib.container import messages
from googlecloudsdk.core import log
from googlecloudsdk.core.console import console_io


def _AddAdditionalZonesFlag(parser, deprecated=True):
  action = None
  if deprecated:
    action = actions.DeprecationAction(
        'additional-zones',
        warn='This flag is deprecated. '
        'Use --node-locations=PRIMARY_ZONE,[ZONE,...] instead.')
  parser.add_argument(
      '--additional-zones',
      type=arg_parsers.ArgList(min_length=1),
      action=action,
      metavar='ZONE',
      help="""\
The set of additional zones in which the specified node footprint should be
replicated. All zones must be in the same region as the cluster's primary zone.
If additional-zones is not specified, all nodes will be in the cluster's primary
zone.

Note that `NUM_NODES` nodes will be created in each zone, such that if you
specify `--num-nodes=4` and choose one additional zone, 8 nodes will be created.

Multiple locations can be specified, separated by commas. For example:

  $ {command} example-cluster --zone us-central1-a --additional-zones us-central1-b,us-central1-c
""")


def _AddAdditionalZonesGroup(parser):
  group = parser.add_mutually_exclusive_group()
  _AddAdditionalZonesFlag(group, deprecated=True)
  flags.AddNodeLocationsFlag(group)


def _GetEnableStackdriver(args):
  # hasattr checks if field exists, if not isSpecified would throw exception
  if not hasattr(args, 'enable_stackdriver_kubernetes'):
    return None
  if not args.IsSpecified('enable_stackdriver_kubernetes'):
    return None
  return args.enable_stackdriver_kubernetes


def _Args(parser):
  """Register flags for this command.

  Args:
    parser: An argparse.ArgumentParser-like object. It is mocked out in order to
      capture some information, but behaves like an ArgumentParser.
  """
  parser.add_argument(
      'name',
      help="""\
The name of the cluster to create.

The name may contain only lowercase alphanumerics and '-', must start with a
letter and end with an alphanumeric, and must be no longer than 40
characters.
""")
  # Timeout in seconds for operation
  parser.add_argument(
      '--timeout',
      type=int,
      default=3600,
      hidden=True,
      help='Timeout (seconds) for waiting on the operation to complete.')
  flags.AddAsyncFlag(parser)

  parser.add_argument(
      '--subnetwork',
      help="""\
The Google Compute Engine subnetwork
(https://cloud.google.com/compute/docs/subnetworks) to which the cluster is
connected. The subnetwork must belong to the network specified by --network.

Cannot be used with the "--create-subnetwork" option.
""")
  parser.add_argument(
      '--network',
      help='The Compute Engine Network that the cluster will connect to. '
      'Google Kubernetes Engine will use this network when creating routes '
      'and firewalls for the clusters. Defaults to the \'default\' network.')
  parser.add_argument(
      '--cluster-ipv4-cidr',
      help='The IP address range for the pods in this cluster in CIDR '
      'notation (e.g. 10.0.0.0/14).  Prior to Kubernetes version 1.7.0 '
      'this must be a subset of 10.0.0.0/8; however, starting with version '
      '1.7.0 can be any RFC 1918 IP range.')

  parser.display_info.AddFormat(util.CLUSTERS_FORMAT)


def ValidateBasicAuthFlags(args):
  """Validates flags associated with basic auth.

  Overwrites username if enable_basic_auth is specified; checks that password is
  set if username is non-empty.

  Args:
    args: an argparse namespace. All the arguments that were provided to this
      command invocation.

  Raises:
    util.Error, if username is non-empty and password is not set.
  """
  if hasattr(args, 'enable_basic_auth') and \
      args.IsSpecified('enable_basic_auth'):
    if not args.enable_basic_auth:
      args.username = ''
    # `enable_basic_auth == true` is a no-op defaults are resoved server-side
    # based on the version of the cluster. For versions before 1.12, this is
    # 'admin', otherwise '' (disabled).
  if not args.username and args.IsSpecified('password'):
    raise util.Error(constants.USERNAME_PASSWORD_ERROR_MSG)


def MaybeLogAuthWarning(args):
  if (hasattr(args, 'issue_client_certificate') and \
      args.IsSpecified('issue_client_certificate')):
    if not (hasattr(args, 'enable_basic_auth') and \
            (args.IsSpecified('enable_basic_auth') or \
              args.IsSpecified('username'))):
      log.warning('If `--issue-client-certificate` is specified but '
                  '`--enable-basic-auth` or `--username` is not, our API will '
                  'treat that as `--no-enable-basic-auth`.')


def ParseCreateOptionsBase(args, is_autogke, get_default):
  """Parses the flags provided with the cluster creation command."""
  if hasattr(args, 'addons') and args.IsSpecified('addons') and \
      api_adapter.DASHBOARD in args.addons:
    log.warning(
        'The `KubernetesDashboard` addon is deprecated, and will be removed as '
        'an option for new clusters starting in 1.15. It is recommended to use '
        'the Cloud Console to manage and monitor your Kubernetes clusters, '
        'workloads and applications. See: '
        'https://cloud.google.com/kubernetes-engine/docs/concepts/dashboards')

  flags.MungeBasicAuthFlags(args)

  MaybeLogAuthWarning(args)
  enable_ip_alias = get_default('enable_ip_alias')
  if hasattr(args, 'enable_ip_alias'):
    flags.WarnForUnspecifiedIpAllocationPolicy(args)

  enable_autorepair = False
  if hasattr(args, 'enable_autorepair'):
    enable_autorepair = cmd_util.GetAutoRepair(args)
    flags.WarnForNodeModification(args, enable_autorepair)

  metadata = metadata_utils.ConstructMetadataDict(
      get_default('metadata'),
      get_default('metadata_from_file'))

  return api_adapter.CreateClusterOptions(
      accelerators=get_default('accelerator'),
      additional_zones=get_default('additional_zones'),
      addons=get_default('addons'),
      boot_disk_kms_key=get_default('boot_disk_kms_key'),
      cluster_ipv4_cidr=get_default('cluster_ipv4_cidr'),
      cluster_secondary_range_name=get_default('cluster_secondary_range_name'),
      cluster_version=get_default('cluster_version'),
      node_version=get_default('node_version'),
      create_subnetwork=get_default('create_subnetwork'),
      disable_default_snat=get_default('disable_default_snat'),
      disk_type=get_default('disk_type'),
      enable_autorepair=enable_autorepair,
      enable_autoscaling=get_default('enable_autoscaling'),
      enable_autoupgrade=(cmd_util.GetAutoUpgrade(args) if
                          hasattr(args, 'enable_autoupgrade')
                          else None),
      enable_binauthz=get_default('enable_binauthz'),
      enable_stackdriver_kubernetes=_GetEnableStackdriver(args),
      enable_cloud_logging=args.enable_cloud_logging if (hasattr(args, 'enable_cloud_logging') and args.IsSpecified('enable_cloud_logging')) else None,
      enable_cloud_monitoring=args.enable_cloud_monitoring if (hasattr(args, 'enable_cloud_monitoring') and args.IsSpecified('enable_cloud_monitoring')) else None,
      enable_ip_alias=enable_ip_alias,
      enable_intra_node_visibility=get_default('enable_intra_node_visibility'),
      enable_kubernetes_alpha=get_default('enable_kubernetes_alpha'),
      enable_cloud_run_alpha=args.enable_cloud_run_alpha if (hasattr(args, 'enable_cloud_run_alpha') and args.IsSpecified('enable_cloud_run_alpha')) else None,
      enable_legacy_authorization=get_default('enable_legacy_authorization'),
      enable_master_authorized_networks=\
        get_default('enable_master_authorized_networks'),
      enable_master_global_access=get_default('enable_master_global_access'),
      enable_network_policy=get_default('enable_network_policy'),
      enable_private_nodes=get_default('enable_private_nodes'),
      enable_private_endpoint=get_default('enable_private_endpoint'),
      image_type=get_default('image_type'),
      image=get_default('image'),
      image_project=get_default('image_project'),
      image_family=get_default('image_family'),
      issue_client_certificate=get_default('issue_client_certificate'),
      labels=get_default('labels'),
      local_ssd_count=get_default('local_ssd_count'),
      maintenance_window=get_default('maintenance_window'),
      maintenance_window_start=get_default('maintenance_window_start'),
      maintenance_window_end=get_default('maintenance_window_end'),
      maintenance_window_recurrence=get_default('maintenance_window_recurrence'),
      master_authorized_networks=get_default('master_authorized_networks'),
      master_ipv4_cidr=get_default('master_ipv4_cidr'),
      max_nodes=get_default('max_nodes'),
      max_nodes_per_pool=get_default('max_nodes_per_pool'),
      min_cpu_platform=get_default('min_cpu_platform'),
      min_nodes=get_default('min_nodes'),
      network=get_default('network'),
      node_disk_size_gb=utils.BytesToGb(args.disk_size) if hasattr(args, 'disk_size') else None,
      node_labels=get_default('node_labels'),
      node_locations=get_default('node_locations'),
      node_machine_type=get_default('machine_type'),
      node_taints=get_default('node_taints'),
      num_nodes=get_default('num_nodes'),
      password=get_default('password'),
      preemptible=get_default('preemptible'),
      scopes=get_default('scopes'),
      service_account=get_default('service_account'),
      services_ipv4_cidr=get_default('services_ipv4_cidr'),
      services_secondary_range_name=get_default('services_secondary_range_name'),
      subnetwork=get_default('subnetwork'),
      tags=get_default('tags'),
      user=get_default('username'),
      metadata=metadata,
      default_max_pods_per_node=get_default('default_max_pods_per_node'),
      max_pods_per_node=get_default('max_pods_per_node'),
      enable_tpu=get_default('enable_tpu'),
      tpu_ipv4_cidr=get_default('tpu_ipv4_cidr'),
      resource_usage_bigquery_dataset=get_default('resource_usage_bigquery_dataset'),
      enable_network_egress_metering=get_default('enable_network_egress_metering'),
      enable_resource_consumption_metering=get_default('enable_resource_consumption_metering'),
      database_encryption_key=get_default('database_encryption_key'),
      workload_pool=get_default('workload_pool'),
      identity_provider=get_default('identity_provider'),
      workload_metadata=get_default('workload_metadata'),
      workload_metadata_from_node=get_default('workload_metadata_from_node'),
      enable_vertical_pod_autoscaling=get_default('enable_vertical_pod_autoscaling'),
      enable_autoprovisioning=get_default('enable_autoprovisioning'),
      autoprovisioning_config_file=get_default('autoprovisioning_config_file'),
      autoprovisioning_service_account=get_default('autoprovisioning_service_account'),
      autoprovisioning_scopes=get_default('autoprovisioning_scopes'),
      autoprovisioning_locations=get_default('autoprovisioning_locations'),
      autoprovisioning_max_surge_upgrade=get_default('autoprovisioning_max_surge_upgrade'),
      autoprovisioning_max_unavailable_upgrade=get_default('autoprovisioning_max_unavailable_upgrade'),
      enable_autoprovisioning_autorepair=get_default('enable_autoprovisioning_autorepair'),
      enable_autoprovisioning_autoupgrade=get_default('enable_autoprovisioning_autoupgrade'),
      autoprovisioning_min_cpu_platform=get_default('autoprovisioning_min_cpu_platform'),
      min_cpu=get_default('min_cpu'),
      max_cpu=get_default('max_cpu'),
      min_memory=get_default('min_memory'),
      max_memory=get_default('max_memory'),
      min_accelerator=get_default('min_accelerator'),
      max_accelerator=get_default('max_accelerator'),
      shielded_secure_boot=get_default('shielded_secure_boot'),
      shielded_integrity_monitoring=get_default('shielded_integrity_monitoring'),
      reservation_affinity=get_default('reservation_affinity'),
      reservation=get_default('reservation'),
      release_channel=get_default('release_channel'),
      enable_shielded_nodes=get_default('enable_shielded_nodes'),
      max_surge_upgrade=get_default('max_surge_upgrade'),
      max_unavailable_upgrade=get_default('max_unavailable_upgrade'),
      auto_gke=is_autogke)


GA = 'ga'
BETA = 'beta'
ALPHA = 'alpha'


def AddAutoRepair(parser):
  flags.AddEnableAutoRepairFlag(parser, for_create=True)


def AddPrivateClusterDeprecated(parser, default=None):
  default_value = {} if default is None else default
  flags.AddPrivateClusterFlags(parser, default=default_value,
                               with_deprecated=True)


def AddEnableAutoUpgradeWithDefault(parser):
  flags.AddEnableAutoUpgradeFlag(parser, default=True)


def AddAutoprovisioningGA(parser):
  flags.AddAutoprovisioningFlags(parser, hidden=False, for_create=True, ga=True)


def AddAutoprovisioning(parser):
  flags.AddAutoprovisioningFlags(parser, hidden=False, for_create=True)


def AddTpuWithServiceNetworking(parser):
  flags.AddTpuFlags(parser, enable_tpu_service_networking=True)


def AddWorkloadIdentityWithProvider(parser):
  flags.AddWorkloadIdentityFlags(parser, use_identity_provider=True)


def AddDisableDefaultSnatFlagForClusterCreate(parser):
  flags.AddDisableDefaultSnatFlag(parser, for_cluster_create=True)


def AddMasterSignalsFlag(parser):
  flags.AddEnableMasterSignalsFlags(parser, for_create=True)


def AddPrivateIPv6Flag(api, parser):
  flags.AddPrivateIpv6GoogleAccessTypeFlag(api, parser, hidden=True)


def AddKubernetesObjectsExportFlag(parser):
  flags.AddKubernetesObjectsExportConfig(parser, for_create=True)


def DefaultAttribute(flagname, flag_defaults):
  if flagname in flag_defaults:
    return flag_defaults[flagname]
  return None


def AttrValue(args, flagname, flag_defaults):
  return getattr(args, flagname, DefaultAttribute(flagname, flag_defaults))

flags_to_add = {
    GA: {
        'accelerator': flags.AddAcceleratorArgs,
        'additionalzones': _AddAdditionalZonesFlag,
        'addons': flags.AddAddonsFlags,
        'autorepair': AddAutoRepair,
        'autoprovisioning': AddAutoprovisioningGA,
        'autoupgrade': AddEnableAutoUpgradeWithDefault,
        'args': _Args,
        'basicauth': flags.AddBasicAuthFlags,
        'binauthz': flags.AddEnableBinAuthzFlag,
        'bootdiskkms': flags.AddBootDiskKmsKeyFlag,
        'cloudlogging': flags.AddEnableCloudLogging,
        'cloudmonitoring': flags.AddEnableCloudMonitoring,
        'cloudrunalpha': flags.AddEnableCloudRunAlphaFlag,
        'clusterautoscaling': flags.AddClusterAutoscalingFlags,
        'clusterversion': flags.AddClusterVersionFlag,
        'disabledefaultsnat': AddDisableDefaultSnatFlagForClusterCreate,
        'databaseencryption': flags.AddDatabaseEncryptionFlag,
        'disksize': flags.AddDiskSizeFlag,
        'disktype': flags.AddDiskTypeFlag,
        'imageflags': flags.AddImageFlagsCreate,
        'intranodevisibility': flags.AddEnableIntraNodeVisibilityFlag,
        'ipalias': flags.AddIpAliasCoreFlag,
        'ipalias_additional': flags.AddIPAliasRelatedFlags,
        'issueclientcert': flags.AddIssueClientCertificateFlag,
        'kubernetesalpha': flags.AddEnableKubernetesAlphaFlag,
        'labels': flags.AddLabelsFlag,
        'legacyauth': flags.AddEnableLegacyAuthorizationFlag,
        'localssd': flags.AddLocalSSDFlag,
        'machinetype': flags.AddMachineTypeFlag,
        'maintenancewindow': flags.AddMaintenanceWindowGroup,
        'masterauth': flags.AddMasterAuthorizedNetworksFlags,
        'masterglobalaccess': flags.AddMasterGlobalAccessFlag,
        'maxnodes': flags.AddMaxNodesPerPool,
        'maxpodspernode': flags.AddMaxPodsPerNodeFlag,
        'maxunavailable': flags.AddMaxUnavailableUpgradeFlag,
        'metadata': flags.AddMetadataFlags,
        'mincpu': flags.AddMinCpuPlatformFlag,
        'networkpolicy': flags.AddNetworkPolicyFlags,
        'nodeidentity': flags.AddClusterNodeIdentityFlags,
        'nodelabels': flags.AddNodeLabelsFlag,
        'nodelocations': flags.AddNodeLocationsFlag,
        'nodetaints': flags.AddNodeTaintsFlag,
        'nodeversion': flags.AddNodeVersionFlag,
        'num_nodes': flags.AddNumNodes,
        'preemptible': flags.AddPreemptibleFlag,
        'privatecluster': flags.AddPrivateClusterFlags,
        'releasechannel': flags.AddReleaseChannelFlag,
        'reservationaffinity': flags.AddReservationAffinityFlags,
        'resourceusageexport': flags.AddResourceUsageExportFlags,
        'shieldedinstance': flags.AddShieldedInstanceFlags,
        'shieldednodes': flags.AddEnableShieldedNodesFlags,
        'surgeupgrade': flags.AddSurgeUpgradeFlag,
        'stackdriver': flags.AddEnableStackdriverKubernetesFlag,
        'tags': flags.AddTagsCreate,
        'tpu': flags.AddTpuFlags,
        'verticalpodautoscaling': flags.AddVerticalPodAutoscalingFlag,
        'workloadidentity': flags.AddWorkloadIdentityFlags,
        'workloadmetadata': flags.AddWorkloadMetadataFlag,
    },
    BETA: {
        'accelerator':
            flags.AddAcceleratorArgs,
        'additionalzones':
            _AddAdditionalZonesGroup,
        'addons':
            flags.AddBetaAddonsFlags,
        'allowrouteoverlap':
            flags.AddAllowRouteOverlapFlag,
        'args':
            _Args,
        'autorepair':
            AddAutoRepair,
        'autoprovisioning':
            AddAutoprovisioning,
        'autoscalingprofiles':
            flags.AddAutoscalingProfilesFlag,
        'authenticatorsecurity':
            flags.AddAuthenticatorSecurityGroupFlags,
        'autoupgrade':
            AddEnableAutoUpgradeWithDefault,
        'basicauth':
            flags.AddBasicAuthFlags,
        'binauthz':
            flags.AddEnableBinAuthzFlag,
        'bootdiskkms':
            flags.AddBootDiskKmsKeyFlag,
        'cloudlogging':
            flags.AddEnableCloudLogging,
        'cloudmonitoring':
            flags.AddEnableCloudMonitoring,
        'cloudrunalpha':
            flags.AddEnableCloudRunAlphaFlag,
        'clusterautoscaling':
            flags.AddClusterAutoscalingFlags,
        'clusterversion':
            flags.AddClusterVersionFlag,
        'confidentialnodes':
            flags.AddEnableConfidentialNodesFlag,
        'databaseencryption':
            flags.AddDatabaseEncryptionFlag,
        'datapath': (lambda p: flags.AddDatapathProviderFlag(p, hidden=True)),
        'dataplanev2':
            flags.AddDataplaneV2Flag,
        'disabledefaultsnat':
            AddDisableDefaultSnatFlagForClusterCreate,
        'disksize':
            flags.AddDiskSizeFlag,
        'disktype':
            flags.AddDiskTypeFlag,
        'imageflags':
            flags.AddImageFlagsCreate,
        'intranodevisibility':
            flags.AddEnableIntraNodeVisibilityFlag,
        'ipalias':
            flags.AddIpAliasCoreFlag,
        'ipalias_additional':
            flags.AddIPAliasRelatedFlags,
        'issueclientcert':
            flags.AddIssueClientCertificateFlag,
        'istioconfig':
            flags.AddIstioConfigFlag,
        'kubernetesalpha':
            flags.AddEnableKubernetesAlphaFlag,
        'kubernetesobjectsexport':
            AddKubernetesObjectsExportFlag,
        'gvnic':
            flags.AddEnableGvnicFlag,
        'localssd':
            flags.AddLocalSSDFlag,
        'loggingmonitoring':
            flags.AddEnableLoggingMonitoringSystemOnlyFlag,
        'labels':
            flags.AddLabelsFlag,
        'legacyauth':
            flags.AddEnableLegacyAuthorizationFlag,
        'machinetype':
            flags.AddMachineTypeFlag,
        'maintenancewindow':
            flags.AddMaintenanceWindowGroup,
        'masterglobalaccess':
            flags.AddMasterGlobalAccessFlag,
        'masterauth':
            flags.AddMasterAuthorizedNetworksFlags,
        'mastersignals':
            AddMasterSignalsFlag,
        'maxnodes':
            flags.AddMaxNodesPerPool,
        'maxpodspernode':
            flags.AddMaxPodsPerNodeFlag,
        'maxunavailable':
            (lambda p: flags.AddMaxUnavailableUpgradeFlag(p, is_create=True)),
        'metadata':
            flags.AddMetadataFlags,
        'mincpu':
            flags.AddMinCpuPlatformFlag,
        'networkpolicy':
            flags.AddNetworkPolicyFlags,
        'nodetaints':
            flags.AddNodeTaintsFlag,
        'nodeidentity':
            flags.AddClusterNodeIdentityFlags,
        'nodeversion':
            flags.AddNodeVersionFlag,
        'nodelabels':
            flags.AddNodeLabelsFlag,
        'notificationconfig':
            (lambda p: flags.AddNotificationConfigFlag(p, hidden=True)),
        'num_nodes':
            flags.AddNumNodes,
        'podsecuritypolicy':
            flags.AddPodSecurityPolicyFlag,
        'preemptible':
            flags.AddPreemptibleFlag,
        'privatecluster':
            AddPrivateClusterDeprecated,
        'privateipv6type': (lambda p: AddPrivateIPv6Flag('v1beta1', p)),
        'releasechannel':
            flags.AddReleaseChannelFlag,
        'resourceusageexport':
            flags.AddResourceUsageExportFlags,
        'reservationaffinity':
            flags.AddReservationAffinityFlags,
        'shieldedinstance':
            flags.AddShieldedInstanceFlags,
        'shieldednodes':
            flags.AddEnableShieldedNodesFlags,
        'stackdriver':
            flags.AddEnableStackdriverKubernetesFlag,
        'surgeupgrade': (lambda p: flags.AddSurgeUpgradeFlag(p, default=1)),
        'systemconfig':
            lambda p: flags.AddSystemConfigFlag(p, hidden=False),
        'tags':
            flags.AddTagsCreate,
        'tpu':
            AddTpuWithServiceNetworking,
        'verticalpodautoscaling':
            flags.AddVerticalPodAutoscalingFlag,
        'workloadidentity':
            AddWorkloadIdentityWithProvider,
        'workloadmetadata':
            (lambda p: flags.AddWorkloadMetadataFlag(p, use_mode=False)),
    },
    ALPHA: {
        'accelerator':
            flags.AddAcceleratorArgs,
        'additionalzones':
            _AddAdditionalZonesGroup,
        'addons':
            flags.AddAlphaAddonsFlags,
        'allowrouteoverlap':
            flags.AddAllowRouteOverlapFlag,
        'args':
            _Args,
        'authenticatorsecurity':
            flags.AddAuthenticatorSecurityGroupFlags,
        'autoprovisioning':
            AddAutoprovisioning,
        'autorepair':
            AddAutoRepair,
        'autoscalingprofiles':
            flags.AddAutoscalingProfilesFlag,
        'basicauth':
            flags.AddBasicAuthFlags,
        'cloudlogging':
            flags.AddEnableCloudLogging,
        'clusterversion':
            flags.AddClusterVersionFlag,
        'autoupgrade':
            AddEnableAutoUpgradeWithDefault,
        'binauthz':
            flags.AddEnableBinAuthzFlag,
        'bootdiskkms':
            flags.AddBootDiskKmsKeyFlag,
        'cloudmonitoring':
            flags.AddEnableCloudMonitoring,
        'cloudrunalpha':
            flags.AddEnableCloudRunAlphaFlag,
        'cloudrunconfig':
            flags.AddCloudRunConfigFlag,
        'clusterautoscaling':
            flags.AddClusterAutoscalingFlags,
        'clusterdns':
            flags.AddClusterDNSFlags,
        'confidentialnodes':
            flags.AddEnableConfidentialNodesFlag,
        'costmanagementconfig':
            flags.AddCostManagementConfigFlag,
        'databaseencryption':
            flags.AddDatabaseEncryptionFlag,
        'datapath':
            lambda p: flags.AddDatapathProviderFlag(p, hidden=True),
        'dataplanev2':
            flags.AddDataplaneV2Flag,
        'disabledefaultsnat':
            AddDisableDefaultSnatFlagForClusterCreate,
        'disksize':
            flags.AddDiskSizeFlag,
        'disktype':
            flags.AddDiskTypeFlag,
        'gvnic':
            flags.AddEnableGvnicFlag,
        'ilbsubsetting':
            flags.AddILBSubsettingFlags,
        'imageflags':
            flags.AddImageFlagsCreate,
        'intranodevisibility':
            flags.AddEnableIntraNodeVisibilityFlag,
        'ipalias':
            flags.AddIpAliasCoreFlag,
        'ipalias_additional':
            flags.AddIPAliasRelatedFlags,
        'issueclientcert':
            flags.AddIssueClientCertificateFlag,
        'istioconfig':
            flags.AddIstioConfigFlag,
        'kubernetesalpha':
            flags.AddEnableKubernetesAlphaFlag,
        'labels':
            flags.AddLabelsFlag,
        'legacyauth':
            flags.AddEnableLegacyAuthorizationFlag,
        'linuxsysctl':
            flags.AddLinuxSysctlFlags,
        'localssdandlocalssdvol':
            flags.AddLocalSSDAndLocalSSDVolumeConfigsFlag,
        'loggingmonitoring':
            flags.AddEnableLoggingMonitoringSystemOnlyFlag,
        'machinetype':
            flags.AddMachineTypeFlag,
        'kubernetesobjectsexport':
            AddKubernetesObjectsExportFlag,
        'npname':
            lambda p: flags.AddInitialNodePoolNameArg(p, hidden=False),
        'maxunavailable':
            (lambda p: flags.AddMaxUnavailableUpgradeFlag(p, is_create=True)),
        'masterglobalaccess':
            flags.AddMasterGlobalAccessFlag,
        'maxnodes':
            flags.AddMaxNodesPerPool,
        'maxpodspernode':
            flags.AddMaxPodsPerNodeFlag,
        'maintenancewindow':
            flags.AddMaintenanceWindowGroup,
        'masterauth':
            flags.AddMasterAuthorizedNetworksFlags,
        'mastersignals':
            AddMasterSignalsFlag,
        'metadata':
            flags.AddMetadataFlags,
        'mincpu':
            flags.AddMinCpuPlatformFlag,
        'networkpolicy':
            flags.AddNetworkPolicyFlags,
        'nodetaints':
            flags.AddNodeTaintsFlag,
        'nodeidentity':
            flags.AddClusterNodeIdentityFlags,
        'nodeversion':
            flags.AddNodeVersionFlag,
        'nodelabels':
            flags.AddNodeLabelsFlag,
        'notificationconfig':
            (lambda p: flags.AddNotificationConfigFlag(p, hidden=True)),
        'num_nodes':
            flags.AddNumNodes,
        'podsecuritypolicy':
            flags.AddPodSecurityPolicyFlag,
        'preemptible':
            flags.AddPreemptibleFlag,
        'privatecluster':
            AddPrivateClusterDeprecated,
        'privateipv6':
            (lambda p: flags.AddEnablePrivateIpv6AccessFlag(p, hidden=True)),
        'privateipv6type': (lambda p: AddPrivateIPv6Flag('v1alpha1', p)),
        'reservationaffinity':
            flags.AddReservationAffinityFlags,
        'resourceusageexport':
            flags.AddResourceUsageExportFlags,
        'releasechannel':
            flags.AddReleaseChannelFlag,
        'shieldedinstance':
            flags.AddShieldedInstanceFlags,
        'shieldednodes':
            flags.AddEnableShieldedNodesFlags,
        'stackdriver':
            flags.AddEnableStackdriverKubernetesFlag,
        'securityprofile':
            flags.AddSecurityProfileForCreateFlags,
        'surgeupgrade': (lambda p: flags.AddSurgeUpgradeFlag(p, default=1)),
        'systemconfig':
            lambda p: flags.AddSystemConfigFlag(p, hidden=False),
        'tags':
            flags.AddTagsCreate,
        'tpu':
            AddTpuWithServiceNetworking,
        'verticalpodautoscaling':
            flags.AddVerticalPodAutoscalingFlag,
        'workloadidentity':
            AddWorkloadIdentityWithProvider,
        'workloadmetadata':
            (lambda p: flags.AddWorkloadMetadataFlag(p, use_mode=False)),
    },
}


def AddFlags(channel, parser, flag_defaults, allowlist=None):
  """Adds flags to the current parser.

  Args:
    channel: channel from which to add flags. eg. "GA" or "BETA"
    parser: parser to add current flags to
    flag_defaults: mapping to override the default value of flags
    allowlist: only add intersection of this list and channel flags
  """
  add_flag_for_channel = flags_to_add[channel]

  for flagname in add_flag_for_channel:
    if allowlist is None or (flagname in allowlist):
      if flagname in flag_defaults:
        add_flag_for_channel[flagname](parser, default=flag_defaults[flagname])
      else:
        add_flag_for_channel[flagname](parser)

base_flag_defaults = {
    'num_nodes': 3,
}


@base.ReleaseTracks(base.ReleaseTrack.GA)
class Create(base.CreateCommand):
  """Create a cluster for running containers."""

  detailed_help = {
      'DESCRIPTION':
          '{description}',
      'EXAMPLES':
          """\
          To create a cluster with the default configuration, run:

            $ {command} sample-cluster
          """,
  }

  autogke = False
  default_flag_values = base_flag_defaults

  @staticmethod
  def Args(parser):
    AddFlags(GA, parser, base_flag_defaults)

  def ParseCreateOptions(self, args):
    get_default = lambda key: AttrValue(args, key, self.default_flag_values)
    return ParseCreateOptionsBase(args, self.autogke, get_default)

  def Run(self, args):
    """This is what gets called when the user runs this command.

    Args:
      args: an argparse namespace. All the arguments that were provided to this
        command invocation.

    Returns:
      Cluster message for the successfully created cluster.

    Raises:
      util.Error, if creation failed.
    """
    if args.async_ and not args.IsSpecified('format'):
      args.format = util.OPERATIONS_FORMAT

    util.CheckKubectlInstalled()

    adapter = self.context['api_adapter']
    location_get = self.context['location_get']
    location = location_get(args)

    cluster_ref = adapter.ParseCluster(args.name, location)
    options = self.ParseCreateOptions(args)

    if options.private_cluster and not (
        options.enable_master_authorized_networks or
        options.master_authorized_networks):
      log.warning(
          '`--private-cluster` makes the master inaccessible from '
          'cluster-external IP addresses, by design. To allow limited '
          'access to the master, see the `--master-authorized-networks` flags '
          'and our documentation on setting up private clusters: '
          'https://cloud.google.com'
          '/kubernetes-engine/docs/how-to/private-clusters')

    if not options.enable_shielded_nodes:
      log.warning(
          'Starting with version 1.18, clusters will have shielded GKE nodes by default.'
      )

    if options.enable_ip_alias:
      log.warning(
          'The Pod address range limits the maximum size of the cluster. '
          'Please refer to https://cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr to learn how to optimize IP address allocation.'
      )
    else:
      max_node_number = util.CalculateMaxNodeNumberByPodRange(
          options.cluster_ipv4_cidr)
      if max_node_number > 0:
        log.warning(
            'Your Pod address range (`--cluster-ipv4-cidr`) can accommodate at most %d node(s). '
            % max_node_number)

    if options.enable_kubernetes_alpha:
      console_io.PromptContinue(
          message=constants.KUBERNETES_ALPHA_PROMPT,
          throw_if_unattended=True,
          cancel_on_no=True)

    if options.enable_autorepair is not None:
      log.status.Print(
          messages.AutoUpdateUpgradeRepairMessage(options.enable_autorepair,
                                                  'autorepair'))

    if options.accelerators is not None:
      log.status.Print(constants.KUBERNETES_GPU_LIMITATION_MSG)

    operation = None
    try:
      operation_ref = adapter.CreateCluster(cluster_ref, options)
      if args.async_:
        return adapter.GetCluster(cluster_ref)

      operation = adapter.WaitForOperation(
          operation_ref,
          'Creating cluster {0} in {1}'.format(cluster_ref.clusterId,
                                               cluster_ref.zone),
          timeout_s=args.timeout)
      cluster = adapter.GetCluster(cluster_ref)
    except apitools_exceptions.HttpError as error:
      raise exceptions.HttpException(error, util.HTTP_ERROR_FORMAT)

    log.CreatedResource(cluster_ref)
    cluster_url = util.GenerateClusterUrl(cluster_ref)
    log.status.Print('To inspect the contents of your cluster, go to: ' +
                     cluster_url)
    if operation.detail:
      # Non-empty detail on a DONE create operation should be surfaced as
      # a warning to end user.
      log.warning(operation.detail)

    try:
      util.ClusterConfig.Persist(cluster, cluster_ref.projectId)
    except kconfig.MissingEnvVarError as error:
      log.warning(error)

    return [cluster]


@base.ReleaseTracks(base.ReleaseTrack.BETA)
class CreateBeta(Create):
  """Create a cluster for running containers."""

  @staticmethod
  def Args(parser):
    AddFlags(BETA, parser, base_flag_defaults)

  def ParseCreateOptions(self, args):
    get_default = lambda key: AttrValue(args, key, self.default_flag_values)
    ops = ParseCreateOptionsBase(args, self.autogke, get_default)
    flags.WarnForNodeVersionAutoUpgrade(args)
    flags.ValidateSurgeUpgradeSettings(args)
    flags.ValidateNotificationConfigFlag(args)
    ops.boot_disk_kms_key = get_default('boot_disk_kms_key')
    ops.min_cpu_platform = get_default('min_cpu_platform')
    ops.enable_pod_security_policy = get_default('enable_pod_security_policy')

    ops.allow_route_overlap = get_default('allow_route_overlap')
    ops.private_cluster = get_default('private_cluster')
    ops.istio_config = get_default('istio_config')
    ops.enable_vertical_pod_autoscaling = \
        get_default('enable_vertical_pod_autoscaling')
    ops.security_group = get_default('security_group')
    flags.ValidateIstioConfigCreateArgs(
        get_default('istio_config'), get_default('addons'))
    ops.max_surge_upgrade = get_default('max_surge_upgrade')
    ops.max_unavailable_upgrade = get_default('max_unavailable_upgrade')
    ops.autoscaling_profile = get_default('autoscaling_profile')
    ops.enable_tpu_service_networking = \
        get_default('enable_tpu_service_networking')
    ops.enable_logging_monitoring_system_only = \
        get_default('enable_logging_monitoring_system_only')
    ops.enable_gvnic = get_default('enable_gvnic')
    ops.system_config_from_file = get_default('system_config_from_file')
    ops.datapath_provider = get_default('datapath_provider')
    ops.dataplane_v2 = get_default('enable_dataplane_v2')
    ops.disable_default_snat = get_default('disable_default_snat')
    ops.enable_master_metrics = get_default('enable_master_metrics')
    ops.master_logs = get_default('master_logs')
    ops.notification_config = get_default('notification_config')
    ops.private_ipv6_google_access_type = \
        get_default('private_ipv6_google_access_type')
    ops.enable_confidential_nodes = get_default('enable_confidential_nodes')
    ops.kubernetes_objects_changes_target = \
        getattr(args, 'kubernetes_objects_changes_target', None)
    ops.kubernetes_objects_snapshots_target = \
        getattr(args, 'kubernetes_objects_snapshots_target', None)
    return ops


@base.ReleaseTracks(base.ReleaseTrack.ALPHA)
class CreateAlpha(Create):
  """Create a cluster for running containers."""

  @staticmethod
  def Args(parser):
    AddFlags(ALPHA, parser, base_flag_defaults)

  def ParseCreateOptions(self, args):
    get_default = lambda key: AttrValue(args, key, self.default_flag_values)
    ops = ParseCreateOptionsBase(args, self.autogke, get_default)
    flags.WarnForNodeVersionAutoUpgrade(args)
    flags.ValidateSurgeUpgradeSettings(args)
    flags.ValidateCloudRunConfigCreateArgs(
        get_default('cloud_run_config'),
        get_default('addons'))
    flags.ValidateNotificationConfigFlag(args)
    ops.boot_disk_kms_key = get_default('boot_disk_kms_key')
    ops.autoscaling_profile = get_default('autoscaling_profile')
    ops.local_ssd_volume_configs = get_default('local_ssd_volumes')
    ops.enable_pod_security_policy = get_default('enable_pod_security_policy')
    ops.allow_route_overlap = get_default('allow_route_overlap')
    ops.private_cluster = get_default('private_cluster')
    ops.enable_private_nodes = get_default('enable_private_nodes')
    ops.enable_private_endpoint = get_default('enable_private_endpoint')
    ops.master_ipv4_cidr = get_default('master_ipv4_cidr')
    ops.enable_tpu_service_networking = \
        get_default('enable_tpu_service_networking')
    ops.istio_config = get_default('istio_config')
    ops.cloud_run_config = get_default('cloud_run_config')
    ops.security_group = get_default('security_group')
    flags.ValidateIstioConfigCreateArgs(
        get_default('istio_config'), get_default('addons'))
    ops.enable_vertical_pod_autoscaling = \
        get_default('enable_vertical_pod_autoscaling')
    ops.security_profile = get_default('security_profile')
    ops.security_profile_runtime_rules = \
        get_default('security_profile_runtime_rules')
    ops.node_pool_name = get_default('node_pool_name')
    ops.enable_network_egress_metering = \
        get_default('enable_network_egress_metering')
    ops.enable_resource_consumption_metering = \
        get_default('enable_resource_consumption_metering')
    ops.enable_private_ipv6_access = get_default('enable_private_ipv6_access')
    ops.max_surge_upgrade = get_default('max_surge_upgrade')
    ops.max_unavailable_upgrade = get_default('max_unavailable_upgrade')
    ops.linux_sysctls = get_default('linux_sysctls')
    ops.enable_l4_ilb_subsetting = get_default('enable_l4_ilb_subsetting')
    ops.disable_default_snat = get_default('disable_default_snat')
    ops.system_config_from_file = get_default('system_config_from_file')
    ops.enable_cost_management = get_default('enable_cost_management')
    ops.enable_logging_monitoring_system_only = \
        get_default('enable_logging_monitoring_system_only')
    ops.datapath_provider = get_default('datapath_provider')
    ops.dataplane_v2 = get_default('enable_dataplane_v2')
    ops.enable_gvnic = get_default('enable_gvnic')
    ops.enable_master_metrics = get_default('enable_master_metrics')
    ops.master_logs = get_default('master_logs')
    ops.notification_config = get_default('notification_config')
    ops.private_ipv6_google_access_type = \
        get_default('private_ipv6_google_access_type')
    ops.enable_confidential_nodes = get_default('enable_confidential_nodes')
    ops.cluster_dns = get_default('cluster_dns')
    ops.cluster_dns_scope = get_default('cluster_dns_scope')
    ops.cluster_dns_domain = get_default('cluster_dns_domain')
    ops.kubernetes_objects_changes_target = \
        getattr(args, 'kubernetes_objects_changes_target', None)
    ops.kubernetes_objects_snapshots_target = \
        getattr(args, 'kubernetes_objects_snapshots_target', None)
    return ops
