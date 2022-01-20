#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=sns-set-return-subscription-arn@v1.0 defects=1}
def set_return_subscription_noncompliant(self,
                                         sqs_arn: str,
                                         topic_arn: str) -> None:
    import botocore
    session = botocore.session.get_session()
    sns_client = session.create_client('sns', 'us-west-2')
    # Noncompliant: fails to set the 'ReturnSubscriptionArn' argument to
    # 'True' while returning the subscription ARN.
    sns_client.subscribe(TopicArn=topic_arn, Protocol='sqs',
                         Endpoint=sqs_arn)
# {/fact}


# {fact rule=sns-set-return-subscription-arn@v1.0 defects=0}
def set_return_subscription_compliant(self,
                                      sqs_arn: str,
                                      topic_arn: str) -> None:
    import botocore
    session = botocore.session.get_session()
    sns_client = session.create_client('sns', 'us-west-2')
    # Compliant: sets the 'ReturnSubscriptionArn' argument to 'True'
    # while returning the subscription ARN.
    sns_client.subscribe(TopicArn=topic_arn, Protocol='sqs',
                         Endpoint=sqs_arn, ReturnSubscriptionArn=True)
# {/fact}
