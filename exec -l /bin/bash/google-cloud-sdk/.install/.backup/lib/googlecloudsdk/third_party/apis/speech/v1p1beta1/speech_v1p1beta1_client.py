"""Generated client library for speech version v1p1beta1."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.speech.v1p1beta1 import speech_v1p1beta1_messages as messages


class SpeechV1p1beta1(base_api.BaseApiClient):
  """Generated client library for service speech version v1p1beta1."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://speech.googleapis.com/'
  MTLS_BASE_URL = 'https://speech.mtls.googleapis.com/'

  _PACKAGE = 'speech'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
  _VERSION = 'v1p1beta1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'SpeechV1p1beta1'
  _URL_VERSION = 'v1p1beta1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new speech handle."""
    url = url or self.BASE_URL
    super(SpeechV1p1beta1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.operations = self.OperationsService(self)
    self.projects_locations_customClasses = self.ProjectsLocationsCustomClassesService(self)
    self.projects_locations_datasets = self.ProjectsLocationsDatasetsService(self)
    self.projects_locations_log_data_stats = self.ProjectsLocationsLogDataStatsService(self)
    self.projects_locations_models = self.ProjectsLocationsModelsService(self)
    self.projects_locations_operations = self.ProjectsLocationsOperationsService(self)
    self.projects_locations_phraseSets = self.ProjectsLocationsPhraseSetsService(self)
    self.projects_locations = self.ProjectsLocationsService(self)
    self.projects = self.ProjectsService(self)
    self.speech = self.SpeechService(self)

  class OperationsService(base_api.BaseApiService):
    """Service class for the operations resource."""

    _NAME = 'operations'

    def __init__(self, client):
      super(SpeechV1p1beta1.OperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

      Args:
        request: (SpeechOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1p1beta1/operations/{operationsId}',
        http_method='GET',
        method_id='speech.operations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1p1beta1/operations/{+name}',
        request_field='',
        request_type_name='SpeechOperationsGetRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. NOTE: the `name` binding allows API services to override the binding to use different resource name schemes, such as `users/*/operations`. To override the binding, API services can add a binding such as `"/v1/{name=users/*}/operations"` to their service configuration. For backwards compatibility, the default name includes the operations collection id, however overriding users must ensure the name binding is the parent resource, without the operations collection id.

      Args:
        request: (SpeechOperationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListOperationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='speech.operations.list',
        ordered_params=[],
        path_params=[],
        query_params=['filter', 'name', 'pageSize', 'pageToken'],
        relative_path='v1p1beta1/operations',
        request_field='',
        request_type_name='SpeechOperationsListRequest',
        response_type_name='ListOperationsResponse',
        supports_download=False,
    )

  class ProjectsLocationsCustomClassesService(base_api.BaseApiService):
    """Service class for the projects_locations_customClasses resource."""

    _NAME = 'projects_locations_customClasses'

    def __init__(self, client):
      super(SpeechV1p1beta1.ProjectsLocationsCustomClassesService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Create a custom class.

      Args:
        request: (SpeechProjectsLocationsCustomClassesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (CustomClass) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1p1beta1/projects/{projectsId}/locations/{locationsId}/customClasses',
        http_method='POST',
        method_id='speech.projects.locations.customClasses.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['customClassId'],
        relative_path='v1p1beta1/{+parent}/customClasses',
        request_field='customClass',
        request_type_name='SpeechProjectsLocationsCustomClassesCreateRequest',
        response_type_name='CustomClass',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Delete a custom class.

      Args:
        request: (SpeechProjectsLocationsCustomClassesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1p1beta1/projects/{projectsId}/locations/{locationsId}/customClasses/{customClassesId}',
        http_method='DELETE',
        method_id='speech.projects.locations.customClasses.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1p1beta1/{+name}',
        request_field='',
        request_type_name='SpeechProjectsLocationsCustomClassesDeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Get a custom class.

      Args:
        request: (SpeechProjectsLocationsCustomClassesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (CustomClass) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1p1beta1/projects/{projectsId}/locations/{locationsId}/customClasses/{customClassesId}',
        http_method='GET',
        method_id='speech.projects.locations.customClasses.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1p1beta1/{+name}',
        request_field='',
        request_type_name='SpeechProjectsLocationsCustomClassesGetRequest',
        response_type_name='CustomClass',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""List custom classes.

      Args:
        request: (SpeechProjectsLocationsCustomClassesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListCustomClassesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1p1beta1/projects/{projectsId}/locations/{locationsId}/customClasses',
        http_method='GET',
        method_id='speech.projects.locations.customClasses.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['pageSize', 'pageToken'],
        relative_path='v1p1beta1/{+parent}/customClasses',
        request_field='',
        request_type_name='SpeechProjectsLocationsCustomClassesListRequest',
        response_type_name='ListCustomClassesResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Update a custom class.

      Args:
        request: (SpeechProjectsLocationsCustomClassesPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (CustomClass) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1p1beta1/projects/{projectsId}/locations/{locationsId}/customClasses/{customClassesId}',
        http_method='PATCH',
        method_id='speech.projects.locations.customClasses.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['updateMask'],
        relative_path='v1p1beta1/{+name}',
        request_field='customClass',
        request_type_name='SpeechProjectsLocationsCustomClassesPatchRequest',
        response_type_name='CustomClass',
        supports_download=False,
    )

  class ProjectsLocationsDatasetsService(base_api.BaseApiService):
    """Service class for the projects_locations_datasets resource."""

    _NAME = 'projects_locations_datasets'

    def __init__(self, client):
      super(SpeechV1p1beta1.ProjectsLocationsDatasetsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a new dataset for custom model training. The name of created dataset is stored in `response.metadata.works_on` field. Metadata type is SpeechOperationMetadata. Response type is Empty.

      Args:
        request: (SpeechProjectsLocationsDatasetsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1p1beta1/projects/{projectsId}/locations/{locationsId}/datasets',
        http_method='POST',
        method_id='speech.projects.locations.datasets.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v1p1beta1/{+parent}/datasets',
        request_field='dataset',
        request_type_name='SpeechProjectsLocationsDatasetsCreateRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes the named automl dataset. Returns an Empty response.

      Args:
        request: (SpeechProjectsLocationsDatasetsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1p1beta1/projects/{projectsId}/locations/{locationsId}/datasets/{datasetsId}',
        http_method='DELETE',
        method_id='speech.projects.locations.datasets.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1p1beta1/{+name}',
        request_field='',
        request_type_name='SpeechProjectsLocationsDatasetsDeleteRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Get the dataset associated with the dataset resource.

      Args:
        request: (SpeechProjectsLocationsDatasetsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Dataset) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1p1beta1/projects/{projectsId}/locations/{locationsId}/datasets/{datasetsId}',
        http_method='GET',
        method_id='speech.projects.locations.datasets.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['includeModelInfo'],
        relative_path='v1p1beta1/{+name}',
        request_field='',
        request_type_name='SpeechProjectsLocationsDatasetsGetRequest',
        response_type_name='Dataset',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Fetch the list of dataset associated with this project.

      Args:
        request: (SpeechProjectsLocationsDatasetsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListDatasetsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1p1beta1/projects/{projectsId}/locations/{locationsId}/datasets',
        http_method='GET',
        method_id='speech.projects.locations.datasets.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'includeModelInfo', 'pageSize', 'pageToken'],
        relative_path='v1p1beta1/{+parent}/datasets',
        request_field='',
        request_type_name='SpeechProjectsLocationsDatasetsListRequest',
        response_type_name='ListDatasetsResponse',
        supports_download=False,
    )

    def RefreshData(self, request, global_params=None):
      r"""Refresh data for a dataset. Returns an Empty response.

      Args:
        request: (SpeechProjectsLocationsDatasetsRefreshDataRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('RefreshData')
      return self._RunMethod(
          config, request, global_params=global_params)

    RefreshData.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1p1beta1/projects/{projectsId}/locations/{locationsId}/datasets/{datasetsId}:refreshData',
        http_method='POST',
        method_id='speech.projects.locations.datasets.refreshData',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1p1beta1/{+name}:refreshData',
        request_field='refreshDataRequest',
        request_type_name='SpeechProjectsLocationsDatasetsRefreshDataRequest',
        response_type_name='Operation',
        supports_download=False,
    )

  class ProjectsLocationsLogDataStatsService(base_api.BaseApiService):
    """Service class for the projects_locations_log_data_stats resource."""

    _NAME = 'projects_locations_log_data_stats'

    def __init__(self, client):
      super(SpeechV1p1beta1.ProjectsLocationsLogDataStatsService, self).__init__(client)
      self._upload_configs = {
          }

    def List(self, request, global_params=None):
      r"""Lists all log data stats associated with requested project.

      Args:
        request: (SpeechProjectsLocationsLogDataStatsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListLogDataStatsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1p1beta1/projects/{projectsId}/locations/{locationsId}/log_data_stats',
        http_method='GET',
        method_id='speech.projects.locations.log_data_stats.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v1p1beta1/{+parent}/log_data_stats',
        request_field='',
        request_type_name='SpeechProjectsLocationsLogDataStatsListRequest',
        response_type_name='ListLogDataStatsResponse',
        supports_download=False,
    )

  class ProjectsLocationsModelsService(base_api.BaseApiService):
    """Service class for the projects_locations_models resource."""

    _NAME = 'projects_locations_models'

    def __init__(self, client):
      super(SpeechV1p1beta1.ProjectsLocationsModelsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a new custom model. Metadata type is SpeechOperationMetadata. Response type is Model.

      Args:
        request: (SpeechProjectsLocationsModelsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1p1beta1/projects/{projectsId}/locations/{locationsId}/models',
        http_method='POST',
        method_id='speech.projects.locations.models.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['name'],
        relative_path='v1p1beta1/{+parent}/models',
        request_field='model',
        request_type_name='SpeechProjectsLocationsModelsCreateRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes the named automl model. Returns an Empty response.

      Args:
        request: (SpeechProjectsLocationsModelsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1p1beta1/projects/{projectsId}/locations/{locationsId}/models/{modelsId}',
        http_method='DELETE',
        method_id='speech.projects.locations.models.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1p1beta1/{+name}',
        request_field='',
        request_type_name='SpeechProjectsLocationsModelsDeleteRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Deploy(self, request, global_params=None):
      r"""Performs asynchronous model deployment of the model: receive results via the google.longrunning.Operations interface. After the operation is completed this returns either an `Operation.error` in case of error or a `google.protobuf.Empty` if the deployment was successful.

      Args:
        request: (SpeechProjectsLocationsModelsDeployRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Deploy')
      return self._RunMethod(
          config, request, global_params=global_params)

    Deploy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1p1beta1/projects/{projectsId}/locations/{locationsId}/models/{modelsId}:deploy',
        http_method='POST',
        method_id='speech.projects.locations.models.deploy',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1p1beta1/{+name}:deploy',
        request_field='deployModelRequest',
        request_type_name='SpeechProjectsLocationsModelsDeployRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Evaluate(self, request, global_params=None):
      r"""Performs asynchronous evaluation of the model: receive results via the google.longrunning.Operations interface. After the operation is completed this returns either an `Operation.error` in case of error or a `EvaluateModelResponse` with the evaluation results.

      Args:
        request: (SpeechProjectsLocationsModelsEvaluateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Evaluate')
      return self._RunMethod(
          config, request, global_params=global_params)

    Evaluate.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1p1beta1/projects/{projectsId}/locations/{locationsId}/models/{modelsId}:evaluate',
        http_method='POST',
        method_id='speech.projects.locations.models.evaluate',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1p1beta1/{+name}:evaluate',
        request_field='evaluateModelRequest',
        request_type_name='SpeechProjectsLocationsModelsEvaluateRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Fetch the list of models associated with this project.

      Args:
        request: (SpeechProjectsLocationsModelsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListModelsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1p1beta1/projects/{projectsId}/locations/{locationsId}/models',
        http_method='GET',
        method_id='speech.projects.locations.models.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1p1beta1/{+parent}/models',
        request_field='',
        request_type_name='SpeechProjectsLocationsModelsListRequest',
        response_type_name='ListModelsResponse',
        supports_download=False,
    )

  class ProjectsLocationsOperationsService(base_api.BaseApiService):
    """Service class for the projects_locations_operations resource."""

    _NAME = 'projects_locations_operations'

    def __init__(self, client):
      super(SpeechV1p1beta1.ProjectsLocationsOperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

      Args:
        request: (SpeechProjectsLocationsOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1p1beta1/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}',
        http_method='GET',
        method_id='speech.projects.locations.operations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1p1beta1/{+name}',
        request_field='',
        request_type_name='SpeechProjectsLocationsOperationsGetRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. NOTE: the `name` binding allows API services to override the binding to use different resource name schemes, such as `users/*/operations`. To override the binding, API services can add a binding such as `"/v1/{name=users/*}/operations"` to their service configuration. For backwards compatibility, the default name includes the operations collection id, however overriding users must ensure the name binding is the parent resource, without the operations collection id.

      Args:
        request: (SpeechProjectsLocationsOperationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListOperationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1p1beta1/projects/{projectsId}/locations/{locationsId}/operations',
        http_method='GET',
        method_id='speech.projects.locations.operations.list',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1p1beta1/{+name}/operations',
        request_field='',
        request_type_name='SpeechProjectsLocationsOperationsListRequest',
        response_type_name='ListOperationsResponse',
        supports_download=False,
    )

  class ProjectsLocationsPhraseSetsService(base_api.BaseApiService):
    """Service class for the projects_locations_phraseSets resource."""

    _NAME = 'projects_locations_phraseSets'

    def __init__(self, client):
      super(SpeechV1p1beta1.ProjectsLocationsPhraseSetsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Create a set of phrase hints. Each item in the set can be a single word or a multi-word phrase. The items in the PhraseSet are favored by the recognition model when you send a call that includes the PhraseSet.

      Args:
        request: (SpeechProjectsLocationsPhraseSetsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (PhraseSet) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1p1beta1/projects/{projectsId}/locations/{locationsId}/phraseSets',
        http_method='POST',
        method_id='speech.projects.locations.phraseSets.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['phraseSetId'],
        relative_path='v1p1beta1/{+parent}/phraseSets',
        request_field='phraseSet',
        request_type_name='SpeechProjectsLocationsPhraseSetsCreateRequest',
        response_type_name='PhraseSet',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Delete a phrase set.

      Args:
        request: (SpeechProjectsLocationsPhraseSetsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1p1beta1/projects/{projectsId}/locations/{locationsId}/phraseSets/{phraseSetsId}',
        http_method='DELETE',
        method_id='speech.projects.locations.phraseSets.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1p1beta1/{+name}',
        request_field='',
        request_type_name='SpeechProjectsLocationsPhraseSetsDeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Get a phrase set.

      Args:
        request: (SpeechProjectsLocationsPhraseSetsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (PhraseSet) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1p1beta1/projects/{projectsId}/locations/{locationsId}/phraseSets/{phraseSetsId}',
        http_method='GET',
        method_id='speech.projects.locations.phraseSets.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1p1beta1/{+name}',
        request_field='',
        request_type_name='SpeechProjectsLocationsPhraseSetsGetRequest',
        response_type_name='PhraseSet',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""List phrase sets.

      Args:
        request: (SpeechProjectsLocationsPhraseSetsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListPhraseSetResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1p1beta1/projects/{projectsId}/locations/{locationsId}/phraseSets',
        http_method='GET',
        method_id='speech.projects.locations.phraseSets.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['pageSize', 'pageToken'],
        relative_path='v1p1beta1/{+parent}/phraseSets',
        request_field='',
        request_type_name='SpeechProjectsLocationsPhraseSetsListRequest',
        response_type_name='ListPhraseSetResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Update a phrase set.

      Args:
        request: (SpeechProjectsLocationsPhraseSetsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (PhraseSet) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1p1beta1/projects/{projectsId}/locations/{locationsId}/phraseSets/{phraseSetsId}',
        http_method='PATCH',
        method_id='speech.projects.locations.phraseSets.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['updateMask'],
        relative_path='v1p1beta1/{+name}',
        request_field='phraseSet',
        request_type_name='SpeechProjectsLocationsPhraseSetsPatchRequest',
        response_type_name='PhraseSet',
        supports_download=False,
    )

  class ProjectsLocationsService(base_api.BaseApiService):
    """Service class for the projects_locations resource."""

    _NAME = 'projects_locations'

    def __init__(self, client):
      super(SpeechV1p1beta1.ProjectsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

    def LogData(self, request, global_params=None):
      r"""Purges all log data associated with requested project. Operation response type is google.protobuf.Empty. Since logs are stored by asynchronous writer process, buffered log data might still end up in storage, even after this call. To ensure all data is purged, call this method 3 days after last recognition call.

      Args:
        request: (SpeechProjectsLocationsLogDataRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('LogData')
      return self._RunMethod(
          config, request, global_params=global_params)

    LogData.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1p1beta1/projects/{projectsId}/locations/{locationsId}/log_data',
        http_method='DELETE',
        method_id='speech.projects.locations.log_data',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['bucketName'],
        relative_path='v1p1beta1/{+parent}/log_data',
        request_field='',
        request_type_name='SpeechProjectsLocationsLogDataRequest',
        response_type_name='Operation',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = 'projects'

    def __init__(self, client):
      super(SpeechV1p1beta1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }

  class SpeechService(base_api.BaseApiService):
    """Service class for the speech resource."""

    _NAME = 'speech'

    def __init__(self, client):
      super(SpeechV1p1beta1.SpeechService, self).__init__(client)
      self._upload_configs = {
          }

    def Longrunningrecognize(self, request, global_params=None):
      r"""Performs asynchronous speech recognition: receive results via the google.longrunning.Operations interface. Returns either an `Operation.error` or an `Operation.response` which contains a `LongRunningRecognizeResponse` message. For more information on asynchronous speech recognition, see the [how-to](https://cloud.google.com/speech-to-text/docs/async-recognize).

      Args:
        request: (LongRunningRecognizeRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Longrunningrecognize')
      return self._RunMethod(
          config, request, global_params=global_params)

    Longrunningrecognize.method_config = lambda: base_api.ApiMethodInfo(
        http_method='POST',
        method_id='speech.speech.longrunningrecognize',
        ordered_params=[],
        path_params=[],
        query_params=[],
        relative_path='v1p1beta1/speech:longrunningrecognize',
        request_field='<request>',
        request_type_name='LongRunningRecognizeRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Recognize(self, request, global_params=None):
      r"""Performs synchronous speech recognition: receive results after all audio has been sent and processed.

      Args:
        request: (RecognizeRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (RecognizeResponse) The response message.
      """
      config = self.GetMethodConfig('Recognize')
      return self._RunMethod(
          config, request, global_params=global_params)

    Recognize.method_config = lambda: base_api.ApiMethodInfo(
        http_method='POST',
        method_id='speech.speech.recognize',
        ordered_params=[],
        path_params=[],
        query_params=[],
        relative_path='v1p1beta1/speech:recognize',
        request_field='<request>',
        request_type_name='RecognizeRequest',
        response_type_name='RecognizeResponse',
        supports_download=False,
    )
