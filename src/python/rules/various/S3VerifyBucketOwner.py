# {fact rule=s3-verify-bucket-owner@v1.0 defects=1}
def verify_s3bucket_owner_non_compliant(_src_key,
                                        _dst_key,
                                        _bucket_name,
                                        owner,
                                        value: dict):
    import boto3
    client = boto3.client('s3')
    # Noncompliant: missing S3 bucket owner condition
    # (ExpectedSourceBucketOwner).
    client.copy_object(
        Bucket=_bucket_name,
        Key=_dst_key,
        CopySource={
            'Bucket': _bucket_name,
            'Key': _src_key
        },
        ExpectedBucketOwner=owner,
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
        ExpectedSourceBucketOwner=["owner2"]
    )
# {/fact}

