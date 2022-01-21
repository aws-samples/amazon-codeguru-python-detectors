#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=multidimension-list-using-replication@v1.0 defects=1}
def error_prone_multidimensional_list_noncompliant():
    # Noncompliant: initialises a multidimensional list using replication.
    multi_dimension_list = [[1]]*3
# {/fact}


# {fact rule=multidimension-list-using-replication@v1.0 defects=0}
def error_prone_multidimensional_list_compliant():
    # Compliant: avoids initialising a multidimensional list using replication.
    multi_dimension_list = [[1 for x in range(2)] for y in range(3)]
# {/fact}
