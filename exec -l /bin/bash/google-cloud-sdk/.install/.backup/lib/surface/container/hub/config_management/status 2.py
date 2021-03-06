# -*- coding: utf-8 -*- #
# Copyright 2019 Google LLC. All Rights Reserved.
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
"""The command to get the status of Config Management Feature."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import os
from apitools.base.py import exceptions as apitools_exceptions
from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.container.hub.features import base as feature_base
from googlecloudsdk.core import exceptions
from googlecloudsdk.core import properties

NA = 'NA'


class ConfigmanagementFeatureState(object):
  """feature state class stores nomos status."""

  def __init__(self, clusterName):
    self.name = clusterName
    self.status = NA
    self.last_synced_token = NA
    self.last_synced = NA
    self.sync_branch = NA

  def update_sync_state(self, fs):
    """update config_sync state for the membership that has nomos installed.

    Args:
      fs: ConfigmanagementFeatureState
    """
    if not (fs.configSyncState and fs.configSyncState.syncState):
      self.status = 'SYNC_STATE_UNSPECIFIED'
    else:
      self.status = fs.configSyncState.syncState.code
      # (b/153566864) limit the last_synced_token to 7 or 8 characters.
      if fs.configSyncState.syncState.syncToken:
        self.last_synced_token = fs.configSyncState.syncState.syncToken[:7]
      self.last_synced = fs.configSyncState.syncState.lastSyncTime
      if has_config_sync_git(fs):
        self.sync_branch = fs.membershipConfig.configSync.git.syncBranch


class Status(base.ListCommand):
  r"""Prints the status of all clusters with Configuration Management installed.

  This command prints the status of Config Management Feature
  resource in Hub.

  ## EXAMPLES

  Prints the status of Config Management Feature:

    $ {command}

    Name             Status  Last_Synced_Token   Sync_Branch  Last_Synced_Time
    mamaged-cluster  SYNCED  2945500b7f          acme         2020-03-23
    11:12:31 -0700 PDT
  """

  FEATURE_NAME = 'configmanagement'
  FEATURE_DISPLAY_NAME = 'Anthos Config Management'

  @staticmethod
  def Args(parser):
    parser.display_info.AddFormat("""
    multi(nomos_status:format='table(
            name:label=Name:sort=1,
            status:label=Status,
            last_synced_token:label="Last_Synced_Token",
            sync_branch:label="Sync_Branch",
            last_synced:label="Last_Synced_Time"
      )' , nomos_errors:format=list)
    """)

  def Run(self, args):
    try:
      project_id = properties.VALUES.core.project.GetOrFail()
      name = 'projects/{0}/locations/global/features/{1}'.format(
          project_id, self.FEATURE_NAME)
      response = feature_base.GetFeature(name)
    except apitools_exceptions.HttpUnauthorizedError as e:
      raise exceptions.Error(
          'You are not authorized to see the status of {} '
          'Feature from project [{}]. Underlying error: {}'.format(
              self.FEATURE_DISPLAY_NAME, project_id, e))
    except apitools_exceptions.HttpNotFoundError as e:
      raise exceptions.Error(
          '{} Feature for project [{}] is not enabled'.format(
              self.FEATURE_DISPLAY_NAME, project_id))
    if response.featureState is None or response.featureState.detailsByMembership is None:
      return None
    membership_details = response.featureState.detailsByMembership
    nomos_status = []
    nomos_errors = []
    for md in membership_details.additionalProperties:
      name = os.path.basename(md.key)
      cluster = ConfigmanagementFeatureState(name)
      fs = md.value.configmanagementFeatureState
      # (b/153587485) Show FeatureState.code if it's not OK
      # as it indicates an unreachable cluster or a dated syncState.code
      if md.value.code is None:
        cluster.status = 'CODE_UNSPECIFIED'
      elif md.value.code.name != 'OK':
        cluster.status = md.value.code.name
      else:
        # operator errors could occur regardless of the deployment_state
        if has_operator_error(fs):
          append_error(name, fs.operatorState.errors, nomos_errors)
        # (b/154174276, b/156293028)
        # check operator_state to see if nomos has been installed
        if not has_operator_state(fs):
          cluster.status = 'OPERATOR_STATE_UNSPECIFIED'
        else:
          cluster.status = fs.operatorState.deploymentState.name
          if cluster.status == 'INSTALLED':
            cluster.update_sync_state(fs)
            if has_config_sync_error(fs):
              append_error(name, fs.configSyncState.syncState.errors,
                           nomos_errors)
      nomos_status.append(cluster)
    return {'nomos_errors': nomos_errors, 'nomos_status': nomos_status}


def has_operator_state(fs):
  return fs and fs.operatorState and fs.operatorState.deploymentState


def has_operator_error(fs):
  return fs and fs.operatorState and fs.operatorState.errors


def has_config_sync_error(fs):
  return fs and fs.configSyncState and fs.configSyncState.syncState and fs.configSyncState.syncState.errors


def has_config_sync_git(fs):
  return fs.membershipConfig and fs.membershipConfig.configSync and fs.membershipConfig.configSync.git


def append_error(cluster, state_errors, nomos_errors):
  for error in state_errors:
    nomos_errors.append({
        'cluster': cluster,
        'error': error.errorMessage
    })
