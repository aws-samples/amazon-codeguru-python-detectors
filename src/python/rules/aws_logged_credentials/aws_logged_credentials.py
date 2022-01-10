#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=aws-logged-credentials@v1.0 defects=1}
def log_credentials_noncompliant():
    import boto3
    import logging
    session = boto3.Session()
    credentials = session.get_credentials()
    credentials = credentials.get_frozen_credentials()
    access_key = credentials.access_key
    secret_key = credentials.secret_key
    # Noncompliant: credentials are written to the logger.
    logging.info('Access key: ', access_key)
    logging.info('secret access key: ', secret_key)
# {/fact}


# {fact rule=aws-logged-credentials@v1.0 defects=0}
def log_credentials_compliant():
    import boto3
    session = boto3.Session()
    credentials = session.get_credentials()
    credentials = credentials.get_frozen_credentials()
    access_key = credentials.access_key
    secret_key = credentials.secret_key
    # Compliant: avoids writing credentials to the logger.
    session = boto3.Session(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key
    )
# {/fact}
