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
"""List certificates within a project."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from apitools.base.py import list_pager

from googlecloudsdk.api_lib.privateca import base as privateca_base
from googlecloudsdk.api_lib.util import common_args
from googlecloudsdk.calliope import base
from googlecloudsdk.calliope import exceptions
from googlecloudsdk.command_lib.privateca import resource_args
from googlecloudsdk.command_lib.privateca import response_utils
from googlecloudsdk.command_lib.privateca import text_utils
from googlecloudsdk.command_lib.util.concepts import concept_parsers
from googlecloudsdk.command_lib.util.concepts import presentation_specs
from googlecloudsdk.core import properties


def _ParseParentName(args):
  """Gets the parent resource name under which to list certificates."""
  ca_ref = args.CONCEPTS.issuer.Parse()
  if ca_ref:
    return ca_ref.RelativeName()

  if args.IsSpecified('issuer'):
    raise exceptions.InvalidArgumentException(
        '--issuer',
        ('The issuer flag is not fully specified. Please add the '
         "--issuer-location flag or specify the issuer's full resource name."))

  project = properties.VALUES.core.project.GetOrFail()

  if args.IsSpecified('location'):
    return 'projects/{}/locations/{}/certificateAuthorities/-'.format(
        project, args.location)

  return 'projects/{}/locations/-/certificateAuthorities/-'.format(project)


class List(base.ListCommand):
  """List certificates within a project."""

  @staticmethod
  def Args(parser):
    base.Argument(
        '--location',
        help='Location of the certificates.'
    ).AddToParser(parser)
    concept_parsers.ConceptParser(
        [
            presentation_specs.ResourcePresentationSpec(
                '--issuer',
                resource_args.CreateCertificateAuthorityResourceSpec(
                    'CERTIFICATE_AUTHORITY'),
                'The issuing Certificate Authority.',
                required=False,
                prefixes=True),
        ]).AddToParser(parser)
    base.PAGE_SIZE_FLAG.SetDefault(parser, 100)

    parser.display_info.AddFormat("""
        table(
          name.basename(),
          name.scope().segment(-3):label=ISSUER,
          name.scope().segment(-5):label=LOCATION,
          revocation_details.yesno(yes="REVOKED", no="ACTIVE"):label=REVOCATION_STATUS,
          certificate_description.subject_description.not_before_time():label=NOT_BEFORE,
          certificate_description.subject_description.not_after_time():label=NOT_AFTER)
        """)
    parser.display_info.AddTransforms({
        'not_before_time': text_utils.TransformNotBeforeTime,
        'not_after_time': text_utils.TransformNotAfterTime
    })

  def Run(self, args):
    client = privateca_base.GetClientInstance()
    messages = privateca_base.GetMessagesModule()

    parent = _ParseParentName(args)
    request = messages.PrivatecaProjectsLocationsCertificateAuthoritiesCertificatesListRequest(
        parent=parent,
        orderBy=common_args.ParseSortByArg(args.sort_by),
        pageSize=args.page_size,
        filter=args.filter)

    return list_pager.YieldFromList(
        client.projects_locations_certificateAuthorities_certificates,
        request,
        field='certificates',
        limit=args.limit,
        batch_size_attribute='pageSize',
        get_field_func=response_utils.GetFieldAndLogUnreachable)
