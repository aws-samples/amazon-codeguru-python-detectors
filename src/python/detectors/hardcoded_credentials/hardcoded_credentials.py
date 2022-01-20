#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=hardcoded-credentials@v1.0 defects=1}
def create_session_noncompliant():
    import boto3
    # Noncompliant: uses hardcoded secret access key.
    sample_key = "AjWnyxxxxx45xxxxZxxxX7ZQxxxxYxxx1xYxxxxx"
    boto3.session.Session(aws_secret_access_key=sample_key)
# {/fact}


# {fact rule=hardcoded-credentials@v1.0 defects=0}
def create_session_compliant():
    import boto3
    import os
    # Compliant: uses environment variable for secret access key.
    sample_key = os.environ.get("AWS_SECRET_ACCESS_KEY")
    boto3.session.Session(aws_secret_access_key=sample_key)
# {/fact}
