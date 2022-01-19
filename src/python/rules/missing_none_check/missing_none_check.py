#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=missing-none-check@v1.0 defects=1}
def none_check_noncompliant():
    import boto3
    ddb_client = boto3.client('dynamodb')
    response = ddb_client.update_item()
    # Noncompliant: does not check to verify if the ResponseMetadata is None.
    return response.get("ResponseMetadata", {})
# {/fact}


# {fact rule=missing-none-check@v1.0 defects=0}
def none_check_compliant(self, record_dicts: List[Dict]) -> Dict:
    import boto3
    kinesis_client = boto3.client('kinesis')
    response = kinesis_client.put_records(record_dicts)
    # Compliant: checks to verify if the response metadata is None.
    response_metadata = response.get('ResponseMetadata', {})
    if response_metadata is not None:
        return response_metadata
    else:
        return response
# {/fact}
