#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=aws-missing-encryption-cdk@v1.0 defects=1}
import aws_cdk as cdk
from aws_cdk import aws_sqs as sqs


class Stack(cdk.Stack):

    def missing_encryption_noncompliant(self):
        # Noncompliant: missing encryption
        unencrypted_queue = sqs.Queue(self, 'unencrypted_queue')
# {/fact}
