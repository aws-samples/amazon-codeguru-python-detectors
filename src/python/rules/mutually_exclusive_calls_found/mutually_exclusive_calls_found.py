#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=mutually-exclusive-calls-found@v1.0 defects=1}
def get_metrics_noncompliant() -> None:
    import boto3
    client = boto3.client('cloudwatch', region_name='eu-west-1')
    datapoints = client.get_metric_statistics(
        Namespace='CloudWatchSdkTest',
        MetricName='PythonBotoTestMetric',
        Dimensions=[
            {
                'Name': 'DimensionName',
                'Value': 'DimensionValue'
            },
        ],
        EndTime=datetime.datetime.now(datetime.timezone.utc),
        StartTime=EndTime - datetime.timedelta(days=1),
        Period=300,
        # Noncompliant: calls mutually exclusive methods.
        Statistics=[
            'SampleCount', 'Average', 'Sum', 'Minimum', 'Maximum'
        ],
        ExtendedStatistics=[
            'p70'
        ]
    )
# {/fact}


# {fact rule=mutually-exclusive-calls-found@v1.0 defects=0}
def get_metrics_compliant() -> None:
    import boto3
    client = boto3.client('cloudwatch', region_name='eu-west-1')
    datapoints = client.get_metric_statistics(
        Namespace='CloudWatchSdkTest',
        MetricName='PythonBotoTestMetric',
        Dimensions=[
            {
                'Name': 'DimensionName',
                'Value': 'DimensionValue'
            },
        ],
        EndTime=datetime.datetime.now(datetime.timezone.utc),
        StartTime=EndTime - datetime.timedelta(days=1),
        Period=300,
        # Compliant: avoid calling mutually exclusive methods.
        ExtendedStatistics=[
            'p99',
            'p100'
        ]
    )
# {/fact}
