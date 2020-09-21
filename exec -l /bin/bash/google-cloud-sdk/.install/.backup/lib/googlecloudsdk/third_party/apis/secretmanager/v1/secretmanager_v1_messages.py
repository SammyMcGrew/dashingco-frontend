"""Generated message classes for secretmanager version v1.

Stores sensitive data such as API keys, passwords, and certificates. Provides
convenience while improving security.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding
from apitools.base.py import extra_types


package = 'secretmanager'


class AccessSecretVersionResponse(_messages.Message):
  r"""Response message for SecretManagerService.AccessSecretVersion.

  Fields:
    name: The resource name of the SecretVersion in the format
      `projects/*/secrets/*/versions/*`.
    payload: Secret payload
  """

  name = _messages.StringField(1)
  payload = _messages.MessageField('SecretPayload', 2)


class AddSecretVersionRequest(_messages.Message):
  r"""Request message for SecretManagerService.AddSecretVersion.

  Fields:
    payload: Required. The secret payload of the SecretVersion.
  """

  payload = _messages.MessageField('SecretPayload', 1)


class AuditConfig(_messages.Message):
  r"""Specifies the audit configuration for a service. The configuration
  determines which permission types are logged, and what identities, if any,
  are exempted from logging. An AuditConfig must have one or more
  AuditLogConfigs. If there are AuditConfigs for both `allServices` and a
  specific service, the union of the two AuditConfigs is used for that
  service: the log_types specified in each AuditConfig are enabled, and the
  exempted_members in each AuditLogConfig are exempted. Example Policy with
  multiple AuditConfigs: { "audit_configs": [ { "service": "allServices",
  "audit_log_configs": [ { "log_type": "DATA_READ", "exempted_members": [
  "user:jose@example.com" ] }, { "log_type": "DATA_WRITE" }, { "log_type":
  "ADMIN_READ" } ] }, { "service": "sampleservice.googleapis.com",
  "audit_log_configs": [ { "log_type": "DATA_READ" }, { "log_type":
  "DATA_WRITE", "exempted_members": [ "user:aliya@example.com" ] } ] } ] } For
  sampleservice, this policy enables DATA_READ, DATA_WRITE and ADMIN_READ
  logging. It also exempts jose@example.com from DATA_READ logging, and
  aliya@example.com from DATA_WRITE logging.

  Fields:
    auditLogConfigs: The configuration for logging of each type of permission.
    service: Specifies a service that will be enabled for audit logging. For
      example, `storage.googleapis.com`, `cloudsql.googleapis.com`.
      `allServices` is a special value that covers all services.
  """

  auditLogConfigs = _messages.MessageField('AuditLogConfig', 1, repeated=True)
  service = _messages.StringField(2)


class AuditLogConfig(_messages.Message):
  r"""Provides the configuration for logging a type of permissions. Example: {
  "audit_log_configs": [ { "log_type": "DATA_READ", "exempted_members": [
  "user:jose@example.com" ] }, { "log_type": "DATA_WRITE" } ] } This enables
  'DATA_READ' and 'DATA_WRITE' logging, while exempting jose@example.com from
  DATA_READ logging.

  Enums:
    LogTypeValueValuesEnum: The log type that this config enables.

  Fields:
    exemptedMembers: Specifies the identities that do not cause logging for
      this type of permission. Follows the same format of Binding.members.
    logType: The log type that this config enables.
  """

  class LogTypeValueValuesEnum(_messages.Enum):
    r"""The log type that this config enables.

    Values:
      LOG_TYPE_UNSPECIFIED: Default case. Should never be this.
      ADMIN_READ: Admin reads. Example: CloudIAM getIamPolicy
      DATA_WRITE: Data writes. Example: CloudSQL Users create
      DATA_READ: Data reads. Example: CloudSQL Users list
    """
    LOG_TYPE_UNSPECIFIED = 0
    ADMIN_READ = 1
    DATA_WRITE = 2
    DATA_READ = 3

  exemptedMembers = _messages.StringField(1, repeated=True)
  logType = _messages.EnumField('LogTypeValueValuesEnum', 2)


class Automatic(_messages.Message):
  r"""A replication policy that replicates the Secret payload without any
  restrictions.
  """



class Binding(_messages.Message):
  r"""Associates `members` with a `role`.

  Fields:
    condition: The condition that is associated with this binding. If the
      condition evaluates to `true`, then this binding applies to the current
      request. If the condition evaluates to `false`, then this binding does
      not apply to the current request. However, a different role binding
      might grant the same role to one or more of the members in this binding.
      To learn which resources support conditions in their IAM policies, see
      the [IAM
      documentation](https://cloud.google.com/iam/help/conditions/resource-
      policies).
    members: Specifies the identities requesting access for a Cloud Platform
      resource. `members` can have the following values: * `allUsers`: A
      special identifier that represents anyone who is on the internet; with
      or without a Google account. * `allAuthenticatedUsers`: A special
      identifier that represents anyone who is authenticated with a Google
      account or a service account. * `user:{emailid}`: An email address that
      represents a specific Google account. For example, `alice@example.com` .
      * `serviceAccount:{emailid}`: An email address that represents a service
      account. For example, `my-other-app@appspot.gserviceaccount.com`. *
      `group:{emailid}`: An email address that represents a Google group. For
      example, `admins@example.com`. *
      `deleted:user:{emailid}?uid={uniqueid}`: An email address (plus unique
      identifier) representing a user that has been recently deleted. For
      example, `alice@example.com?uid=123456789012345678901`. If the user is
      recovered, this value reverts to `user:{emailid}` and the recovered user
      retains the role in the binding. *
      `deleted:serviceAccount:{emailid}?uid={uniqueid}`: An email address
      (plus unique identifier) representing a service account that has been
      recently deleted. For example, `my-other-
      app@appspot.gserviceaccount.com?uid=123456789012345678901`. If the
      service account is undeleted, this value reverts to
      `serviceAccount:{emailid}` and the undeleted service account retains the
      role in the binding. * `deleted:group:{emailid}?uid={uniqueid}`: An
      email address (plus unique identifier) representing a Google group that
      has been recently deleted. For example,
      `admins@example.com?uid=123456789012345678901`. If the group is
      recovered, this value reverts to `group:{emailid}` and the recovered
      group retains the role in the binding. * `domain:{domain}`: The G Suite
      domain (primary) that represents all the users of that domain. For
      example, `google.com` or `example.com`.
    role: Role that is assigned to `members`. For example, `roles/viewer`,
      `roles/editor`, or `roles/owner`.
  """

  condition = _messages.MessageField('Expr', 1)
  members = _messages.StringField(2, repeated=True)
  role = _messages.StringField(3)


class DestroySecretVersionRequest(_messages.Message):
  r"""Request message for SecretManagerService.DestroySecretVersion."""


class DisableSecretVersionRequest(_messages.Message):
  r"""Request message for SecretManagerService.DisableSecretVersion."""


class Empty(_messages.Message):
  r"""A generic empty message that you can re-use to avoid defining duplicated
  empty messages in your APIs. A typical example is to use it as the request
  or the response type of an API method. For instance: service Foo { rpc
  Bar(google.protobuf.Empty) returns (google.protobuf.Empty); } The JSON
  representation for `Empty` is empty JSON object `{}`.
  """



class EnableSecretVersionRequest(_messages.Message):
  r"""Request message for SecretManagerService.EnableSecretVersion."""


class Expr(_messages.Message):
  r"""Represents a textual expression in the Common Expression Language (CEL)
  syntax. CEL is a C-like expression language. The syntax and semantics of CEL
  are documented at https://github.com/google/cel-spec. Example (Comparison):
  title: "Summary size limit" description: "Determines if a summary is less
  than 100 chars" expression: "document.summary.size() < 100" Example
  (Equality): title: "Requestor is owner" description: "Determines if
  requestor is the document owner" expression: "document.owner ==
  request.auth.claims.email" Example (Logic): title: "Public documents"
  description: "Determine whether the document should be publicly visible"
  expression: "document.type != 'private' && document.type != 'internal'"
  Example (Data Manipulation): title: "Notification string" description:
  "Create a notification string with a timestamp." expression: "'New message
  received at ' + string(document.create_time)" The exact variables and
  functions that may be referenced within an expression are determined by the
  service that evaluates it. See the service documentation for additional
  information.

  Fields:
    description: Optional. Description of the expression. This is a longer
      text which describes the expression, e.g. when hovered over it in a UI.
    expression: Textual representation of an expression in Common Expression
      Language syntax.
    location: Optional. String indicating the location of the expression for
      error reporting, e.g. a file name and a position in the file.
    title: Optional. Title for the expression, i.e. a short string describing
      its purpose. This can be used e.g. in UIs which allow to enter the
      expression.
  """

  description = _messages.StringField(1)
  expression = _messages.StringField(2)
  location = _messages.StringField(3)
  title = _messages.StringField(4)


class ListLocationsResponse(_messages.Message):
  r"""The response message for Locations.ListLocations.

  Fields:
    locations: A list of locations that matches the specified filter in the
      request.
    nextPageToken: The standard List next-page token.
  """

  locations = _messages.MessageField('Location', 1, repeated=True)
  nextPageToken = _messages.StringField(2)


class ListSecretVersionsResponse(_messages.Message):
  r"""Response message for SecretManagerService.ListSecretVersions.

  Fields:
    nextPageToken: A token to retrieve the next page of results. Pass this
      value in ListSecretVersionsRequest.page_token to retrieve the next page.
    totalSize: The total number of SecretVersions.
    versions: The list of SecretVersions sorted in reverse by create_time
      (newest first).
  """

  nextPageToken = _messages.StringField(1)
  totalSize = _messages.IntegerField(2, variant=_messages.Variant.INT32)
  versions = _messages.MessageField('SecretVersion', 3, repeated=True)


class ListSecretsResponse(_messages.Message):
  r"""Response message for SecretManagerService.ListSecrets.

  Fields:
    nextPageToken: A token to retrieve the next page of results. Pass this
      value in ListSecretsRequest.page_token to retrieve the next page.
    secrets: The list of Secrets sorted in reverse by create_time (newest
      first).
    totalSize: The total number of Secrets.
  """

  nextPageToken = _messages.StringField(1)
  secrets = _messages.MessageField('Secret', 2, repeated=True)
  totalSize = _messages.IntegerField(3, variant=_messages.Variant.INT32)


class Location(_messages.Message):
  r"""A resource that represents Google Cloud Platform location.

  Messages:
    LabelsValue: Cross-service attributes for the location. For example
      {"cloud.googleapis.com/region": "us-east1"}
    MetadataValue: Service-specific metadata. For example the available
      capacity at the given location.

  Fields:
    displayName: The friendly name for this location, typically a nearby city
      name. For example, "Tokyo".
    labels: Cross-service attributes for the location. For example
      {"cloud.googleapis.com/region": "us-east1"}
    locationId: The canonical id for this location. For example: `"us-east1"`.
    metadata: Service-specific metadata. For example the available capacity at
      the given location.
    name: Resource name for the location, which may vary between
      implementations. For example: `"projects/example-project/locations/us-
      east1"`
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class LabelsValue(_messages.Message):
    r"""Cross-service attributes for the location. For example
    {"cloud.googleapis.com/region": "us-east1"}

    Messages:
      AdditionalProperty: An additional property for a LabelsValue object.

    Fields:
      additionalProperties: Additional properties of type LabelsValue
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a LabelsValue object.

      Fields:
        key: Name of the additional property.
        value: A string attribute.
      """

      key = _messages.StringField(1)
      value = _messages.StringField(2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  @encoding.MapUnrecognizedFields('additionalProperties')
  class MetadataValue(_messages.Message):
    r"""Service-specific metadata. For example the available capacity at the
    given location.

    Messages:
      AdditionalProperty: An additional property for a MetadataValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a MetadataValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  displayName = _messages.StringField(1)
  labels = _messages.MessageField('LabelsValue', 2)
  locationId = _messages.StringField(3)
  metadata = _messages.MessageField('MetadataValue', 4)
  name = _messages.StringField(5)


class Policy(_messages.Message):
  r"""An Identity and Access Management (IAM) policy, which specifies access
  controls for Google Cloud resources. A `Policy` is a collection of
  `bindings`. A `binding` binds one or more `members` to a single `role`.
  Members can be user accounts, service accounts, Google groups, and domains
  (such as G Suite). A `role` is a named list of permissions; each `role` can
  be an IAM predefined role or a user-created custom role. For some types of
  Google Cloud resources, a `binding` can also specify a `condition`, which is
  a logical expression that allows access to a resource only if the expression
  evaluates to `true`. A condition can add constraints based on attributes of
  the request, the resource, or both. To learn which resources support
  conditions in their IAM policies, see the [IAM
  documentation](https://cloud.google.com/iam/help/conditions/resource-
  policies). **JSON example:** { "bindings": [ { "role":
  "roles/resourcemanager.organizationAdmin", "members": [
  "user:mike@example.com", "group:admins@example.com", "domain:google.com",
  "serviceAccount:my-project-id@appspot.gserviceaccount.com" ] }, { "role":
  "roles/resourcemanager.organizationViewer", "members": [
  "user:eve@example.com" ], "condition": { "title": "expirable access",
  "description": "Does not grant access after Sep 2020", "expression":
  "request.time < timestamp('2020-10-01T00:00:00.000Z')", } } ], "etag":
  "BwWWja0YfJA=", "version": 3 } **YAML example:** bindings: - members: -
  user:mike@example.com - group:admins@example.com - domain:google.com -
  serviceAccount:my-project-id@appspot.gserviceaccount.com role:
  roles/resourcemanager.organizationAdmin - members: - user:eve@example.com
  role: roles/resourcemanager.organizationViewer condition: title: expirable
  access description: Does not grant access after Sep 2020 expression:
  request.time < timestamp('2020-10-01T00:00:00.000Z') - etag: BwWWja0YfJA= -
  version: 3 For a description of IAM and its features, see the [IAM
  documentation](https://cloud.google.com/iam/docs/).

  Fields:
    auditConfigs: Specifies cloud audit logging configuration for this policy.
    bindings: Associates a list of `members` to a `role`. Optionally, may
      specify a `condition` that determines how and when the `bindings` are
      applied. Each of the `bindings` must contain at least one member.
    etag: `etag` is used for optimistic concurrency control as a way to help
      prevent simultaneous updates of a policy from overwriting each other. It
      is strongly suggested that systems make use of the `etag` in the read-
      modify-write cycle to perform policy updates in order to avoid race
      conditions: An `etag` is returned in the response to `getIamPolicy`, and
      systems are expected to put that etag in the request to `setIamPolicy`
      to ensure that their change will be applied to the same version of the
      policy. **Important:** If you use IAM Conditions, you must include the
      `etag` field whenever you call `setIamPolicy`. If you omit this field,
      then IAM allows you to overwrite a version `3` policy with a version `1`
      policy, and all of the conditions in the version `3` policy are lost.
    version: Specifies the format of the policy. Valid values are `0`, `1`,
      and `3`. Requests that specify an invalid value are rejected. Any
      operation that affects conditional role bindings must specify version
      `3`. This requirement applies to the following operations: * Getting a
      policy that includes a conditional role binding * Adding a conditional
      role binding to a policy * Changing a conditional role binding in a
      policy * Removing any role binding, with or without a condition, from a
      policy that includes conditions **Important:** If you use IAM
      Conditions, you must include the `etag` field whenever you call
      `setIamPolicy`. If you omit this field, then IAM allows you to overwrite
      a version `3` policy with a version `1` policy, and all of the
      conditions in the version `3` policy are lost. If a policy does not
      include any conditions, operations on that policy may specify any valid
      version or leave the field unset. To learn which resources support
      conditions in their IAM policies, see the [IAM
      documentation](https://cloud.google.com/iam/help/conditions/resource-
      policies).
  """

  auditConfigs = _messages.MessageField('AuditConfig', 1, repeated=True)
  bindings = _messages.MessageField('Binding', 2, repeated=True)
  etag = _messages.BytesField(3)
  version = _messages.IntegerField(4, variant=_messages.Variant.INT32)


class Replica(_messages.Message):
  r"""Represents a Replica for this Secret.

  Fields:
    location: The canonical IDs of the location to replicate data. For
      example: `"us-east1"`.
  """

  location = _messages.StringField(1)


class Replication(_messages.Message):
  r"""A policy that defines the replication configuration of data.

  Fields:
    automatic: The Secret will automatically be replicated without any
      restrictions.
    userManaged: The Secret will only be replicated into the locations
      specified.
  """

  automatic = _messages.MessageField('Automatic', 1)
  userManaged = _messages.MessageField('UserManaged', 2)


class Secret(_messages.Message):
  r"""A Secret is a logical secret whose value and versions can be accessed. A
  Secret is made up of zero or more SecretVersions that represent the secret
  data.

  Messages:
    LabelsValue: The labels assigned to this Secret. Label keys must be
      between 1 and 63 characters long, have a UTF-8 encoding of maximum 128
      bytes, and must conform to the following PCRE regular expression:
      `\p{Ll}\p{Lo}{0,62}` Label values must be between 0 and 63 characters
      long, have a UTF-8 encoding of maximum 128 bytes, and must conform to
      the following PCRE regular expression: `[\p{Ll}\p{Lo}\p{N}_-]{0,63}` No
      more than 64 labels can be assigned to a given resource.

  Fields:
    createTime: Output only. The time at which the Secret was created.
    labels: The labels assigned to this Secret. Label keys must be between 1
      and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and
      must conform to the following PCRE regular expression:
      `\p{Ll}\p{Lo}{0,62}` Label values must be between 0 and 63 characters
      long, have a UTF-8 encoding of maximum 128 bytes, and must conform to
      the following PCRE regular expression: `[\p{Ll}\p{Lo}\p{N}_-]{0,63}` No
      more than 64 labels can be assigned to a given resource.
    name: Output only. The resource name of the Secret in the format
      `projects/*/secrets/*`.
    replication: Required. Immutable. The replication policy of the secret
      data attached to the Secret. The replication policy cannot be changed
      after the Secret has been created.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class LabelsValue(_messages.Message):
    r"""The labels assigned to this Secret. Label keys must be between 1 and
    63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must
    conform to the following PCRE regular expression: `\p{Ll}\p{Lo}{0,62}`
    Label values must be between 0 and 63 characters long, have a UTF-8
    encoding of maximum 128 bytes, and must conform to the following PCRE
    regular expression: `[\p{Ll}\p{Lo}\p{N}_-]{0,63}` No more than 64 labels
    can be assigned to a given resource.

    Messages:
      AdditionalProperty: An additional property for a LabelsValue object.

    Fields:
      additionalProperties: Additional properties of type LabelsValue
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a LabelsValue object.

      Fields:
        key: Name of the additional property.
        value: A string attribute.
      """

      key = _messages.StringField(1)
      value = _messages.StringField(2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  createTime = _messages.StringField(1)
  labels = _messages.MessageField('LabelsValue', 2)
  name = _messages.StringField(3)
  replication = _messages.MessageField('Replication', 4)


class SecretPayload(_messages.Message):
  r"""A secret payload resource in the Secret Manager API. This contains the
  sensitive secret payload that is associated with a SecretVersion.

  Fields:
    data: The secret data. Must be no larger than 64KiB.
  """

  data = _messages.BytesField(1)


class SecretVersion(_messages.Message):
  r"""A secret version resource in the Secret Manager API.

  Enums:
    StateValueValuesEnum: Output only. The current state of the SecretVersion.

  Fields:
    createTime: Output only. The time at which the SecretVersion was created.
    destroyTime: Output only. The time this SecretVersion was destroyed. Only
      present if state is DESTROYED.
    name: Output only. The resource name of the SecretVersion in the format
      `projects/*/secrets/*/versions/*`. SecretVersion IDs in a Secret start
      at 1 and are incremented for each subsequent version of the secret.
    state: Output only. The current state of the SecretVersion.
  """

  class StateValueValuesEnum(_messages.Enum):
    r"""Output only. The current state of the SecretVersion.

    Values:
      STATE_UNSPECIFIED: Not specified. This value is unused and invalid.
      ENABLED: The SecretVersion may be accessed.
      DISABLED: The SecretVersion may not be accessed, but the secret data is
        still available and can be placed back into the ENABLED state.
      DESTROYED: The SecretVersion is destroyed and the secret data is no
        longer stored. A version may not leave this state once entered.
    """
    STATE_UNSPECIFIED = 0
    ENABLED = 1
    DISABLED = 2
    DESTROYED = 3

  createTime = _messages.StringField(1)
  destroyTime = _messages.StringField(2)
  name = _messages.StringField(3)
  state = _messages.EnumField('StateValueValuesEnum', 4)


class SecretmanagerProjectsLocationsGetRequest(_messages.Message):
  r"""A SecretmanagerProjectsLocationsGetRequest object.

  Fields:
    name: Resource name for the location.
  """

  name = _messages.StringField(1, required=True)


class SecretmanagerProjectsLocationsListRequest(_messages.Message):
  r"""A SecretmanagerProjectsLocationsListRequest object.

  Fields:
    filter: The standard list filter.
    name: The resource that owns the locations collection, if applicable.
    pageSize: The standard list page size.
    pageToken: The standard list page token.
  """

  filter = _messages.StringField(1)
  name = _messages.StringField(2, required=True)
  pageSize = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(4)


class SecretmanagerProjectsSecretsAddVersionRequest(_messages.Message):
  r"""A SecretmanagerProjectsSecretsAddVersionRequest object.

  Fields:
    addSecretVersionRequest: A AddSecretVersionRequest resource to be passed
      as the request body.
    parent: Required. The resource name of the Secret to associate with the
      SecretVersion in the format `projects/*/secrets/*`.
  """

  addSecretVersionRequest = _messages.MessageField('AddSecretVersionRequest', 1)
  parent = _messages.StringField(2, required=True)


class SecretmanagerProjectsSecretsCreateRequest(_messages.Message):
  r"""A SecretmanagerProjectsSecretsCreateRequest object.

  Fields:
    parent: Required. The resource name of the project to associate with the
      Secret, in the format `projects/*`.
    secret: A Secret resource to be passed as the request body.
    secretId: Required. This must be unique within the project. A secret ID is
      a string with a maximum length of 255 characters and can contain
      uppercase and lowercase letters, numerals, and the hyphen (`-`) and
      underscore (`_`) characters.
  """

  parent = _messages.StringField(1, required=True)
  secret = _messages.MessageField('Secret', 2)
  secretId = _messages.StringField(3)


class SecretmanagerProjectsSecretsDeleteRequest(_messages.Message):
  r"""A SecretmanagerProjectsSecretsDeleteRequest object.

  Fields:
    name: Required. The resource name of the Secret to delete in the format
      `projects/*/secrets/*`.
  """

  name = _messages.StringField(1, required=True)


class SecretmanagerProjectsSecretsGetIamPolicyRequest(_messages.Message):
  r"""A SecretmanagerProjectsSecretsGetIamPolicyRequest object.

  Fields:
    options_requestedPolicyVersion: Optional. The policy format version to be
      returned. Valid values are 0, 1, and 3. Requests specifying an invalid
      value will be rejected. Requests for policies with any conditional
      bindings must specify version 3. Policies without any conditional
      bindings may specify any valid value or leave the field unset. To learn
      which resources support conditions in their IAM policies, see the [IAM
      documentation](https://cloud.google.com/iam/help/conditions/resource-
      policies).
    resource: REQUIRED: The resource for which the policy is being requested.
      See the operation documentation for the appropriate value for this
      field.
  """

  options_requestedPolicyVersion = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  resource = _messages.StringField(2, required=True)


class SecretmanagerProjectsSecretsGetRequest(_messages.Message):
  r"""A SecretmanagerProjectsSecretsGetRequest object.

  Fields:
    name: Required. The resource name of the Secret, in the format
      `projects/*/secrets/*`.
  """

  name = _messages.StringField(1, required=True)


class SecretmanagerProjectsSecretsListRequest(_messages.Message):
  r"""A SecretmanagerProjectsSecretsListRequest object.

  Fields:
    pageSize: Optional. The maximum number of results to be returned in a
      single page. If set to 0, the server decides the number of results to
      return. If the number is greater than 25000, it is capped at 25000.
    pageToken: Optional. Pagination token, returned earlier via
      ListSecretsResponse.next_page_token.
    parent: Required. The resource name of the project associated with the
      Secrets, in the format `projects/*`.
  """

  pageSize = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(2)
  parent = _messages.StringField(3, required=True)


class SecretmanagerProjectsSecretsPatchRequest(_messages.Message):
  r"""A SecretmanagerProjectsSecretsPatchRequest object.

  Fields:
    name: Output only. The resource name of the Secret in the format
      `projects/*/secrets/*`.
    secret: A Secret resource to be passed as the request body.
    updateMask: Required. Specifies the fields to be updated.
  """

  name = _messages.StringField(1, required=True)
  secret = _messages.MessageField('Secret', 2)
  updateMask = _messages.StringField(3)


class SecretmanagerProjectsSecretsSetIamPolicyRequest(_messages.Message):
  r"""A SecretmanagerProjectsSecretsSetIamPolicyRequest object.

  Fields:
    resource: REQUIRED: The resource for which the policy is being specified.
      See the operation documentation for the appropriate value for this
      field.
    setIamPolicyRequest: A SetIamPolicyRequest resource to be passed as the
      request body.
  """

  resource = _messages.StringField(1, required=True)
  setIamPolicyRequest = _messages.MessageField('SetIamPolicyRequest', 2)


class SecretmanagerProjectsSecretsTestIamPermissionsRequest(_messages.Message):
  r"""A SecretmanagerProjectsSecretsTestIamPermissionsRequest object.

  Fields:
    resource: REQUIRED: The resource for which the policy detail is being
      requested. See the operation documentation for the appropriate value for
      this field.
    testIamPermissionsRequest: A TestIamPermissionsRequest resource to be
      passed as the request body.
  """

  resource = _messages.StringField(1, required=True)
  testIamPermissionsRequest = _messages.MessageField('TestIamPermissionsRequest', 2)


class SecretmanagerProjectsSecretsVersionsAccessRequest(_messages.Message):
  r"""A SecretmanagerProjectsSecretsVersionsAccessRequest object.

  Fields:
    name: Required. The resource name of the SecretVersion in the format
      `projects/*/secrets/*/versions/*`.
  """

  name = _messages.StringField(1, required=True)


class SecretmanagerProjectsSecretsVersionsDestroyRequest(_messages.Message):
  r"""A SecretmanagerProjectsSecretsVersionsDestroyRequest object.

  Fields:
    destroySecretVersionRequest: A DestroySecretVersionRequest resource to be
      passed as the request body.
    name: Required. The resource name of the SecretVersion to destroy in the
      format `projects/*/secrets/*/versions/*`.
  """

  destroySecretVersionRequest = _messages.MessageField('DestroySecretVersionRequest', 1)
  name = _messages.StringField(2, required=True)


class SecretmanagerProjectsSecretsVersionsDisableRequest(_messages.Message):
  r"""A SecretmanagerProjectsSecretsVersionsDisableRequest object.

  Fields:
    disableSecretVersionRequest: A DisableSecretVersionRequest resource to be
      passed as the request body.
    name: Required. The resource name of the SecretVersion to disable in the
      format `projects/*/secrets/*/versions/*`.
  """

  disableSecretVersionRequest = _messages.MessageField('DisableSecretVersionRequest', 1)
  name = _messages.StringField(2, required=True)


class SecretmanagerProjectsSecretsVersionsEnableRequest(_messages.Message):
  r"""A SecretmanagerProjectsSecretsVersionsEnableRequest object.

  Fields:
    enableSecretVersionRequest: A EnableSecretVersionRequest resource to be
      passed as the request body.
    name: Required. The resource name of the SecretVersion to enable in the
      format `projects/*/secrets/*/versions/*`.
  """

  enableSecretVersionRequest = _messages.MessageField('EnableSecretVersionRequest', 1)
  name = _messages.StringField(2, required=True)


class SecretmanagerProjectsSecretsVersionsGetRequest(_messages.Message):
  r"""A SecretmanagerProjectsSecretsVersionsGetRequest object.

  Fields:
    name: Required. The resource name of the SecretVersion in the format
      `projects/*/secrets/*/versions/*`.
      `projects/*/secrets/*/versions/latest` is an alias to the `latest`
      SecretVersion.
  """

  name = _messages.StringField(1, required=True)


class SecretmanagerProjectsSecretsVersionsListRequest(_messages.Message):
  r"""A SecretmanagerProjectsSecretsVersionsListRequest object.

  Fields:
    pageSize: Optional. The maximum number of results to be returned in a
      single page. If set to 0, the server decides the number of results to
      return. If the number is greater than 25000, it is capped at 25000.
    pageToken: Optional. Pagination token, returned earlier via
      ListSecretVersionsResponse.next_page_token][].
    parent: Required. The resource name of the Secret associated with the
      SecretVersions to list, in the format `projects/*/secrets/*`.
  """

  pageSize = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(2)
  parent = _messages.StringField(3, required=True)


class SetIamPolicyRequest(_messages.Message):
  r"""Request message for `SetIamPolicy` method.

  Fields:
    policy: REQUIRED: The complete policy to be applied to the `resource`. The
      size of the policy is limited to a few 10s of KB. An empty policy is a
      valid policy but certain Cloud Platform services (such as Projects)
      might reject them.
    updateMask: OPTIONAL: A FieldMask specifying which fields of the policy to
      modify. Only the fields in the mask will be modified. If no mask is
      provided, the following default mask is used: `paths: "bindings, etag"`
  """

  policy = _messages.MessageField('Policy', 1)
  updateMask = _messages.StringField(2)


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


class TestIamPermissionsRequest(_messages.Message):
  r"""Request message for `TestIamPermissions` method.

  Fields:
    permissions: The set of permissions to check for the `resource`.
      Permissions with wildcards (such as '*' or 'storage.*') are not allowed.
      For more information see [IAM
      Overview](https://cloud.google.com/iam/docs/overview#permissions).
  """

  permissions = _messages.StringField(1, repeated=True)


class TestIamPermissionsResponse(_messages.Message):
  r"""Response message for `TestIamPermissions` method.

  Fields:
    permissions: A subset of `TestPermissionsRequest.permissions` that the
      caller is allowed.
  """

  permissions = _messages.StringField(1, repeated=True)


class UserManaged(_messages.Message):
  r"""A replication policy that replicates the Secret payload into the
  locations specified in Secret.replication.user_managed.replicas

  Fields:
    replicas: Required. The list of Replicas for this Secret. Cannot be empty.
  """

  replicas = _messages.MessageField('Replica', 1, repeated=True)


encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2')
