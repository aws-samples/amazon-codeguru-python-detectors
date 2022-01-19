#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=aws-unchecked-batch-failures@v1.0 defects=1}
def write_itemsin_batch_noncompliant(self, request_items):
    import boto3
    self.dynamodb = boto3.client('dynamodb')
    batch_list = self.dynamodb_conn.new_batch_write_list()
    batch_list.add_batch(dynamodb_table, puts=items)
    response = self.dynamodb_conn.batch_write_item(batch_list)
    # Noncompliant: unprocessed items not checked.
    return response
# {/fact}


# {fact rule=aws-unchecked-batch-failures@v1.0 defects=0}
def write_itemsin_batch_compliant(self, request_items):
    import boto3
    self.dynamodb = boto3.client('dynamodb')
    batch_list = self.dynamodb_conn.new_batch_write_list()
    batch_list.add_batch(dynamodb_table, puts=items)
    response = self.dynamodb_conn.batch_write_item(batch_list)
    # Compliant: has checks for unprocessed items.
    unprocessed = response.get('UnprocessedItems', None)
    return response, unprocessed
# {/fact}
