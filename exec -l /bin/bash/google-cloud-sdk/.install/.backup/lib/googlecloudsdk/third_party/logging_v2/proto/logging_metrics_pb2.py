# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: googlecloudsdk/third_party/logging_v2/proto/logging_metrics.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import distribution_pb2 as google_dot_api_dot_distribution__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import metric_pb2 as google_dot_api_dot_metric__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='googlecloudsdk/third_party/logging_v2/proto/logging_metrics.proto',
  package='google.logging.v2',
  syntax='proto3',
  serialized_options=b'\n\025com.google.logging.v2B\023LoggingMetricsProtoP\001Z8google.golang.org/genproto/googleapis/logging/v2;logging\370\001\001\252\002\027Google.Cloud.Logging.V2\312\002\027Google\\Cloud\\Logging\\V2\352\002\032Google::Cloud::Logging::V2',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nAgooglecloudsdk/third_party/logging_v2/proto/logging_metrics.proto\x12\x11google.logging.v2\x1a\x17google/api/client.proto\x1a\x1dgoogle/api/distribution.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x17google/api/metric.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/api/annotations.proto\"\x8c\x05\n\tLogMetric\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0\x41\x02\x12\x18\n\x0b\x64\x65scription\x18\x02 \x01(\tB\x03\xe0\x41\x01\x12\x13\n\x06\x66ilter\x18\x03 \x01(\tB\x03\xe0\x41\x02\x12<\n\x11metric_descriptor\x18\x05 \x01(\x0b\x32\x1c.google.api.MetricDescriptorB\x03\xe0\x41\x01\x12\x1c\n\x0fvalue_extractor\x18\x06 \x01(\tB\x03\xe0\x41\x01\x12P\n\x10label_extractors\x18\x07 \x03(\x0b\x32\x31.google.logging.v2.LogMetric.LabelExtractorsEntryB\x03\xe0\x41\x01\x12\x43\n\x0e\x62ucket_options\x18\x08 \x01(\x0b\x32&.google.api.Distribution.BucketOptionsB\x03\xe0\x41\x01\x12\x34\n\x0b\x63reate_time\x18\t \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x03\xe0\x41\x03\x12\x34\n\x0bupdate_time\x18\n \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x03\xe0\x41\x03\x12<\n\x07version\x18\x04 \x01(\x0e\x32\'.google.logging.v2.LogMetric.ApiVersionB\x02\x18\x01\x1a\x36\n\x14LabelExtractorsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x1c\n\nApiVersion\x12\x06\n\x02V2\x10\x00\x12\x06\n\x02V1\x10\x01:J\xea\x41G\n logging.googleapis.com/LogMetric\x12#projects/{project}/metrics/{metric}\"\x8d\x01\n\x15ListLogMetricsRequest\x12\x43\n\x06parent\x18\x01 \x01(\tB3\xe0\x41\x02\xfa\x41-\n+cloudresourcemanager.googleapis.com/Project\x12\x17\n\npage_token\x18\x02 \x01(\tB\x03\xe0\x41\x01\x12\x16\n\tpage_size\x18\x03 \x01(\x05\x42\x03\xe0\x41\x01\"`\n\x16ListLogMetricsResponse\x12-\n\x07metrics\x18\x01 \x03(\x0b\x32\x1c.google.logging.v2.LogMetric\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"T\n\x13GetLogMetricRequest\x12=\n\x0bmetric_name\x18\x01 \x01(\tB(\xe0\x41\x02\xfa\x41\"\n logging.googleapis.com/LogMetric\"\x85\x01\n\x16\x43reateLogMetricRequest\x12\x38\n\x06parent\x18\x01 \x01(\tB(\xe0\x41\x02\xfa\x41\"\x12 logging.googleapis.com/LogMetric\x12\x31\n\x06metric\x18\x02 \x01(\x0b\x32\x1c.google.logging.v2.LogMetricB\x03\xe0\x41\x02\"\x8a\x01\n\x16UpdateLogMetricRequest\x12=\n\x0bmetric_name\x18\x01 \x01(\tB(\xe0\x41\x02\xfa\x41\"\n logging.googleapis.com/LogMetric\x12\x31\n\x06metric\x18\x02 \x01(\x0b\x32\x1c.google.logging.v2.LogMetricB\x03\xe0\x41\x02\"W\n\x16\x44\x65leteLogMetricRequest\x12=\n\x0bmetric_name\x18\x01 \x01(\tB(\xe0\x41\x02\xfa\x41\"\n logging.googleapis.com/LogMetric2\xae\x08\n\x10MetricsServiceV2\x12\x97\x01\n\x0eListLogMetrics\x12(.google.logging.v2.ListLogMetricsRequest\x1a).google.logging.v2.ListLogMetricsResponse\"0\x82\xd3\xe4\x93\x02!\x12\x1f/v2/{parent=projects/*}/metrics\xda\x41\x06parent\x12\x92\x01\n\x0cGetLogMetric\x12&.google.logging.v2.GetLogMetricRequest\x1a\x1c.google.logging.v2.LogMetric\"<\x82\xd3\xe4\x93\x02(\x12&/v2/{metric_name=projects/*/metrics/*}\xda\x41\x0bmetric_name\x12\x9b\x01\n\x0f\x43reateLogMetric\x12).google.logging.v2.CreateLogMetricRequest\x1a\x1c.google.logging.v2.LogMetric\"?\x82\xd3\xe4\x93\x02)\"\x1f/v2/{parent=projects/*}/metrics:\x06metric\xda\x41\rparent,metric\x12\xa7\x01\n\x0fUpdateLogMetric\x12).google.logging.v2.UpdateLogMetricRequest\x1a\x1c.google.logging.v2.LogMetric\"K\x82\xd3\xe4\x93\x02\x30\x1a&/v2/{metric_name=projects/*/metrics/*}:\x06metric\xda\x41\x12metric_name,metric\x12\x92\x01\n\x0f\x44\x65leteLogMetric\x12).google.logging.v2.DeleteLogMetricRequest\x1a\x16.google.protobuf.Empty\"<\x82\xd3\xe4\x93\x02(*&/v2/{metric_name=projects/*/metrics/*}\xda\x41\x0bmetric_name\x1a\x8d\x02\xca\x41\x16logging.googleapis.com\xd2\x41\xf0\x01https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-only,https://www.googleapis.com/auth/logging.admin,https://www.googleapis.com/auth/logging.read,https://www.googleapis.com/auth/logging.writeB\xbc\x01\n\x15\x63om.google.logging.v2B\x13LoggingMetricsProtoP\x01Z8google.golang.org/genproto/googleapis/logging/v2;logging\xf8\x01\x01\xaa\x02\x17Google.Cloud.Logging.V2\xca\x02\x17Google\\Cloud\\Logging\\V2\xea\x02\x1aGoogle::Cloud::Logging::V2b\x06proto3'
  ,
  dependencies=[google_dot_api_dot_client__pb2.DESCRIPTOR,google_dot_api_dot_distribution__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_metric__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_LOGMETRIC_APIVERSION = _descriptor.EnumDescriptor(
  name='ApiVersion',
  full_name='google.logging.v2.LogMetric.ApiVersion',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='V2', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='V1', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=936,
  serialized_end=964,
)
_sym_db.RegisterEnumDescriptor(_LOGMETRIC_APIVERSION)


_LOGMETRIC_LABELEXTRACTORSENTRY = _descriptor.Descriptor(
  name='LabelExtractorsEntry',
  full_name='google.logging.v2.LogMetric.LabelExtractorsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='google.logging.v2.LogMetric.LabelExtractorsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.logging.v2.LogMetric.LabelExtractorsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=880,
  serialized_end=934,
)

_LOGMETRIC = _descriptor.Descriptor(
  name='LogMetric',
  full_name='google.logging.v2.LogMetric',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.logging.v2.LogMetric.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='google.logging.v2.LogMetric.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='filter', full_name='google.logging.v2.LogMetric.filter', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metric_descriptor', full_name='google.logging.v2.LogMetric.metric_descriptor', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value_extractor', full_name='google.logging.v2.LogMetric.value_extractor', index=4,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='label_extractors', full_name='google.logging.v2.LogMetric.label_extractors', index=5,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bucket_options', full_name='google.logging.v2.LogMetric.bucket_options', index=6,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='create_time', full_name='google.logging.v2.LogMetric.create_time', index=7,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='update_time', full_name='google.logging.v2.LogMetric.update_time', index=8,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version', full_name='google.logging.v2.LogMetric.version', index=9,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_LOGMETRIC_LABELEXTRACTORSENTRY, ],
  enum_types=[
    _LOGMETRIC_APIVERSION,
  ],
  serialized_options=b'\352AG\n logging.googleapis.com/LogMetric\022#projects/{project}/metrics/{metric}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=388,
  serialized_end=1040,
)


_LISTLOGMETRICSREQUEST = _descriptor.Descriptor(
  name='ListLogMetricsRequest',
  full_name='google.logging.v2.ListLogMetricsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='google.logging.v2.ListLogMetricsRequest.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002\372A-\n+cloudresourcemanager.googleapis.com/Project', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='google.logging.v2.ListLogMetricsRequest.page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='google.logging.v2.ListLogMetricsRequest.page_size', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1043,
  serialized_end=1184,
)


_LISTLOGMETRICSRESPONSE = _descriptor.Descriptor(
  name='ListLogMetricsResponse',
  full_name='google.logging.v2.ListLogMetricsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='metrics', full_name='google.logging.v2.ListLogMetricsResponse.metrics', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='google.logging.v2.ListLogMetricsResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1186,
  serialized_end=1282,
)


_GETLOGMETRICREQUEST = _descriptor.Descriptor(
  name='GetLogMetricRequest',
  full_name='google.logging.v2.GetLogMetricRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='metric_name', full_name='google.logging.v2.GetLogMetricRequest.metric_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002\372A\"\n logging.googleapis.com/LogMetric', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1284,
  serialized_end=1368,
)


_CREATELOGMETRICREQUEST = _descriptor.Descriptor(
  name='CreateLogMetricRequest',
  full_name='google.logging.v2.CreateLogMetricRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='google.logging.v2.CreateLogMetricRequest.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002\372A\"\022 logging.googleapis.com/LogMetric', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metric', full_name='google.logging.v2.CreateLogMetricRequest.metric', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1371,
  serialized_end=1504,
)


_UPDATELOGMETRICREQUEST = _descriptor.Descriptor(
  name='UpdateLogMetricRequest',
  full_name='google.logging.v2.UpdateLogMetricRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='metric_name', full_name='google.logging.v2.UpdateLogMetricRequest.metric_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002\372A\"\n logging.googleapis.com/LogMetric', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metric', full_name='google.logging.v2.UpdateLogMetricRequest.metric', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1507,
  serialized_end=1645,
)


_DELETELOGMETRICREQUEST = _descriptor.Descriptor(
  name='DeleteLogMetricRequest',
  full_name='google.logging.v2.DeleteLogMetricRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='metric_name', full_name='google.logging.v2.DeleteLogMetricRequest.metric_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002\372A\"\n logging.googleapis.com/LogMetric', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1647,
  serialized_end=1734,
)

_LOGMETRIC_LABELEXTRACTORSENTRY.containing_type = _LOGMETRIC
_LOGMETRIC.fields_by_name['metric_descriptor'].message_type = google_dot_api_dot_metric__pb2._METRICDESCRIPTOR
_LOGMETRIC.fields_by_name['label_extractors'].message_type = _LOGMETRIC_LABELEXTRACTORSENTRY
_LOGMETRIC.fields_by_name['bucket_options'].message_type = google_dot_api_dot_distribution__pb2._DISTRIBUTION_BUCKETOPTIONS
_LOGMETRIC.fields_by_name['create_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_LOGMETRIC.fields_by_name['update_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_LOGMETRIC.fields_by_name['version'].enum_type = _LOGMETRIC_APIVERSION
_LOGMETRIC_APIVERSION.containing_type = _LOGMETRIC
_LISTLOGMETRICSRESPONSE.fields_by_name['metrics'].message_type = _LOGMETRIC
_CREATELOGMETRICREQUEST.fields_by_name['metric'].message_type = _LOGMETRIC
_UPDATELOGMETRICREQUEST.fields_by_name['metric'].message_type = _LOGMETRIC
DESCRIPTOR.message_types_by_name['LogMetric'] = _LOGMETRIC
DESCRIPTOR.message_types_by_name['ListLogMetricsRequest'] = _LISTLOGMETRICSREQUEST
DESCRIPTOR.message_types_by_name['ListLogMetricsResponse'] = _LISTLOGMETRICSRESPONSE
DESCRIPTOR.message_types_by_name['GetLogMetricRequest'] = _GETLOGMETRICREQUEST
DESCRIPTOR.message_types_by_name['CreateLogMetricRequest'] = _CREATELOGMETRICREQUEST
DESCRIPTOR.message_types_by_name['UpdateLogMetricRequest'] = _UPDATELOGMETRICREQUEST
DESCRIPTOR.message_types_by_name['DeleteLogMetricRequest'] = _DELETELOGMETRICREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LogMetric = _reflection.GeneratedProtocolMessageType('LogMetric', (_message.Message,), {

  'LabelExtractorsEntry' : _reflection.GeneratedProtocolMessageType('LabelExtractorsEntry', (_message.Message,), {
    'DESCRIPTOR' : _LOGMETRIC_LABELEXTRACTORSENTRY,
    '__module__' : 'googlecloudsdk.third_party.logging_v2.proto.logging_metrics_pb2'
    # @@protoc_insertion_point(class_scope:google.logging.v2.LogMetric.LabelExtractorsEntry)
    })
  ,
  'DESCRIPTOR' : _LOGMETRIC,
  '__module__' : 'googlecloudsdk.third_party.logging_v2.proto.logging_metrics_pb2'
  ,
  '__doc__': """Describes a logs-based metric. The value of the metric is the number
  of log entries that match a logs filter in a given time interval.
  Logs-based metric can also be used to extract values from logs and
  create a a distribution of the values. The distribution records the
  statistics of the extracted values along with an optional histogram of
  the values as specified by the bucket options.
  
  Attributes:
      name:
          Required. The client-assigned metric identifier. Examples:
          ``"error_count"``, ``"nginx/requests"``.  Metric identifiers
          are limited to 100 characters and can include only the
          following characters: ``A-Z``, ``a-z``, ``0-9``, and the
          special characters ``_-.,+!*',()%/``. The forward-slash
          character (``/``) denotes a hierarchy of name pieces, and it
          cannot be the first character of the name.  The metric
          identifier in this field must not be `URL-encoded
          <https://en.wikipedia.org/wiki/Percent-encoding>`__. However,
          when the metric identifier appears as the ``[METRIC_ID]`` part
          of a ``metric_name`` API parameter, then the metric identifier
          must be URL-encoded. Example: ``"projects/my-
          project/metrics/nginx%2Frequests"``.
      description:
          Optional. A description of this metric, which is used in
          documentation. The maximum length of the description is 8000
          characters.
      filter:
          Required. An `advanced logs filter <https://cloud.google.com/l
          ogging/docs/view/advanced_filters>`__ which is used to match
          log entries. Example:  ::     "resource.type=gae_app AND
          severity>=ERROR"  The maximum length of the filter is 20000
          characters.
      metric_descriptor:
          Optional. The metric descriptor associated with the logs-based
          metric. If unspecified, it uses a default metric descriptor
          with a DELTA metric kind, INT64 value type, with no labels and
          a unit of "1". Such a metric counts the number of log entries
          matching the ``filter`` expression.  The ``name``, ``type``,
          and ``description`` fields in the ``metric_descriptor`` are
          output only, and is constructed using the ``name`` and
          ``description`` field in the LogMetric.  To create a logs-
          based metric that records a distribution of log values, a
          DELTA metric kind with a DISTRIBUTION value type must be used
          along with a ``value_extractor`` expression in the LogMetric.
          Each label in the metric descriptor must have a matching label
          name as the key and an extractor expression as the value in
          the ``label_extractors`` map.  The ``metric_kind`` and
          ``value_type`` fields in the ``metric_descriptor`` cannot be
          updated once initially configured. New labels can be added in
          the ``metric_descriptor``, but existing labels cannot be
          modified except for their description.
      value_extractor:
          Optional. A ``value_extractor`` is required when using a
          distribution logs-based metric to extract the values to record
          from a log entry. Two functions are supported for value
          extraction: ``EXTRACT(field)`` or ``REGEXP_EXTRACT(field,
          regex)``. The argument are: 1. field: The name of the log
          entry field from which the value is to be extracted. 2. regex:
          A regular expression using the Google RE2 syntax
          (https://github.com/google/re2/wiki/Syntax) with a single
          capture group to extract data from the specified log entry
          field. The value of the field is converted to a string before
          applying the regex. It is an error to specify a regex that
          does not include exactly one capture group.  The result of the
          extraction must be convertible to a double type, as the
          distribution always records double values. If either the
          extraction or the conversion to double fails, then those
          values are not recorded in the distribution.  Example:
          ``REGEXP_EXTRACT(jsonPayload.request, ".*quantity=(\d+).*")``
      label_extractors:
          Optional. A map from a label key string to an extractor
          expression which is used to extract data from a log entry
          field and assign as the label value. Each label key specified
          in the LabelDescriptor must have an associated extractor
          expression in this map. The syntax of the extractor expression
          is the same as for the ``value_extractor`` field.  The
          extracted value is converted to the type defined in the label
          descriptor. If the either the extraction or the type
          conversion fails, the label will have a default value. The
          default value for a string label is an empty string, for an
          integer label its 0, and for a boolean label its ``false``.
          Note that there are upper bounds on the maximum number of
          labels and the number of active time series that are allowed
          in a project.
      bucket_options:
          Optional. The ``bucket_options`` are required when the logs-
          based metric is using a DISTRIBUTION value type and it
          describes the bucket boundaries used to create a histogram of
          the extracted values.
      create_time:
          Output only. The creation timestamp of the metric.  This field
          may not be present for older metrics.
      update_time:
          Output only. The last update timestamp of the metric.  This
          field may not be present for older metrics.
      version:
          Deprecated. The API version that created or updated this
          metric. The v2 format is used by default and cannot be
          changed.
  """,
  # @@protoc_insertion_point(class_scope:google.logging.v2.LogMetric)
  })
_sym_db.RegisterMessage(LogMetric)
_sym_db.RegisterMessage(LogMetric.LabelExtractorsEntry)

ListLogMetricsRequest = _reflection.GeneratedProtocolMessageType('ListLogMetricsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTLOGMETRICSREQUEST,
  '__module__' : 'googlecloudsdk.third_party.logging_v2.proto.logging_metrics_pb2'
  ,
  '__doc__': """The parameters to ListLogMetrics.
  
  Attributes:
      parent:
          Required. The name of the project containing the metrics:  ::
          "projects/[PROJECT_ID]"
      page_token:
          Optional. If present, then retrieve the next batch of results
          from the preceding call to this method. ``pageToken`` must be
          the value of ``nextPageToken`` from the previous response. The
          values of other method parameters should be identical to those
          in the previous call.
      page_size:
          Optional. The maximum number of results to return from this
          request. Non-positive values are ignored. The presence of
          ``nextPageToken`` in the response indicates that more results
          might be available.
  """,
  # @@protoc_insertion_point(class_scope:google.logging.v2.ListLogMetricsRequest)
  })
_sym_db.RegisterMessage(ListLogMetricsRequest)

ListLogMetricsResponse = _reflection.GeneratedProtocolMessageType('ListLogMetricsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTLOGMETRICSRESPONSE,
  '__module__' : 'googlecloudsdk.third_party.logging_v2.proto.logging_metrics_pb2'
  ,
  '__doc__': """Result returned from ListLogMetrics.
  
  Attributes:
      metrics:
          A list of logs-based metrics.
      next_page_token:
          If there might be more results than appear in this response,
          then ``nextPageToken`` is included. To get the next set of
          results, call this method again using the value of
          ``nextPageToken`` as ``pageToken``.
  """,
  # @@protoc_insertion_point(class_scope:google.logging.v2.ListLogMetricsResponse)
  })
_sym_db.RegisterMessage(ListLogMetricsResponse)

GetLogMetricRequest = _reflection.GeneratedProtocolMessageType('GetLogMetricRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETLOGMETRICREQUEST,
  '__module__' : 'googlecloudsdk.third_party.logging_v2.proto.logging_metrics_pb2'
  ,
  '__doc__': """The parameters to GetLogMetric.
  
  Attributes:
      metric_name:
          Required. The resource name of the desired metric:  ::
          "projects/[PROJECT_ID]/metrics/[METRIC_ID]"
  """,
  # @@protoc_insertion_point(class_scope:google.logging.v2.GetLogMetricRequest)
  })
_sym_db.RegisterMessage(GetLogMetricRequest)

CreateLogMetricRequest = _reflection.GeneratedProtocolMessageType('CreateLogMetricRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATELOGMETRICREQUEST,
  '__module__' : 'googlecloudsdk.third_party.logging_v2.proto.logging_metrics_pb2'
  ,
  '__doc__': """The parameters to CreateLogMetric.
  
  Attributes:
      parent:
          Required. The resource name of the project in which to create
          the metric:  ::     "projects/[PROJECT_ID]"  The new metric
          must be provided in the request.
      metric:
          Required. The new logs-based metric, which must not have an
          identifier that already exists.
  """,
  # @@protoc_insertion_point(class_scope:google.logging.v2.CreateLogMetricRequest)
  })
_sym_db.RegisterMessage(CreateLogMetricRequest)

UpdateLogMetricRequest = _reflection.GeneratedProtocolMessageType('UpdateLogMetricRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATELOGMETRICREQUEST,
  '__module__' : 'googlecloudsdk.third_party.logging_v2.proto.logging_metrics_pb2'
  ,
  '__doc__': """The parameters to UpdateLogMetric.
  
  Attributes:
      metric_name:
          Required. The resource name of the metric to update:  ::
          "projects/[PROJECT_ID]/metrics/[METRIC_ID]"  The updated
          metric must be provided in the request and it's ``name`` field
          must be the same as ``[METRIC_ID]`` If the metric does not
          exist in ``[PROJECT_ID]``, then a new metric is created.
      metric:
          Required. The updated metric.
  """,
  # @@protoc_insertion_point(class_scope:google.logging.v2.UpdateLogMetricRequest)
  })
_sym_db.RegisterMessage(UpdateLogMetricRequest)

DeleteLogMetricRequest = _reflection.GeneratedProtocolMessageType('DeleteLogMetricRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETELOGMETRICREQUEST,
  '__module__' : 'googlecloudsdk.third_party.logging_v2.proto.logging_metrics_pb2'
  ,
  '__doc__': """The parameters to DeleteLogMetric.
  
  Attributes:
      metric_name:
          Required. The resource name of the metric to delete:  ::
          "projects/[PROJECT_ID]/metrics/[METRIC_ID]"
  """,
  # @@protoc_insertion_point(class_scope:google.logging.v2.DeleteLogMetricRequest)
  })
_sym_db.RegisterMessage(DeleteLogMetricRequest)


DESCRIPTOR._options = None
_LOGMETRIC_LABELEXTRACTORSENTRY._options = None
_LOGMETRIC.fields_by_name['name']._options = None
_LOGMETRIC.fields_by_name['description']._options = None
_LOGMETRIC.fields_by_name['filter']._options = None
_LOGMETRIC.fields_by_name['metric_descriptor']._options = None
_LOGMETRIC.fields_by_name['value_extractor']._options = None
_LOGMETRIC.fields_by_name['label_extractors']._options = None
_LOGMETRIC.fields_by_name['bucket_options']._options = None
_LOGMETRIC.fields_by_name['create_time']._options = None
_LOGMETRIC.fields_by_name['update_time']._options = None
_LOGMETRIC.fields_by_name['version']._options = None
_LOGMETRIC._options = None
_LISTLOGMETRICSREQUEST.fields_by_name['parent']._options = None
_LISTLOGMETRICSREQUEST.fields_by_name['page_token']._options = None
_LISTLOGMETRICSREQUEST.fields_by_name['page_size']._options = None
_GETLOGMETRICREQUEST.fields_by_name['metric_name']._options = None
_CREATELOGMETRICREQUEST.fields_by_name['parent']._options = None
_CREATELOGMETRICREQUEST.fields_by_name['metric']._options = None
_UPDATELOGMETRICREQUEST.fields_by_name['metric_name']._options = None
_UPDATELOGMETRICREQUEST.fields_by_name['metric']._options = None
_DELETELOGMETRICREQUEST.fields_by_name['metric_name']._options = None

_METRICSSERVICEV2 = _descriptor.ServiceDescriptor(
  name='MetricsServiceV2',
  full_name='google.logging.v2.MetricsServiceV2',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\312A\026logging.googleapis.com\322A\360\001https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-only,https://www.googleapis.com/auth/logging.admin,https://www.googleapis.com/auth/logging.read,https://www.googleapis.com/auth/logging.write',
  create_key=_descriptor._internal_create_key,
  serialized_start=1737,
  serialized_end=2807,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListLogMetrics',
    full_name='google.logging.v2.MetricsServiceV2.ListLogMetrics',
    index=0,
    containing_service=None,
    input_type=_LISTLOGMETRICSREQUEST,
    output_type=_LISTLOGMETRICSRESPONSE,
    serialized_options=b'\202\323\344\223\002!\022\037/v2/{parent=projects/*}/metrics\332A\006parent',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetLogMetric',
    full_name='google.logging.v2.MetricsServiceV2.GetLogMetric',
    index=1,
    containing_service=None,
    input_type=_GETLOGMETRICREQUEST,
    output_type=_LOGMETRIC,
    serialized_options=b'\202\323\344\223\002(\022&/v2/{metric_name=projects/*/metrics/*}\332A\013metric_name',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CreateLogMetric',
    full_name='google.logging.v2.MetricsServiceV2.CreateLogMetric',
    index=2,
    containing_service=None,
    input_type=_CREATELOGMETRICREQUEST,
    output_type=_LOGMETRIC,
    serialized_options=b'\202\323\344\223\002)\"\037/v2/{parent=projects/*}/metrics:\006metric\332A\rparent,metric',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateLogMetric',
    full_name='google.logging.v2.MetricsServiceV2.UpdateLogMetric',
    index=3,
    containing_service=None,
    input_type=_UPDATELOGMETRICREQUEST,
    output_type=_LOGMETRIC,
    serialized_options=b'\202\323\344\223\0020\032&/v2/{metric_name=projects/*/metrics/*}:\006metric\332A\022metric_name,metric',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteLogMetric',
    full_name='google.logging.v2.MetricsServiceV2.DeleteLogMetric',
    index=4,
    containing_service=None,
    input_type=_DELETELOGMETRICREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=b'\202\323\344\223\002(*&/v2/{metric_name=projects/*/metrics/*}\332A\013metric_name',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_METRICSSERVICEV2)

DESCRIPTOR.services_by_name['MetricsServiceV2'] = _METRICSSERVICEV2

# @@protoc_insertion_point(module_scope)
