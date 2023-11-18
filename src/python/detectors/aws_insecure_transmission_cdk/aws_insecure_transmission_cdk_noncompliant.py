#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=aws-insecure-transmission-cdk@v1.0 defects=1}
import aws_cdk as cdk
from aws_cdk import aws_s3 as s3


class BucketEnforceSSL(cdk.Stack):

    def aws_insecure_transmission_cdk_noncompliant(self):
        # Noncompliant: SSL configuration missing
        bucket = s3.Bucket(self, "s3-bucket-bad")
# {/fact}
