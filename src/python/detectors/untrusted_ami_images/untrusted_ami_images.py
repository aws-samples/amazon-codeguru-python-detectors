#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=untrusted-ami-images@v1.0 defects=1}
def image_filter_non_compliant():
    import boto3
    ec2 = boto3.resource('ec2')
    image_name = 'The name of the AMI (provided during image creation)'
    # Noncompliant: requests Amazon Machine Images (AMIs) with
    # only name filter ignoring owner or AMI identifiers.
    filters = [{'Name': 'name', 'Values': [image_name]}]
    images = ec2.images.filter(Filters=filters)
# {/fact}


# {fact rule=untrusted-ami-images@v1.0 defects=0}
def image_filter_compliant():
    import boto3
    ec2 = boto3.resource('ec2')
    image_name = 'The name of the AMI (provided during image creation)'
    owner_id = 'The AWS account ID of the owner'
    # Compliant: requests Amazon Machine Images (AMIs) with
    # both name and owner-id filters.
    filters = [
        {'Name': 'name', 'Values': [image_name]},
        {'Name': 'owner-id', 'Values': [owner_id]}
    ]
    images = ec2.images.filter(Filters=filters)
# {/fact}
