#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=sns-no-bind-subscribe-publish-rule@v1.0 defects=1}
def sns_publish_noncompliant(self, sqs_arn: str, topic_arn: str) -> None:
    import boto3
    session = boto3.Session()
    sns_client = session.client('sns')
    sns_client.subscribe(TopicArn=topic_arn, Protocol='sqs',
                         Endpoint=sqs_arn,
                         ReturnSubscriptionArn=True)

    # Noncompliant: incorrect binding of SNS  publish operations
    # with 'subscribe' or 'create_topic' operations.
    sns_client.publish(TopicArn=topic_arn,
                       Message='test message for SQS',
                       MessageAttributes={'attr1': {
                           'DataType': 'String',
                           'StringValue': "short_uid"
                       }
                       }
                       )
# {/fact}


# {fact rule=sns-no-bind-subscribe-publish-rule@v1.0 defects=0}
def sns_publish_compliant(self, sqs_arn: str, topic_arn: str) -> None:
    import boto3
    session = boto3.Session()
    sns_client = session.client('sns')
    response = sns_client.subscribe(TopicArn=topic_arn, Protocol='sqs',
                                    Endpoint=sqs_arn,
                                    ReturnSubscriptionArn=True)
    # Compliant: avoids binding of SNS  publish operations
    # with 'subscribe' or 'create_topic' operations.
    return response
# {/fact}
