#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=s3-partial-encrypt-cdk@v1.0 defects=0}
import aws_cdk as cdk
from aws_cdk import aws_s3 as s3


class S3PartialEncrypt(cdk.Stack):

    def s3_partial_encrypt_compliant(self):
        # Compliant: S3_MANAGED encryption specified
        bucket = s3.Bucket(self, 's3-bucket',
                           encryption=s3.BucketEncryption.S3_MANAGED)
# {/fact}
