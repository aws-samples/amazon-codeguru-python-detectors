# {fact something}
def non_compliant_put_object_if_else():
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