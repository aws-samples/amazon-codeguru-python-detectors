#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=partial-encryption@v1.0 defects=1}
def put_object_if_else_noncompliant():
    import boto3
    client = boto3.client('s3')
    # Noncompliant: the data is not encrypted on all branches of a conditional.
    if(some_condition):
        client.put_object(
            Body='filetoupload',
            Bucket='examplebucket',
            Key='objectkey',
            SSEKMSKeyId="keyId"
        )
    else:
        client.put_object(
            Body='filetoupload',
            Bucket='examplebucket',
            Key='objectkey'
        )
# {/fact}


# {fact rule=partial-encryption@v1.0 defects=0}
def put_object_if_else_compliant():
    import boto3
    client = boto3.client('s3')
    # Compliant: the data is encrypted on all branches of the conditional.
    if(some_condition):
        some_intermediate_step = 1
        client.put_object(
            Body='filetoupload',
            Bucket='examplebucket',
            Key='objectkey',
            SSECustomerKey="keyId"
        )
        some_intermediate_step = 1
    else:
        some_intermediate_step = 1
        client.put_object(
            Body='filetoupload',
            Bucket='examplebucket',
            Key='objectkey',
            SSECustomerKey="keyId")
        some_intermediate_step = 1
# {/fact}
