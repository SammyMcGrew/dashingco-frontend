"""Generated client library for iamassist version v1alpha2."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.iamassist.v1alpha2 import iamassist_v1alpha2_messages as messages


class IamassistV1alpha2(base_api.BaseApiClient):
  """Generated client library for service iamassist version v1alpha2."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://iamassist.googleapis.com/'
  MTLS_BASE_URL = 'https://iamassist.mtls.googleapis.com/'

  _PACKAGE = 'iamassist'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
  _VERSION = 'v1alpha2'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'IamassistV1alpha2'
  _URL_VERSION = 'v1alpha2'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new iamassist handle."""
    url = url or self.BASE_URL
    super(IamassistV1alpha2, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.simulator = self.SimulatorService(self)

  class SimulatorService(base_api.BaseApiService):
    """Service class for the simulator resource."""

    _NAME = 'simulator'

    def __init__(self, client):
      super(IamassistV1alpha2.SimulatorService, self).__init__(client)
      self._upload_configs = {
          }

    def CheckAccess(self, request, global_params=None):
      r"""Perform a check on whether a member is granted a permission.
on a resource given the provided simulated policies are applied
to their mapped resources.

      Args:
        request: (GoogleIamAssistV1alpha2CheckAccessRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleIamAssistV1alpha2CheckAccessResponse) The response message.
      """
      config = self.GetMethodConfig('CheckAccess')
      return self._RunMethod(
          config, request, global_params=global_params)

    CheckAccess.method_config = lambda: base_api.ApiMethodInfo(
        http_method='POST',
        method_id='iamassist.simulator.checkAccess',
        ordered_params=[],
        path_params=[],
        query_params=[],
        relative_path='v1alpha2/simulator:checkAccess',
        request_field='<request>',
        request_type_name='GoogleIamAssistV1alpha2CheckAccessRequest',
        response_type_name='GoogleIamAssistV1alpha2CheckAccessResponse',
        supports_download=False,
    )

    def ReplayRecentAccesses(self, request, global_params=None):
      r"""`ReplayRecentAccesses` replays the first K most recent accesses recorded.
from internal logs and responds which, if any, of these accesses would
change if the provided policy overlay were to be applied.

The value for K is not fixed while this API is in EAP.  This K will be
selected low enough so that the full response can fit in single message.

Note that the log freshness (i.e. the timestamp of the newest log
entry) may be up to 7 days stale.  In other words, an access attempt that
only occurred within the past 7 days may not be captured by the replay.

      Args:
        request: (GoogleIamAssistV1alpha2ReplayRecentAccessesRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('ReplayRecentAccesses')
      return self._RunMethod(
          config, request, global_params=global_params)

    ReplayRecentAccesses.method_config = lambda: base_api.ApiMethodInfo(
        http_method='POST',
        method_id='iamassist.simulator.replayRecentAccesses',
        ordered_params=[],
        path_params=[],
        query_params=[],
        relative_path='v1alpha2/simulator:replayRecentAccesses',
        request_field='<request>',
        request_type_name='GoogleIamAssistV1alpha2ReplayRecentAccessesRequest',
        response_type_name='GoogleLongrunningOperation',
        supports_download=False,
    )
