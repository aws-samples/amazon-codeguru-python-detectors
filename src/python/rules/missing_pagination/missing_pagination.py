#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=missing-pagination@v1.0 defects=1}
def s3_loop_noncompliant(s3bucket_name, s3prefix_name):
    import boto3

    s3_client = boto3.resource('s3').meta.client
    # Noncompliant: loops through the contents without checking whether
    # more requests are needed.
    list_object_response = s3_client.list_objects_v2(Bucket=s3bucket_name,
                                                     Prefix=s3prefix_name)
    try:
        if 'Contents' in list_object_response:
            s3_deployment_folders = list_object_response['Contents']
            return s3_deployment_folders

    except ListException:
        print("List objects in bucket {} with prefix {} "
              "failed with response {}".format(s3bucket_name,
                                               s3prefix_name,
                                               list_object_response))
# {/fact}


# {fact rule=missing-pagination@v1.0 defects=0}
def s3_recursion_compliant(self, s3bucket_name, s3prefix_name, token=None):
    import boto3

    s3_client = boto3.client('s3')
    list_object_response = s3_client.list_objects_v2(
        Bucket=s3bucket_name,
        Prefix=s3prefix_name,
        ContinuationToken=token
    ) if token else s3_client.list_objects_v2(Bucket=s3bucket_name,
                                              Prefix=s3prefix_name)

    s3_deployment_folders = list_object_response['Contents']
    # Compliant: keeps requesting until no more requests are needed.
    if not list_object_response['IsTruncated']:
        return s3_deployment_folders

    next_response = self.s3_recursion_compliant(s3bucket_name, s3prefix_name,
                                                list_object_response
                                                ['NextContinuationToken'])
    s3_deployment_folders += next_response

    return s3_deployment_folders
# {/fact}
