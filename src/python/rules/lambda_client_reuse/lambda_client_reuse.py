#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=lambda-client-reuse@v1.0 defects=1}
def lambda_handler_noncompliant(event, context):
    import boto3
    # Noncompliant: recreates AWS clients in each lambda invocation.
    client = boto3.client('s3')
    response = client.list_buckets()
# {/fact}


# {fact rule=lambda-client-reuse@v1.0 defects=0}
import boto3
client = boto3.client('s3')


def lambda_handler_compliant(event, context):
    # Compliant: uses the cached client.
    response = client.list_buckets()
# {/fact}
