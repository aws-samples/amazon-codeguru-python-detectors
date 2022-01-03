# {fact rule=sns-set-return-subscription-arn@v1.0 defects=1}
def set_return_subscription_non_compliant() -> None:
    import boto3
    session = boto3.Session()
    sns_client = session.client('sns')
    topic_info = sns_client.create_topic(Name=TEST_TOPIC_NAME)
    # Noncompliant: fails to set the 'ReturnSubscriptionArn' argument to
    # 'True' while returning the subscription ARN.
    sns_client.subscribe(TopicArn=topic_info['TopicArn'],
                         Protocol='sqs',
                         Endpoint=aws_stack.sqs_queue_arn(
                             TEST_QUEUE_NAME_FOR_SNS
                         ))
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
