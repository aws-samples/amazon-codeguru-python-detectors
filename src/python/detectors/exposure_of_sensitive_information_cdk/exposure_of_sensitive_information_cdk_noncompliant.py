#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=exposure-of-sensitive-information-cdk@v1.0 defects=1}
import aws_cdk as cdk
from aws_cdk.aws_ec2 import CfnSecurityGroupIngress


class SelectivePorts(cdk.Stack):

    def exposure_of_sensitive_information_noncompliant(self):
        # Noncompliant: 0.0.0.0/0 range is used
        CfnSecurityGroupIngress(cdk.Stack, 'rIngress',
                                ip_protocol='tcp',
                                cidr_ip='0.0.0.0/0')

# {/fact}
