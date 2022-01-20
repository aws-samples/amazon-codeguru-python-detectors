#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=improper-privilege-management@v1.0 defects=1}
def set_user_noncompliant():
    import os
    root = 0
    # Noncompliant: the process user is set to root.
    os.setuid(root)
# {/fact}


# {fact rule=improper-privilege-management@v1.0 defects=0}
def set_user_compliant():
    import os
    root = 4
    # Compliant: the process user is set to userid 4.
    os.setuid(root)
# {/fact}
