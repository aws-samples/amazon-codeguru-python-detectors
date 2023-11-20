#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=s3-partial-encrypt-cdk@v1.0 defects=1}
import aws_cdk as cdk
from aws_cdk import aws_s3 as s3


class S3PartialEncrypt(cdk.Stack):

    def s3_partial_encrypt_noncompliant(self):
        # Noncompliant: No encryption specified
        bucket = s3.Bucket(self, 's3-bucket-bad')
# {/fact}
