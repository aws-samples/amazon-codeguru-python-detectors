#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=resource-leak@v1.0 defects=1}
def read_file_noncompliant(filename):
    file = open(filename, 'r')
    # Noncompliant: method returns without properly closing the file.
    return file.readlines()
# {/fact}


# {fact rule=resource-leak@v1.0 defects=0}
def read_file_compliant(filename):
    # Compliant: file is declared using a `with` statement.
    with open(filename, 'r') as file:
        return file.readlines()
# {/fact}
