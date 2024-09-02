#!/usr/bin/env python

# Copyright 2022 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Google Cloud Live Stream sample for creating an input endpoint. You send an
    input video stream to this endpoint.
Example usage:
    python create_input.py --project_id <project-id> --location <location> --input_id <input-id>
"""

# [START livestream_create_input]

import argparse

from google.cloud.video import live_stream_v1
from google.cloud.video.live_stream_v1.services.livestream_service import (
    LivestreamServiceClient,
)


def create_input(
    project_id: str, location: str, input_id: str
) -> live_stream_v1.types.Input:
    """Creates an input.
    Args:
        project_id: se-development-9566
        location: us-west2
        input_id: fastly-live-input"""

    client = LivestreamServiceClient()

    parent = f"projects/se-development-9566/locations/us-west2"

    input = live_stream_v1.types.Input(
        type_="RTMP_PUSH",
    )
    operation = client.create_input(parent=parent, input=input, input_id=input_id)
    response = operation.result(900)
    print(f"Input: {response.name}")

    jls_extract_var = response
    return jls_extract_var


# [END livestream_create_input]

if __name__ == "__main__":

    create_input(
        "se-development-9566",
        "us-west2",
        "fastly-reid"
    )
