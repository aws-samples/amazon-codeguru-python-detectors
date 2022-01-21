#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=aws-kms-reencryption@v1.0 defects=1}
def kms_reencrypt_noncompliant():
    import boto3
    import base64
    client = boto3.client('kms')
    plaintext = client.decrypt(
        CiphertextBlob=bytes(base64.b64decode("secret"))
    )
    # Noncompliant: decrypt is immediately followed by encrypt.
    response = client.encrypt(
        KeyId='string',
        Plaintext=plaintext
    )
    return response
# {/fact}


# {fact rule=aws-kms-reencryption@v1.0 defects=0}
def kms_reencrypt_compliant():
    import boto3
    import base64
    client = boto3.client('kms')
    # Compliant: server-side reencryption.
    response = client.re_encrypt(
        CiphertextBlob=bytes(base64.b64decode("secret")),
        DestinationKeyId="string",
    )
    return response
# {/fact}
