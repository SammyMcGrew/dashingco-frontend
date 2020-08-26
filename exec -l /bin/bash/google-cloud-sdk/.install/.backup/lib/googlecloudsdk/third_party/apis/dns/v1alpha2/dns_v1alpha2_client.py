"""Generated client library for dns version v1alpha2."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.dns.v1alpha2 import dns_v1alpha2_messages as messages


class DnsV1alpha2(base_api.BaseApiClient):
  """Generated client library for service dns version v1alpha2."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://dns.googleapis.com/'
  MTLS_BASE_URL = 'https://dns.mtls.googleapis.com/'

  _PACKAGE = 'dns'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform', 'https://www.googleapis.com/auth/cloud-platform.read-only', 'https://www.googleapis.com/auth/ndev.clouddns.readonly', 'https://www.googleapis.com/auth/ndev.clouddns.readwrite']
  _VERSION = 'v1alpha2'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'DnsV1alpha2'
  _URL_VERSION = 'v1alpha2'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new dns handle."""
    url = url or self.BASE_URL
    super(DnsV1alpha2, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.activePeeringZones = self.ActivePeeringZonesService(self)
    self.changes = self.ChangesService(self)
    self.dnsKeys = self.DnsKeysService(self)
    self.managedZoneOperations = self.ManagedZoneOperationsService(self)
    self.managedZones = self.ManagedZonesService(self)
    self.policies = self.PoliciesService(self)
    self.projects = self.ProjectsService(self)
    self.resourceRecordSets = self.ResourceRecordSetsService(self)

  class ActivePeeringZonesService(base_api.BaseApiService):
    """Service class for the activePeeringZones resource."""

    _NAME = 'activePeeringZones'

    def __init__(self, client):
      super(DnsV1alpha2.ActivePeeringZonesService, self).__init__(client)
      self._upload_configs = {
          }

    def Deactivate(self, request, global_params=None):
      r"""Deactivate a Peering Zone if it's not already deactivated. Returns an error if the managed zone cannot be found, is not a peering zone. If the zone is already deactivated, returns false for deactivate_succeeded field.

      Args:
        request: (DnsActivePeeringZonesDeactivateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (PeeringZoneDeactivateResponse) The response message.
      """
      config = self.GetMethodConfig('Deactivate')
      return self._RunMethod(
          config, request, global_params=global_params)

    Deactivate.method_config = lambda: base_api.ApiMethodInfo(
        http_method='DELETE',
        method_id='dns.activePeeringZones.deactivate',
        ordered_params=['project', 'peeringZoneId'],
        path_params=['peeringZoneId', 'project'],
        query_params=['clientOperationId'],
        relative_path='dns/v1alpha2/projects/{project}/activePeeringZones/{peeringZoneId}',
        request_field='',
        request_type_name='DnsActivePeeringZonesDeactivateRequest',
        response_type_name='PeeringZoneDeactivateResponse',
        supports_download=False,
    )

    def GetPeeringZoneInfo(self, request, global_params=None):
      r"""Fetch the representation of an existing PeeringZone.

      Args:
        request: (DnsActivePeeringZonesGetPeeringZoneInfoRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ManagedZone) The response message.
      """
      config = self.GetMethodConfig('GetPeeringZoneInfo')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetPeeringZoneInfo.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='dns.activePeeringZones.getPeeringZoneInfo',
        ordered_params=['project', 'peeringZoneId'],
        path_params=['peeringZoneId', 'project'],
        query_params=['clientOperationId'],
        relative_path='dns/v1alpha2/projects/{project}/activePeeringZones/{peeringZoneId}',
        request_field='',
        request_type_name='DnsActivePeeringZonesGetPeeringZoneInfoRequest',
        response_type_name='ManagedZone',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Enumerate PeeringZones that target a given network via dns peering.

      Args:
        request: (DnsActivePeeringZonesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (PeeringZonesListResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='dns.activePeeringZones.list',
        ordered_params=['project', 'targetNetwork'],
        path_params=['project'],
        query_params=['maxResults', 'pageToken', 'targetNetwork'],
        relative_path='dns/v1alpha2/projects/{project}/activePeeringZones',
        request_field='',
        request_type_name='DnsActivePeeringZonesListRequest',
        response_type_name='PeeringZonesListResponse',
        supports_download=False,
    )

  class ChangesService(base_api.BaseApiService):
    """Service class for the changes resource."""

    _NAME = 'changes'

    def __init__(self, client):
      super(DnsV1alpha2.ChangesService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Atomically update the ResourceRecordSet collection.

      Args:
        request: (DnsChangesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Change) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        http_method='POST',
        method_id='dns.changes.create',
        ordered_params=['project', 'managedZone'],
        path_params=['managedZone', 'project'],
        query_params=['clientOperationId'],
        relative_path='dns/v1alpha2/projects/{project}/managedZones/{managedZone}/changes',
        request_field='change',
        request_type_name='DnsChangesCreateRequest',
        response_type_name='Change',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Fetch the representation of an existing Change.

      Args:
        request: (DnsChangesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Change) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='dns.changes.get',
        ordered_params=['project', 'managedZone', 'changeId'],
        path_params=['changeId', 'managedZone', 'project'],
        query_params=['clientOperationId'],
        relative_path='dns/v1alpha2/projects/{project}/managedZones/{managedZone}/changes/{changeId}',
        request_field='',
        request_type_name='DnsChangesGetRequest',
        response_type_name='Change',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Enumerate Changes to a ResourceRecordSet collection.

      Args:
        request: (DnsChangesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ChangesListResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='dns.changes.list',
        ordered_params=['project', 'managedZone'],
        path_params=['managedZone', 'project'],
        query_params=['maxResults', 'pageToken', 'sortBy', 'sortOrder'],
        relative_path='dns/v1alpha2/projects/{project}/managedZones/{managedZone}/changes',
        request_field='',
        request_type_name='DnsChangesListRequest',
        response_type_name='ChangesListResponse',
        supports_download=False,
    )

  class DnsKeysService(base_api.BaseApiService):
    """Service class for the dnsKeys resource."""

    _NAME = 'dnsKeys'

    def __init__(self, client):
      super(DnsV1alpha2.DnsKeysService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Fetch the representation of an existing DnsKey.

      Args:
        request: (DnsDnsKeysGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (DnsKey) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='dns.dnsKeys.get',
        ordered_params=['project', 'managedZone', 'dnsKeyId'],
        path_params=['dnsKeyId', 'managedZone', 'project'],
        query_params=['clientOperationId', 'digestType'],
        relative_path='dns/v1alpha2/projects/{project}/managedZones/{managedZone}/dnsKeys/{dnsKeyId}',
        request_field='',
        request_type_name='DnsDnsKeysGetRequest',
        response_type_name='DnsKey',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Enumerate DnsKeys to a ResourceRecordSet collection.

      Args:
        request: (DnsDnsKeysListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (DnsKeysListResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='dns.dnsKeys.list',
        ordered_params=['project', 'managedZone'],
        path_params=['managedZone', 'project'],
        query_params=['digestType', 'maxResults', 'pageToken'],
        relative_path='dns/v1alpha2/projects/{project}/managedZones/{managedZone}/dnsKeys',
        request_field='',
        request_type_name='DnsDnsKeysListRequest',
        response_type_name='DnsKeysListResponse',
        supports_download=False,
    )

  class ManagedZoneOperationsService(base_api.BaseApiService):
    """Service class for the managedZoneOperations resource."""

    _NAME = 'managedZoneOperations'

    def __init__(self, client):
      super(DnsV1alpha2.ManagedZoneOperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Fetch the representation of an existing Operation.

      Args:
        request: (DnsManagedZoneOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='dns.managedZoneOperations.get',
        ordered_params=['project', 'managedZone', 'operation'],
        path_params=['managedZone', 'operation', 'project'],
        query_params=['clientOperationId'],
        relative_path='dns/v1alpha2/projects/{project}/managedZones/{managedZone}/operations/{operation}',
        request_field='',
        request_type_name='DnsManagedZoneOperationsGetRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Enumerate Operations for the given ManagedZone.

      Args:
        request: (DnsManagedZoneOperationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ManagedZoneOperationsListResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='dns.managedZoneOperations.list',
        ordered_params=['project', 'managedZone'],
        path_params=['managedZone', 'project'],
        query_params=['maxResults', 'pageToken', 'sortBy'],
        relative_path='dns/v1alpha2/projects/{project}/managedZones/{managedZone}/operations',
        request_field='',
        request_type_name='DnsManagedZoneOperationsListRequest',
        response_type_name='ManagedZoneOperationsListResponse',
        supports_download=False,
    )

  class ManagedZonesService(base_api.BaseApiService):
    """Service class for the managedZones resource."""

    _NAME = 'managedZones'

    def __init__(self, client):
      super(DnsV1alpha2.ManagedZonesService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Create a new ManagedZone.

      Args:
        request: (DnsManagedZonesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ManagedZone) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        http_method='POST',
        method_id='dns.managedZones.create',
        ordered_params=['project'],
        path_params=['project'],
        query_params=['clientOperationId'],
        relative_path='dns/v1alpha2/projects/{project}/managedZones',
        request_field='managedZone',
        request_type_name='DnsManagedZonesCreateRequest',
        response_type_name='ManagedZone',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Delete a previously created ManagedZone.

      Args:
        request: (DnsManagedZonesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (DnsManagedZonesDeleteResponse) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        http_method='DELETE',
        method_id='dns.managedZones.delete',
        ordered_params=['project', 'managedZone'],
        path_params=['managedZone', 'project'],
        query_params=['clientOperationId'],
        relative_path='dns/v1alpha2/projects/{project}/managedZones/{managedZone}',
        request_field='',
        request_type_name='DnsManagedZonesDeleteRequest',
        response_type_name='DnsManagedZonesDeleteResponse',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Fetch the representation of an existing ManagedZone.

      Args:
        request: (DnsManagedZonesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ManagedZone) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='dns.managedZones.get',
        ordered_params=['project', 'managedZone'],
        path_params=['managedZone', 'project'],
        query_params=['clientOperationId'],
        relative_path='dns/v1alpha2/projects/{project}/managedZones/{managedZone}',
        request_field='',
        request_type_name='DnsManagedZonesGetRequest',
        response_type_name='ManagedZone',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Enumerate ManagedZones that have been created but not yet deleted.

      Args:
        request: (DnsManagedZonesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ManagedZonesListResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='dns.managedZones.list',
        ordered_params=['project'],
        path_params=['project'],
        query_params=['dnsName', 'maxResults', 'pageToken'],
        relative_path='dns/v1alpha2/projects/{project}/managedZones',
        request_field='',
        request_type_name='DnsManagedZonesListRequest',
        response_type_name='ManagedZonesListResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Apply a partial update to an existing ManagedZone.

      Args:
        request: (DnsManagedZonesPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        http_method='PATCH',
        method_id='dns.managedZones.patch',
        ordered_params=['project', 'managedZone'],
        path_params=['managedZone', 'project'],
        query_params=['clientOperationId'],
        relative_path='dns/v1alpha2/projects/{project}/managedZones/{managedZone}',
        request_field='managedZoneResource',
        request_type_name='DnsManagedZonesPatchRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Update(self, request, global_params=None):
      r"""Update an existing ManagedZone.

      Args:
        request: (DnsManagedZonesUpdateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Update')
      return self._RunMethod(
          config, request, global_params=global_params)

    Update.method_config = lambda: base_api.ApiMethodInfo(
        http_method='PUT',
        method_id='dns.managedZones.update',
        ordered_params=['project', 'managedZone'],
        path_params=['managedZone', 'project'],
        query_params=['clientOperationId'],
        relative_path='dns/v1alpha2/projects/{project}/managedZones/{managedZone}',
        request_field='managedZoneResource',
        request_type_name='DnsManagedZonesUpdateRequest',
        response_type_name='Operation',
        supports_download=False,
    )

  class PoliciesService(base_api.BaseApiService):
    """Service class for the policies resource."""

    _NAME = 'policies'

    def __init__(self, client):
      super(DnsV1alpha2.PoliciesService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Create a new Policy.

      Args:
        request: (DnsPoliciesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        http_method='POST',
        method_id='dns.policies.create',
        ordered_params=['project'],
        path_params=['project'],
        query_params=['clientOperationId'],
        relative_path='dns/v1alpha2/projects/{project}/policies',
        request_field='policy',
        request_type_name='DnsPoliciesCreateRequest',
        response_type_name='Policy',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Delete a previously created Policy. Will fail if the policy is still being referenced by a network.

      Args:
        request: (DnsPoliciesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (DnsPoliciesDeleteResponse) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        http_method='DELETE',
        method_id='dns.policies.delete',
        ordered_params=['project', 'policy'],
        path_params=['policy', 'project'],
        query_params=['clientOperationId'],
        relative_path='dns/v1alpha2/projects/{project}/policies/{policy}',
        request_field='',
        request_type_name='DnsPoliciesDeleteRequest',
        response_type_name='DnsPoliciesDeleteResponse',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Fetch the representation of an existing Policy.

      Args:
        request: (DnsPoliciesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='dns.policies.get',
        ordered_params=['project', 'policy'],
        path_params=['policy', 'project'],
        query_params=['clientOperationId'],
        relative_path='dns/v1alpha2/projects/{project}/policies/{policy}',
        request_field='',
        request_type_name='DnsPoliciesGetRequest',
        response_type_name='Policy',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Enumerate all Policies associated with a project.

      Args:
        request: (DnsPoliciesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (PoliciesListResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='dns.policies.list',
        ordered_params=['project'],
        path_params=['project'],
        query_params=['maxResults', 'pageToken'],
        relative_path='dns/v1alpha2/projects/{project}/policies',
        request_field='',
        request_type_name='DnsPoliciesListRequest',
        response_type_name='PoliciesListResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Apply a partial update to an existing Policy.

      Args:
        request: (DnsPoliciesPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (PoliciesPatchResponse) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        http_method='PATCH',
        method_id='dns.policies.patch',
        ordered_params=['project', 'policy'],
        path_params=['policy', 'project'],
        query_params=['clientOperationId'],
        relative_path='dns/v1alpha2/projects/{project}/policies/{policy}',
        request_field='policyResource',
        request_type_name='DnsPoliciesPatchRequest',
        response_type_name='PoliciesPatchResponse',
        supports_download=False,
    )

    def Update(self, request, global_params=None):
      r"""Update an existing Policy.

      Args:
        request: (DnsPoliciesUpdateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (PoliciesUpdateResponse) The response message.
      """
      config = self.GetMethodConfig('Update')
      return self._RunMethod(
          config, request, global_params=global_params)

    Update.method_config = lambda: base_api.ApiMethodInfo(
        http_method='PUT',
        method_id='dns.policies.update',
        ordered_params=['project', 'policy'],
        path_params=['policy', 'project'],
        query_params=['clientOperationId'],
        relative_path='dns/v1alpha2/projects/{project}/policies/{policy}',
        request_field='policyResource',
        request_type_name='DnsPoliciesUpdateRequest',
        response_type_name='PoliciesUpdateResponse',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = 'projects'

    def __init__(self, client):
      super(DnsV1alpha2.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Fetch the representation of an existing Project.

      Args:
        request: (DnsProjectsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Project) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='dns.projects.get',
        ordered_params=['project'],
        path_params=['project'],
        query_params=['clientOperationId'],
        relative_path='dns/v1alpha2/projects/{project}',
        request_field='',
        request_type_name='DnsProjectsGetRequest',
        response_type_name='Project',
        supports_download=False,
    )

  class ResourceRecordSetsService(base_api.BaseApiService):
    """Service class for the resourceRecordSets resource."""

    _NAME = 'resourceRecordSets'

    def __init__(self, client):
      super(DnsV1alpha2.ResourceRecordSetsService, self).__init__(client)
      self._upload_configs = {
          }

    def List(self, request, global_params=None):
      r"""Enumerate ResourceRecordSets that have been created but not yet deleted.

      Args:
        request: (DnsResourceRecordSetsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ResourceRecordSetsListResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='dns.resourceRecordSets.list',
        ordered_params=['project', 'managedZone'],
        path_params=['managedZone', 'project'],
        query_params=['maxResults', 'name', 'pageToken', 'type'],
        relative_path='dns/v1alpha2/projects/{project}/managedZones/{managedZone}/rrsets',
        request_field='',
        request_type_name='DnsResourceRecordSetsListRequest',
        response_type_name='ResourceRecordSetsListResponse',
        supports_download=False,
    )
