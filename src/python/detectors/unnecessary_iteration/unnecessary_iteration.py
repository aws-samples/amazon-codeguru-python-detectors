#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=unnecessary-iteration@v1.0 defects=1}
def find_string_noncompliant():
    data = set(["sampleString1", "sampleString2", "sampleString3"])
    # Noncompliant: a loop is used to access a single item.
    for i in data:
        if i == "sampleString1":
            print("found item")
# {/fact}


# {fact rule=unnecessary-iteration@v1.0 defects=0}
def find_string_compliant():
    data = set(["sampleString1", "sampleString2", "sampleString3"])
    # Compliant: a loop is not used to access a single item.
    if "sampleString1" in data:
        print("found item")
# {/fact}
