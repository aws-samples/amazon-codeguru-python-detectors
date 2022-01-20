#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=s3-verify-bucket-owner@v1.0 defects=1}
def verify_s3bucket_owner_noncompliant(event):
    import boto3
    client = boto3.client('s3')
    # Noncompliant: missing S3 bucket owner condition
    # (ExpectedSourceBucketOwner).
    client.copy_object(
        Bucket=event["bucket"],
        CopySource=f"{event['bucket']}/{event['key']}",
        Key=event["key"],
        ExpectedBucketOwner=event["owner"],
    )
# {/fact}


# {fact rule=s3-verify-bucket-owner@v1.0 defects=0}
def verify_s3bucket_owner_compliant(event):
    import boto3
    client = boto3.client('s3')
    # Compliant: sets the S3 bucket owner condition(ExpectedSourceBucketOwner).
    client.copy_object(
        Bucket=event["bucket"],
        CopySource=f"{event['bucket']}/{event['key']}",
        Key=event["key"],
        ExpectedBucketOwner=event["owner"],
        ExpectedSourceBucketOwner=event["owner2"]
    )
# {/fact}
