#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=dangerous-global-variables@v1.0 defects=1}
def dangerous_global_noncompliant(w):
    # Noncompliant: uses global variable, which can be accessed
    # from multiple sections.
    global width
    width = w
# {/fact}


# {fact rule=dangerous-global-variables@v1.0 defects=0}
def dangerous_global_compliant(w):
    # Compliant: avoids using global variables, restricting
    # the scope to this method.
    width = w
    return width
# {/fact}
