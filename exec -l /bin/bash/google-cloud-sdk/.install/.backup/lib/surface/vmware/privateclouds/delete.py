# -*- coding: utf-8 -*- #
# Copyright 2020 Google LLC. All Rights Reserved.
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
"""'vmware privateclouds delete' command."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.api_lib.vmware.privateclouds import PrivatecloudsClient
from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.vmware import flags

DETAILED_HELP = {
    'DESCRIPTION':
        """
          Delete a VMware privatecloud.
        """,
    'EXAMPLES':
        """
    To delete a privatecloud called example-privatecloud in project my-project and location us-central1:

      $ {command} example-privatecloud

    Or:

      $ {command} example-privatecloud --project=my-project --location=us-central1

    Or:

      $ {command} /projects/my-project/locations/us-central1/example-privatecloud

    In the first example, the project and location are taken from gcloud properties core/project and vmware/location.
    """,
}


@base.ReleaseTracks(base.ReleaseTrack.ALPHA)
class Delete(base.DeleteCommand):
  """Delete a Cloud VMware privatecloud."""

  @staticmethod
  def Args(parser):
    """Register flags for this command."""
    flags.AddPrivatecloudArgToParser(parser, positional=True)

  def Run(self, args):
    privatecloud = args.CONCEPTS.privatecloud.Parse()
    client = PrivatecloudsClient()
    operation = client.Delete(privatecloud)
    return client.WaitForOperation(
        operation,
        'waiting for privatecloud [{}] to be deleted'.format(privatecloud),
        is_delete=True)


Delete.detailed_help = DETAILED_HELP