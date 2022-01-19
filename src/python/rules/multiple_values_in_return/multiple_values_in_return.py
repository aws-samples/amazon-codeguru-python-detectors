#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=multiple-values-in-return@v1.0 defects=1}
def unpack_multiple_values_noncompliant():
    # Noncompliant: uses larger number of return values
    # making it prone to errors.
    return 'a', 'abc', 100, [0, 1, 2]
# {/fact}


# {fact rule=multiple-values-in-return@v1.0 defects=0}
def unpack_multiple_values_compliant():
    # Compliant: avoids using larger number of return values
    # making it less prone to errors.
    return 'abc', 100, [0, 1, 2]
# {/fact}
