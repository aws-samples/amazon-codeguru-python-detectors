#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=improper-wildcard-sanitization@v1.0 defects=1}
def wildcard_sanitization_noncompliant():
    import os
    # Noncompliant: vulnerable to wildcard injection.
    os.popen('/bin/chown *')
# {/fact}


# {fact rule=improper-wildcard-sanitization@v1.0 defects=0}
def wildcard_sanitization_compliant():
    import subprocess
    # Compliant: not vulnerable to wildcard injection.
    subprocess.Popen("/bin/chown *")
# {/fact}
