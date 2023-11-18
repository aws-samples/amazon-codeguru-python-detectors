#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=api-logging-disabled@v1.0 defects=0}
import aws_cdk as cdk
from aws_cdk import aws_apigatewayv2


class APILoggingDisabled(cdk.Stack):

    def api_logging_disabled_compliant(self):
        # Compliant: logging present
        aws_apigatewayv2.CfnStage(self, 'rStage',
                                  access_log_settings=aws_apigatewayv2
                                  .CfnStage.access_log_settingsProperty(
                                      destination_arn='foo',
                                      format='$context.requestId'),
                                  api_id='bar',
                                  stage_name='baz')
# {/fact}
