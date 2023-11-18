#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=use-of-default-credentials-cdk@v1.0 defects=0}
from aws_cdk import aws_redshift as redshift
import aws_cdk as cdk


class CdkStarterStack(cdk.Stack):

    def redshift_default_username_compliant(self):
        # Compliant: Custom username used
        cfn_cluster = redshift.CfnCluster(self, "MyCfnCluster",
                                          master_username='masteruser',
                                          master_user_password='secret',
                                          cluster_type='single-node',
                                          db_name='bar',
                                          node_type='ds2.xlarge')
# {/fact}
