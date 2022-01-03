# {fact rule=sns-no-bind-subscribe-publish-rule@v1.0 defects=1}
def sns_publish_non_compliant() -> None:
    import boto3
    session = boto3.Session()
    sns_client = session.client('sns')
    topic_info = sns_client.create_topic(Name=TEST_TOPIC_NAME)
    sns_client.subscribe(TopicArn=topic_info['TopicArn'], Protocol='sqs',
                         Endpoint=aws_stack.sqs_queue_arn(
                             TEST_QUEUE_NAME_FOR_SNS),
                         ReturnSubscriptionArn=True
                         )
    test_value = short_uid()
    # Noncompliant: incorrect binding of SNS  publish operations
    # with 'subscribe' or 'create_topic' operations.
    sns_client.publish(TopicArn=topic_info['TopicArn'],
                       Message='test message for SQS',
                       MessageAttributes={'attr1': {
                           'DataType': 'String',
                           'StringValue': test_value
                       }
                       }
                       )
# {/fact}


# {fact rule=sns-no-bind-subscribe-publish-rule@v1.0 defects=0}
def sns_publish_compliant(self, sqs_arn: str, topic_arn: str) -> None:
    import boto3
    session = boto3.Session()
    sns_client = session.client('sns')
    response = sns_client.subscribe(
                TopicArn=topic_arn,
                Protocol='sqs',
                Endpoint=sqs_arn,
                ReturnSubscriptionArn=True)
    # Compliant: avoids binding of SNS  publish operations
    # with 'subscribe' or 'create_topic' operations.
    return response
# {/fact}
