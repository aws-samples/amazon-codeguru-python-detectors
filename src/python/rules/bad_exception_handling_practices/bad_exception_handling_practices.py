#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=bad-exception-handling-practices@v1.0 defects=1}
def exception_handling_noncompliant(parameter):
    if not isinstance(parameter, int):
        # Noncompliant: a generic exception is thrown.
        raise Exception("param should be an integer")
# {/fact}


# {fact rule=bad-exception-handling-practices@v1.0 defects=0}
def exception_handling_compliant(parameter):
    if not isinstance(parameter, int):
        # Compliant: specific exception is thrown.
        raise TypeError("param should be an integer")
# {/fact}
