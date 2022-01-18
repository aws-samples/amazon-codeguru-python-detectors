#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=subprocess-correct-api@v1.0 defects=1}
def subprocess_call_noncompliant():
    import subprocess
    with open("~/output.txt", "w") as f:
        # Noncompliant: uses 'subprocess.call' with
        # 'stdout = PIPE' or 'stderr = PIPE'.
        subprocess.call("~/test.sh", stdout=subprocess.PIPE)
# {/fact}


# {fact rule=subprocess-correct-api@v1.0 defects=0}
def subprocess_call_compliant():
    import subprocess
    with open("~/output.txt", "w") as f:
        # Compliant: uses 'subprocess.call' without
        # 'stdout = PIPE' or 'stderr = PIPE'.
        subprocess.call("~/test.sh", stdout=f)
# {/fact}
