#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=use-of-inefficient-api@v1.0 defects=1}
def compare_strings_noncompliant():
    samplestring1 = "samplestring1"
    samplestring2 = "samplestring"
    # Noncompliant: uses find() but ignores the returned position
    # when nonnegative.
    if samplestring1.find(samplestring2) != -1:
        print("String match found.")
    else:
        print("String match not found.")
# {/fact}


# {fact rule=use-of-inefficient-api@v1.0 defects=0}
def compare_strings_compliant():
    samplestring1 = "samplestring1"
    samplestring2 = "samplestring"
    # Compliant: uses the in operator to test for presence.
    if samplestring1 in samplestring2:
        print("String match found.")
    else:
        print("String match not found.")
# {/fact}
