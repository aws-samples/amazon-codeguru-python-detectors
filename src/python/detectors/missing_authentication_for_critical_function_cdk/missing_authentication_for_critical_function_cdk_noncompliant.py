#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=missing-authentication-for-critical-function-cdk@v1.0 defects=1}
import aws_cdk as cdk
from aws_cdk import aws_s3 as s3


class S3Stack(cdk.Stack):

    def missing_authentication_noncompliant(self):
        # Noncompliant: bucket made public
        public_bucket = s3.Bucket(self, 'bucket')
        public_bucket.grant_public_access()
# {/fact}
