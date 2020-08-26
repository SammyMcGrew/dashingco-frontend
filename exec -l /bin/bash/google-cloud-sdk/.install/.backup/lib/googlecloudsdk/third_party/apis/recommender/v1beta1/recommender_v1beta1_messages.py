"""Generated message classes for recommender version v1beta1.

"""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding
from apitools.base.py import extra_types


package = 'recommender'


class GoogleCloudRecommenderV1beta1CostProjection(_messages.Message):
  r"""Contains metadata about how much money a recommendation can save or
  incur.

  Fields:
    cost: An approximate projection on amount saved or amount incurred.
      Negative cost units indicate cost savings and positive cost units
      indicate increase. See google.type.Money documentation for
      positive/negative units.
    duration: Duration for which this cost applies.
  """

  cost = _messages.MessageField('GoogleTypeMoney', 1)
  duration = _messages.StringField(2)


class GoogleCloudRecommenderV1beta1Impact(_messages.Message):
  r"""Contains the impact a recommendation can have for a given category.

  Enums:
    CategoryValueValuesEnum: Category that is being targeted.

  Fields:
    category: Category that is being targeted.
    costProjection: Use with CategoryType.COST
  """

  class CategoryValueValuesEnum(_messages.Enum):
    r"""Category that is being targeted.

    Values:
      CATEGORY_UNSPECIFIED: Default unspecified category. Don't use directly.
      COST: Indicates a potential increase or decrease in cost.
      SECURITY: Indicates a potential increase or decrease in security.
      PERFORMANCE: Indicates a potential increase or decrease in performance.
      MANAGEABILITY: Indicates a potential increase or decrease in
        manageability.
    """
    CATEGORY_UNSPECIFIED = 0
    COST = 1
    SECURITY = 2
    PERFORMANCE = 3
    MANAGEABILITY = 4

  category = _messages.EnumField('CategoryValueValuesEnum', 1)
  costProjection = _messages.MessageField('GoogleCloudRecommenderV1beta1CostProjection', 2)


class GoogleCloudRecommenderV1beta1Insight(_messages.Message):
  r"""An insight along with the information used to derive the insight. The
  insight may have associated recomendations as well.

  Enums:
    CategoryValueValuesEnum: Category being targeted by the insight.

  Messages:
    ContentValue: A struct of custom fields to explain the insight. Example:
      "grantedPermissionsCount": "1000"

  Fields:
    associatedRecommendations: Recommendations derived from this insight.
    category: Category being targeted by the insight.
    content: A struct of custom fields to explain the insight. Example:
      "grantedPermissionsCount": "1000"
    description: Free-form human readable summary in English. The maximum
      length is 500 characters.
    etag: Fingerprint of the Insight. Provides optimistic locking when
      updating states.
    insightSubtype: Insight subtype. Insight content schema will be stable for
      a given subtype.
    lastRefreshTime: Timestamp of the latest data used to generate the
      insight.
    name: Name of the insight.
    observationPeriod: Observation period that led to the insight. The source
      data used to generate the insight ends at last_refresh_time and begins
      at (last_refresh_time - observation_period).
    stateInfo: Information state and metadata.
    targetResources: Fully qualified resource names that this insight is
      targeting.
  """

  class CategoryValueValuesEnum(_messages.Enum):
    r"""Category being targeted by the insight.

    Values:
      CATEGORY_UNSPECIFIED: Unspecified category.
      COST: The insight is related to cost.
      SECURITY: The insight is related to security.
      PERFORMANCE: The insight is related to performance.
      MANAGEABILITY: This insight is related to manageability.
    """
    CATEGORY_UNSPECIFIED = 0
    COST = 1
    SECURITY = 2
    PERFORMANCE = 3
    MANAGEABILITY = 4

  @encoding.MapUnrecognizedFields('additionalProperties')
  class ContentValue(_messages.Message):
    r"""A struct of custom fields to explain the insight. Example:
    "grantedPermissionsCount": "1000"

    Messages:
      AdditionalProperty: An additional property for a ContentValue object.

    Fields:
      additionalProperties: Properties of the object.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a ContentValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  associatedRecommendations = _messages.MessageField('GoogleCloudRecommenderV1beta1InsightRecommendationReference', 1, repeated=True)
  category = _messages.EnumField('CategoryValueValuesEnum', 2)
  content = _messages.MessageField('ContentValue', 3)
  description = _messages.StringField(4)
  etag = _messages.StringField(5)
  insightSubtype = _messages.StringField(6)
  lastRefreshTime = _messages.StringField(7)
  name = _messages.StringField(8)
  observationPeriod = _messages.StringField(9)
  stateInfo = _messages.MessageField('GoogleCloudRecommenderV1beta1InsightStateInfo', 10)
  targetResources = _messages.StringField(11, repeated=True)


class GoogleCloudRecommenderV1beta1InsightRecommendationReference(_messages.Message):
  r"""Reference to an associated recommendation.

  Fields:
    recommendation: Recommendation resource name, e.g. projects/[PROJECT_NUMBE
      R]/locations/[LOCATION]/recommenders/[RECOMMENDER_ID]/recommendations/[R
      ECOMMENDATION_ID]
  """

  recommendation = _messages.StringField(1)


class GoogleCloudRecommenderV1beta1InsightStateInfo(_messages.Message):
  r"""Information related to insight state.

  Enums:
    StateValueValuesEnum: Insight state.

  Messages:
    StateMetadataValue: A map of metadata for the state, provided by user or
      automations systems.

  Fields:
    state: Insight state.
    stateMetadata: A map of metadata for the state, provided by user or
      automations systems.
  """

  class StateValueValuesEnum(_messages.Enum):
    r"""Insight state.

    Values:
      STATE_UNSPECIFIED: Unspecified state.
      ACTIVE: Insight is active. Content for ACTIVE insights can be updated by
        Google. ACTIVE insights can be marked DISMISSED OR ACCEPTED.
      ACCEPTED: Some action has been taken based on this insight. Insights
        become accepted when a recommendation derived from the insight has
        been marked CLAIMED, SUCCEEDED, or FAILED. ACTIVE insights can also be
        marked ACCEPTED explicitly. Content for ACCEPTED insights is
        immutable. ACCEPTED insights can only be marked ACCEPTED (which may
        update state metadata).
      DISMISSED: Insight is dismissed. Content for DISMISSED insights can be
        updated by Google. DISMISSED insights can be marked as ACTIVE.
    """
    STATE_UNSPECIFIED = 0
    ACTIVE = 1
    ACCEPTED = 2
    DISMISSED = 3

  @encoding.MapUnrecognizedFields('additionalProperties')
  class StateMetadataValue(_messages.Message):
    r"""A map of metadata for the state, provided by user or automations
    systems.

    Messages:
      AdditionalProperty: An additional property for a StateMetadataValue
        object.

    Fields:
      additionalProperties: Additional properties of type StateMetadataValue
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a StateMetadataValue object.

      Fields:
        key: Name of the additional property.
        value: A string attribute.
      """

      key = _messages.StringField(1)
      value = _messages.StringField(2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  state = _messages.EnumField('StateValueValuesEnum', 1)
  stateMetadata = _messages.MessageField('StateMetadataValue', 2)


class GoogleCloudRecommenderV1beta1ListInsightsResponse(_messages.Message):
  r"""Response to the `ListInsights` method.

  Fields:
    insights: The set of insights for the `parent` resource.
    nextPageToken: A token that can be used to request the next page of
      results. This field is empty if there are no additional results.
  """

  insights = _messages.MessageField('GoogleCloudRecommenderV1beta1Insight', 1, repeated=True)
  nextPageToken = _messages.StringField(2)


class GoogleCloudRecommenderV1beta1ListRecommendationsResponse(_messages.Message):
  r"""Response to the `ListRecommendations` method.

  Fields:
    nextPageToken: A token that can be used to request the next page of
      results. This field is empty if there are no additional results.
    recommendations: The set of recommendations for the `parent` resource.
  """

  nextPageToken = _messages.StringField(1)
  recommendations = _messages.MessageField('GoogleCloudRecommenderV1beta1Recommendation', 2, repeated=True)


class GoogleCloudRecommenderV1beta1MarkInsightAcceptedRequest(_messages.Message):
  r"""Request for the `MarkInsightAccepted` method.

  Messages:
    StateMetadataValue: Optional. State properties user wish to include with
      this state. Full replace of the current state_metadata.

  Fields:
    etag: Required. Fingerprint of the Insight. Provides optimistic locking.
    stateMetadata: Optional. State properties user wish to include with this
      state. Full replace of the current state_metadata.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class StateMetadataValue(_messages.Message):
    r"""Optional. State properties user wish to include with this state. Full
    replace of the current state_metadata.

    Messages:
      AdditionalProperty: An additional property for a StateMetadataValue
        object.

    Fields:
      additionalProperties: Additional properties of type StateMetadataValue
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a StateMetadataValue object.

      Fields:
        key: Name of the additional property.
        value: A string attribute.
      """

      key = _messages.StringField(1)
      value = _messages.StringField(2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  etag = _messages.StringField(1)
  stateMetadata = _messages.MessageField('StateMetadataValue', 2)


class GoogleCloudRecommenderV1beta1MarkRecommendationClaimedRequest(_messages.Message):
  r"""Request for the `MarkRecommendationClaimed` Method.

  Messages:
    StateMetadataValue: State properties to include with this state.
      Overwrites any existing `state_metadata`. Keys must match the regex
      /^a-z0-9{0,62}$/. Values must match the regex
      /^[a-zA-Z0-9_./-]{0,255}$/.

  Fields:
    etag: Required. Fingerprint of the Recommendation. Provides optimistic
      locking.
    stateMetadata: State properties to include with this state. Overwrites any
      existing `state_metadata`. Keys must match the regex /^a-z0-9{0,62}$/.
      Values must match the regex /^[a-zA-Z0-9_./-]{0,255}$/.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class StateMetadataValue(_messages.Message):
    r"""State properties to include with this state. Overwrites any existing
    `state_metadata`. Keys must match the regex /^a-z0-9{0,62}$/. Values must
    match the regex /^[a-zA-Z0-9_./-]{0,255}$/.

    Messages:
      AdditionalProperty: An additional property for a StateMetadataValue
        object.

    Fields:
      additionalProperties: Additional properties of type StateMetadataValue
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a StateMetadataValue object.

      Fields:
        key: Name of the additional property.
        value: A string attribute.
      """

      key = _messages.StringField(1)
      value = _messages.StringField(2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  etag = _messages.StringField(1)
  stateMetadata = _messages.MessageField('StateMetadataValue', 2)


class GoogleCloudRecommenderV1beta1MarkRecommendationFailedRequest(_messages.Message):
  r"""Request for the `MarkRecommendationFailed` Method.

  Messages:
    StateMetadataValue: State properties to include with this state.
      Overwrites any existing `state_metadata`. Keys must match the regex
      /^a-z0-9{0,62}$/. Values must match the regex
      /^[a-zA-Z0-9_./-]{0,255}$/.

  Fields:
    etag: Required. Fingerprint of the Recommendation. Provides optimistic
      locking.
    stateMetadata: State properties to include with this state. Overwrites any
      existing `state_metadata`. Keys must match the regex /^a-z0-9{0,62}$/.
      Values must match the regex /^[a-zA-Z0-9_./-]{0,255}$/.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class StateMetadataValue(_messages.Message):
    r"""State properties to include with this state. Overwrites any existing
    `state_metadata`. Keys must match the regex /^a-z0-9{0,62}$/. Values must
    match the regex /^[a-zA-Z0-9_./-]{0,255}$/.

    Messages:
      AdditionalProperty: An additional property for a StateMetadataValue
        object.

    Fields:
      additionalProperties: Additional properties of type StateMetadataValue
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a StateMetadataValue object.

      Fields:
        key: Name of the additional property.
        value: A string attribute.
      """

      key = _messages.StringField(1)
      value = _messages.StringField(2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  etag = _messages.StringField(1)
  stateMetadata = _messages.MessageField('StateMetadataValue', 2)


class GoogleCloudRecommenderV1beta1MarkRecommendationSucceededRequest(_messages.Message):
  r"""Request for the `MarkRecommendationSucceeded` Method.

  Messages:
    StateMetadataValue: State properties to include with this state.
      Overwrites any existing `state_metadata`. Keys must match the regex
      /^a-z0-9{0,62}$/. Values must match the regex
      /^[a-zA-Z0-9_./-]{0,255}$/.

  Fields:
    etag: Required. Fingerprint of the Recommendation. Provides optimistic
      locking.
    stateMetadata: State properties to include with this state. Overwrites any
      existing `state_metadata`. Keys must match the regex /^a-z0-9{0,62}$/.
      Values must match the regex /^[a-zA-Z0-9_./-]{0,255}$/.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class StateMetadataValue(_messages.Message):
    r"""State properties to include with this state. Overwrites any existing
    `state_metadata`. Keys must match the regex /^a-z0-9{0,62}$/. Values must
    match the regex /^[a-zA-Z0-9_./-]{0,255}$/.

    Messages:
      AdditionalProperty: An additional property for a StateMetadataValue
        object.

    Fields:
      additionalProperties: Additional properties of type StateMetadataValue
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a StateMetadataValue object.

      Fields:
        key: Name of the additional property.
        value: A string attribute.
      """

      key = _messages.StringField(1)
      value = _messages.StringField(2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  etag = _messages.StringField(1)
  stateMetadata = _messages.MessageField('StateMetadataValue', 2)


class GoogleCloudRecommenderV1beta1Operation(_messages.Message):
  r"""Contains an operation for a resource loosely based on the JSON-PATCH
  format with support for: * Custom filters for describing partial array
  patch. * Extended path values for describing nested arrays. * Custom fields
  for describing the resource for which the operation is being described. *
  Allows extension to custom operations not natively supported by RFC6902. See
  https://tools.ietf.org/html/rfc6902 for details on the original RFC.

  Messages:
    PathFiltersValue: Set of filters to apply if `path` refers to array
      elements or nested array elements in order to narrow down to a single
      unique element that is being tested/modified. This is intended to be an
      exact match per filter. To perform advanced matching, use
      path_value_matchers. * Example: { "/versions/*/name" : "it-123"
      "/versions/*/targetSize/percent": 20 } * Example: { "/bindings/*/role":
      "roles/admin" "/bindings/*/condition" : null } * Example: {
      "/bindings/*/role": "roles/admin" "/bindings/*/members/*" :
      ["x@google.com", "y@google.com"] } When both path_filters and
      path_value_matchers are set, an implicit AND must be performed.
    PathValueMatchersValue: Similar to path_filters, this contains set of
      filters to apply if `path` field referes to array elements. This is
      meant to support value matching beyond exact match. To perform exact
      match, use path_filters. When both path_filters and path_value_matchers
      are set, an implicit AND must be performed.

  Fields:
    action: Type of this operation. Contains one of 'and', 'remove',
      'replace', 'move', 'copy', 'test' and 'custom' operations. This field is
      case-insensitive and always populated.
    path: Path to the target field being operated on. If the operation is at
      the resource level, then path should be "/". This field is always
      populated.
    pathFilters: Set of filters to apply if `path` refers to array elements or
      nested array elements in order to narrow down to a single unique element
      that is being tested/modified. This is intended to be an exact match per
      filter. To perform advanced matching, use path_value_matchers. *
      Example: { "/versions/*/name" : "it-123"
      "/versions/*/targetSize/percent": 20 } * Example: { "/bindings/*/role":
      "roles/admin" "/bindings/*/condition" : null } * Example: {
      "/bindings/*/role": "roles/admin" "/bindings/*/members/*" :
      ["x@google.com", "y@google.com"] } When both path_filters and
      path_value_matchers are set, an implicit AND must be performed.
    pathValueMatchers: Similar to path_filters, this contains set of filters
      to apply if `path` field referes to array elements. This is meant to
      support value matching beyond exact match. To perform exact match, use
      path_filters. When both path_filters and path_value_matchers are set, an
      implicit AND must be performed.
    resource: Contains the fully qualified resource name. This field is always
      populated. ex: //cloudresourcemanager.googleapis.com/projects/foo.
    resourceType: Type of GCP resource being modified/tested. This field is
      always populated. Example: cloudresourcemanager.googleapis.com/Project,
      compute.googleapis.com/Instance
    sourcePath: Can be set with action 'copy' or 'move' to indicate the source
      field within resource or source_resource, ignored if provided for other
      operation types.
    sourceResource: Can be set with action 'copy' to copy resource
      configuration across different resources of the same type. Example: A
      resource clone can be done via action = 'copy', path = "/", from = "/",
      source_resource = and resource_name = . This field is empty for all
      other values of `action`.
    value: Value for the `path` field. Will be set for
      actions:'add'/'replace'. Maybe set for action: 'test'. Either this or
      `value_matcher` will be set for 'test' operation. An exact match must be
      performed.
    valueMatcher: Can be set for action 'test' for advanced matching for the
      value of 'path' field. Either this or `value` will be set for 'test'
      operation.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class PathFiltersValue(_messages.Message):
    r"""Set of filters to apply if `path` refers to array elements or nested
    array elements in order to narrow down to a single unique element that is
    being tested/modified. This is intended to be an exact match per filter.
    To perform advanced matching, use path_value_matchers. * Example: {
    "/versions/*/name" : "it-123" "/versions/*/targetSize/percent": 20 } *
    Example: { "/bindings/*/role": "roles/admin" "/bindings/*/condition" :
    null } * Example: { "/bindings/*/role": "roles/admin"
    "/bindings/*/members/*" : ["x@google.com", "y@google.com"] } When both
    path_filters and path_value_matchers are set, an implicit AND must be
    performed.

    Messages:
      AdditionalProperty: An additional property for a PathFiltersValue
        object.

    Fields:
      additionalProperties: Additional properties of type PathFiltersValue
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a PathFiltersValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  @encoding.MapUnrecognizedFields('additionalProperties')
  class PathValueMatchersValue(_messages.Message):
    r"""Similar to path_filters, this contains set of filters to apply if
    `path` field referes to array elements. This is meant to support value
    matching beyond exact match. To perform exact match, use path_filters.
    When both path_filters and path_value_matchers are set, an implicit AND
    must be performed.

    Messages:
      AdditionalProperty: An additional property for a PathValueMatchersValue
        object.

    Fields:
      additionalProperties: Additional properties of type
        PathValueMatchersValue
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a PathValueMatchersValue object.

      Fields:
        key: Name of the additional property.
        value: A GoogleCloudRecommenderV1beta1ValueMatcher attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('GoogleCloudRecommenderV1beta1ValueMatcher', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  action = _messages.StringField(1)
  path = _messages.StringField(2)
  pathFilters = _messages.MessageField('PathFiltersValue', 3)
  pathValueMatchers = _messages.MessageField('PathValueMatchersValue', 4)
  resource = _messages.StringField(5)
  resourceType = _messages.StringField(6)
  sourcePath = _messages.StringField(7)
  sourceResource = _messages.StringField(8)
  value = _messages.MessageField('extra_types.JsonValue', 9)
  valueMatcher = _messages.MessageField('GoogleCloudRecommenderV1beta1ValueMatcher', 10)


class GoogleCloudRecommenderV1beta1OperationGroup(_messages.Message):
  r"""Group of operations that need to be performed atomically.

  Fields:
    operations: List of operations across one or more resources that belong to
      this group. Loosely based on RFC6902 and should be performed in the
      order they appear.
  """

  operations = _messages.MessageField('GoogleCloudRecommenderV1beta1Operation', 1, repeated=True)


class GoogleCloudRecommenderV1beta1Recommendation(_messages.Message):
  r"""A recommendation along with a suggested action. E.g., a rightsizing
  recommendation for an underutilized VM, IAM role recommendations, etc

  Fields:
    additionalImpact: Optional set of additional impact that this
      recommendation may have when trying to optimize for the primary
      category. These may be positive or negative.
    associatedInsights: Insights that led to this recommendation.
    content: Content of the recommendation describing recommended changes to
      resources.
    description: Free-form human readable summary in English. The maximum
      length is 500 characters.
    etag: Fingerprint of the Recommendation. Provides optimistic locking when
      updating states.
    lastRefreshTime: Last time this recommendation was refreshed by the system
      that created it in the first place.
    name: Name of recommendation.
    primaryImpact: The primary impact that this recommendation can have while
      trying to optimize for one category.
    recommenderSubtype: Contains an identifier for a subtype of
      recommendations produced for the same recommender. Subtype is a function
      of content and impact, meaning a new subtype might be added when
      significant changes to `content` or `primary_impact.category` are
      introduced. See the Recommenders section to see a list of subtypes for a
      given Recommender. Examples: For recommender =
      "google.iam.policy.Recommender", recommender_subtype can be one of
      "REMOVE_ROLE"/"REPLACE_ROLE"
    stateInfo: Information for state. Contains state and metadata.
  """

  additionalImpact = _messages.MessageField('GoogleCloudRecommenderV1beta1Impact', 1, repeated=True)
  associatedInsights = _messages.MessageField('GoogleCloudRecommenderV1beta1RecommendationInsightReference', 2, repeated=True)
  content = _messages.MessageField('GoogleCloudRecommenderV1beta1RecommendationContent', 3)
  description = _messages.StringField(4)
  etag = _messages.StringField(5)
  lastRefreshTime = _messages.StringField(6)
  name = _messages.StringField(7)
  primaryImpact = _messages.MessageField('GoogleCloudRecommenderV1beta1Impact', 8)
  recommenderSubtype = _messages.StringField(9)
  stateInfo = _messages.MessageField('GoogleCloudRecommenderV1beta1RecommendationStateInfo', 10)


class GoogleCloudRecommenderV1beta1RecommendationContent(_messages.Message):
  r"""Contains what resources are changing and how they are changing.

  Fields:
    operationGroups: Operations to one or more Google Cloud resources grouped
      in such a way that, all operations within one group are expected to be
      performed atomically and in an order.
  """

  operationGroups = _messages.MessageField('GoogleCloudRecommenderV1beta1OperationGroup', 1, repeated=True)


class GoogleCloudRecommenderV1beta1RecommendationInsightReference(_messages.Message):
  r"""Reference to an associated insight.

  Fields:
    insight: Insight resource name, e.g. projects/[PROJECT_NUMBER]/locations/[
      LOCATION]/insightTypes/[INSIGHT_TYPE_ID]/insights/[INSIGHT_ID]
  """

  insight = _messages.StringField(1)


class GoogleCloudRecommenderV1beta1RecommendationStateInfo(_messages.Message):
  r"""Information for state. Contains state and metadata.

  Enums:
    StateValueValuesEnum: The state of the recommendation, Eg ACTIVE,
      SUCCEEDED, FAILED.

  Messages:
    StateMetadataValue: A map of metadata for the state, provided by user or
      automations systems.

  Fields:
    state: The state of the recommendation, Eg ACTIVE, SUCCEEDED, FAILED.
    stateMetadata: A map of metadata for the state, provided by user or
      automations systems.
  """

  class StateValueValuesEnum(_messages.Enum):
    r"""The state of the recommendation, Eg ACTIVE, SUCCEEDED, FAILED.

    Values:
      STATE_UNSPECIFIED: Default state. Don't use directly.
      ACTIVE: Recommendation is active and can be applied. Recommendations
        content can be updated by Google. ACTIVE recommendations can be marked
        as CLAIMED, SUCCEEDED, or FAILED.
      CLAIMED: Recommendation is in claimed state. Recommendations content is
        immutable and cannot be updated by Google. CLAIMED recommendations can
        be marked as CLAIMED, SUCCEEDED, or FAILED.
      SUCCEEDED: Recommendation is in succeeded state. Recommendations content
        is immutable and cannot be updated by Google. SUCCEEDED
        recommendations can be marked as SUCCEEDED, or FAILED.
      FAILED: Recommendation is in failed state. Recommendations content is
        immutable and cannot be updated by Google. FAILED recommendations can
        be marked as SUCCEEDED, or FAILED.
      DISMISSED: Recommendation is in dismissed state. Recommendation content
        can be updated by Google. DISMISSED recommendations can be marked as
        ACTIVE.
    """
    STATE_UNSPECIFIED = 0
    ACTIVE = 1
    CLAIMED = 2
    SUCCEEDED = 3
    FAILED = 4
    DISMISSED = 5

  @encoding.MapUnrecognizedFields('additionalProperties')
  class StateMetadataValue(_messages.Message):
    r"""A map of metadata for the state, provided by user or automations
    systems.

    Messages:
      AdditionalProperty: An additional property for a StateMetadataValue
        object.

    Fields:
      additionalProperties: Additional properties of type StateMetadataValue
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a StateMetadataValue object.

      Fields:
        key: Name of the additional property.
        value: A string attribute.
      """

      key = _messages.StringField(1)
      value = _messages.StringField(2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  state = _messages.EnumField('StateValueValuesEnum', 1)
  stateMetadata = _messages.MessageField('StateMetadataValue', 2)


class GoogleCloudRecommenderV1beta1ValueMatcher(_messages.Message):
  r"""Contains various matching options for values for a GCP resource field.

  Fields:
    matchesPattern: To be used for full regex matching. The regular expression
      is using the Google RE2 syntax
      (https://github.com/google/re2/wiki/Syntax), so to be used with
      RE2::FullMatch
  """

  matchesPattern = _messages.StringField(1)


class GoogleTypeMoney(_messages.Message):
  r"""Represents an amount of money with its currency type.

  Fields:
    currencyCode: The 3-letter currency code defined in ISO 4217.
    nanos: Number of nano (10^-9) units of the amount. The value must be
      between -999,999,999 and +999,999,999 inclusive. If `units` is positive,
      `nanos` must be positive or zero. If `units` is zero, `nanos` can be
      positive, zero, or negative. If `units` is negative, `nanos` must be
      negative or zero. For example $-1.75 is represented as `units`=-1 and
      `nanos`=-750,000,000.
    units: The whole units of the amount. For example if `currencyCode` is
      `"USD"`, then 1 unit is one US dollar.
  """

  currencyCode = _messages.StringField(1)
  nanos = _messages.IntegerField(2, variant=_messages.Variant.INT32)
  units = _messages.IntegerField(3)


class RecommenderProjectsLocationsInsightTypesInsightsGetRequest(_messages.Message):
  r"""A RecommenderProjectsLocationsInsightTypesInsightsGetRequest object.

  Fields:
    name: Required. Name of the insight.
  """

  name = _messages.StringField(1, required=True)


class RecommenderProjectsLocationsInsightTypesInsightsListRequest(_messages.Message):
  r"""A RecommenderProjectsLocationsInsightTypesInsightsListRequest object.

  Fields:
    filter: Optional. Filter expression to restrict the insights returned.
      Supported filter fields: state Eg: `state:"DISMISSED" or state:"ACTIVE"
    pageSize: Optional. The maximum number of results to return from this
      request. Non-positive values are ignored. If not specified, the server
      will determine the number of results to return.
    pageToken: Optional. If present, retrieves the next batch of results from
      the preceding call to this method. `page_token` must be the value of
      `next_page_token` from the previous response. The values of other method
      parameters must be identical to those in the previous call.
    parent: Required. The container resource on which to execute the request.
      Acceptable formats: 1. "projects/[PROJECT_NUMBER]/locations/[LOCATION]/i
      nsightTypes/[INSIGHT_TYPE_ID]", LOCATION here refers to GCP Locations:
      https://cloud.google.com/about/locations/
  """

  filter = _messages.StringField(1)
  pageSize = _messages.IntegerField(2, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(3)
  parent = _messages.StringField(4, required=True)


class RecommenderProjectsLocationsInsightTypesInsightsMarkAcceptedRequest(_messages.Message):
  r"""A RecommenderProjectsLocationsInsightTypesInsightsMarkAcceptedRequest
  object.

  Fields:
    googleCloudRecommenderV1beta1MarkInsightAcceptedRequest: A
      GoogleCloudRecommenderV1beta1MarkInsightAcceptedRequest resource to be
      passed as the request body.
    name: Required. Name of the insight.
  """

  googleCloudRecommenderV1beta1MarkInsightAcceptedRequest = _messages.MessageField('GoogleCloudRecommenderV1beta1MarkInsightAcceptedRequest', 1)
  name = _messages.StringField(2, required=True)


class RecommenderProjectsLocationsRecommendersRecommendationsGetRequest(_messages.Message):
  r"""A RecommenderProjectsLocationsRecommendersRecommendationsGetRequest
  object.

  Fields:
    name: Required. Name of the recommendation.
  """

  name = _messages.StringField(1, required=True)


class RecommenderProjectsLocationsRecommendersRecommendationsListRequest(_messages.Message):
  r"""A RecommenderProjectsLocationsRecommendersRecommendationsListRequest
  object.

  Fields:
    filter: Filter expression to restrict the recommendations returned.
      Supported filter fields: state_info.state Eg:
      `state_info.state:"DISMISSED" or state_info.state:"FAILED"
    pageSize: Optional. The maximum number of results to return from this
      request. Non-positive values are ignored. If not specified, the server
      will determine the number of results to return.
    pageToken: Optional. If present, retrieves the next batch of results from
      the preceding call to this method. `page_token` must be the value of
      `next_page_token` from the previous response. The values of other method
      parameters must be identical to those in the previous call.
    parent: Required. The container resource on which to execute the request.
      Acceptable formats: 1. "projects/[PROJECT_NUMBER]/locations/[LOCATION]/r
      ecommenders/[RECOMMENDER_ID]", LOCATION here refers to GCP Locations:
      https://cloud.google.com/about/locations/
  """

  filter = _messages.StringField(1)
  pageSize = _messages.IntegerField(2, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(3)
  parent = _messages.StringField(4, required=True)


class RecommenderProjectsLocationsRecommendersRecommendationsMarkClaimedRequest(_messages.Message):
  r"""A
  RecommenderProjectsLocationsRecommendersRecommendationsMarkClaimedRequest
  object.

  Fields:
    googleCloudRecommenderV1beta1MarkRecommendationClaimedRequest: A
      GoogleCloudRecommenderV1beta1MarkRecommendationClaimedRequest resource
      to be passed as the request body.
    name: Required. Name of the recommendation.
  """

  googleCloudRecommenderV1beta1MarkRecommendationClaimedRequest = _messages.MessageField('GoogleCloudRecommenderV1beta1MarkRecommendationClaimedRequest', 1)
  name = _messages.StringField(2, required=True)


class RecommenderProjectsLocationsRecommendersRecommendationsMarkFailedRequest(_messages.Message):
  r"""A
  RecommenderProjectsLocationsRecommendersRecommendationsMarkFailedRequest
  object.

  Fields:
    googleCloudRecommenderV1beta1MarkRecommendationFailedRequest: A
      GoogleCloudRecommenderV1beta1MarkRecommendationFailedRequest resource to
      be passed as the request body.
    name: Required. Name of the recommendation.
  """

  googleCloudRecommenderV1beta1MarkRecommendationFailedRequest = _messages.MessageField('GoogleCloudRecommenderV1beta1MarkRecommendationFailedRequest', 1)
  name = _messages.StringField(2, required=True)


class RecommenderProjectsLocationsRecommendersRecommendationsMarkSucceededRequest(_messages.Message):
  r"""A
  RecommenderProjectsLocationsRecommendersRecommendationsMarkSucceededRequest
  object.

  Fields:
    googleCloudRecommenderV1beta1MarkRecommendationSucceededRequest: A
      GoogleCloudRecommenderV1beta1MarkRecommendationSucceededRequest resource
      to be passed as the request body.
    name: Required. Name of the recommendation.
  """

  googleCloudRecommenderV1beta1MarkRecommendationSucceededRequest = _messages.MessageField('GoogleCloudRecommenderV1beta1MarkRecommendationSucceededRequest', 1)
  name = _messages.StringField(2, required=True)


class StandardQueryParameters(_messages.Message):
  r"""Query parameters accepted by all methods.

  Enums:
    FXgafvValueValuesEnum: V1 error format.
    AltValueValuesEnum: Data format for response.

  Fields:
    f__xgafv: V1 error format.
    access_token: OAuth access token.
    alt: Data format for response.
    callback: JSONP
    fields: Selector specifying which fields to include in a partial response.
    key: API key. Your API key identifies your project and provides you with
      API access, quota, and reports. Required unless you provide an OAuth 2.0
      token.
    oauth_token: OAuth 2.0 token for the current user.
    prettyPrint: Returns response with indentations and line breaks.
    quotaUser: Available to use for quota purposes for server-side
      applications. Can be any arbitrary string assigned to a user, but should
      not exceed 40 characters.
    trace: A tracing token of the form "token:<tokenid>" to include in api
      requests.
    uploadType: Legacy upload protocol for media (e.g. "media", "multipart").
    upload_protocol: Upload protocol for media (e.g. "raw", "multipart").
  """

  class AltValueValuesEnum(_messages.Enum):
    r"""Data format for response.

    Values:
      json: Responses with Content-Type of application/json
      media: Media download with context-dependent Content-Type
      proto: Responses with Content-Type of application/x-protobuf
    """
    json = 0
    media = 1
    proto = 2

  class FXgafvValueValuesEnum(_messages.Enum):
    r"""V1 error format.

    Values:
      _1: v1 error format
      _2: v2 error format
    """
    _1 = 0
    _2 = 1

  f__xgafv = _messages.EnumField('FXgafvValueValuesEnum', 1)
  access_token = _messages.StringField(2)
  alt = _messages.EnumField('AltValueValuesEnum', 3, default='json')
  callback = _messages.StringField(4)
  fields = _messages.StringField(5)
  key = _messages.StringField(6)
  oauth_token = _messages.StringField(7)
  prettyPrint = _messages.BooleanField(8, default=True)
  quotaUser = _messages.StringField(9)
  trace = _messages.StringField(10)
  uploadType = _messages.StringField(11)
  upload_protocol = _messages.StringField(12)


encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2')
