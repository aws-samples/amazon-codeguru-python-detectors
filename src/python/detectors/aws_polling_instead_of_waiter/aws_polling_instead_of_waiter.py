#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=aws-polling-instead-of-waiter@v1.0 defects=1}
def polling_vs_waiters_noncompliant(response):
    import boto3
    ec2_client = boto3.client('ec2', region_name='us-east-1')
    ec2_instance_id = response['Instances'][0]['InstanceId']

    attempts = 0
    while True:
        print("Waiting for EC2 instance to be up")
        # Noncompliant: uses custom polling instead of waiters feature.
        rsp = ec2_client.describe_instance_status(
            InstanceIds=[
                str(ec2_instance_id)
            ],
            IncludeAllInstances=True
        )

        instance_status = rsp['Statuses'][0]['InstanceStatus']['Status']
        system_status = rsp['Statuses'][0]['SystemStatus']['Status']

        if str(instance_status) == 'ok' and str(system_status) == 'ok':
            break
        if str(instance_status) == 'impaired' or \
                str(instance_status) == 'insufficient-data' or \
                str(system_status) == 'failed' or \
                str(system_status) == 'insufficient-data':
            print('Instance status is ' + str(instance_status))
            print('System status is ' + str(system_status))
            tear_down()
            exit(1)

        attempts = attempts + 1
        if attempts >= MAX_ATTEMPTS:
            print("MAX wait time for EC2 instance to be up reached.")
            print("Tearing down")
            tear_down()
            exit(1)

        time.sleep(10)
# {/fact}


# {fact rule=aws-polling-instead-of-waiter@v1.0 defects=0}
def polling_vs_waiters_compliant():
    import boto3
    client = boto3.client('kinesis', region_name='us-east-1')
    # Setup the Kinesis with 1 shard.
    stream_name = "tf_kinesis_test_1"
    client.create_stream(StreamName=stream_name, ShardCount=1)
    # Wait until stream exists, default is 10 * 18 seconds.
    # Compliant: uses waiters feature.
    client.get_waiter('stream_exists').wait(StreamName=stream_name)
    for i in range(10):
        data = "D" + str(i)
        client.put_record(
            StreamName=stream_name,
            Data=data,
            PartitionKey="TensorFlow" + str(i)
            )
# {/fact}
