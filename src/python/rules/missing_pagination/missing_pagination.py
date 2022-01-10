#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=missing-pagination@v1.0 defects=1}
def s3_loop_noncompliant(s3bucket_name, s3prefix_name):
    import boto3

    s3_client = boto3.resource('s3').meta.client
    list_object_response = s3_client.list_objects_v2(Bucket=s3bucket_name,
                                                     Prefix=s3prefix_name)
    try:
        if 'Contents' not in list_object_response:
            raise ListException

    except ListException:
        print("List objects in bucket {} with prefix {} "
              "failed with response {}".format(s3bucket_name,
                                               s3prefix_name,
                                               list_object_response))
    # Noncompliant: loops through the contents without checking whether
    # more requests are needed.
    for source_s3_obj in list_object_response['Contents']:
        source_s3_obj_key = source_s3_obj['Key']
        target_s3_obj_key = "{}/{}".format(
            target_s3_prefix,
            remove_prefix(source_s3_obj_key, s3prefix_name).lstrip('/'))
        copy_source = {'Bucket': s3bucket_name, 'Key': source_s3_obj_key}
        try:
            if not source_s3_obj_key.endswith('$folder$'):
                s3_client.copy(copy_source,
                               target_s3_bucket,
                               target_s3_obj_key)
        except Exception as e:
            print(e)
    return {
        "output_s3_path": "s3://{}/{}".format(target_s3_bucket,
                                              target_s3_prefix)
    }
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

    next_response = self.conforming_s3_recursion(s3bucket_name, s3prefix_name,
                                                 list_object_response[
                                                     'NextContinuationToken'])
    s3_deployment_folders += next_response

    return s3_deployment_folders
# {/fact}
