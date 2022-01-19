#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=leaky-subprocess-timeout@v1.0 defects=1}
def subprocess_timeout_noncompliant():
    import subprocess
    process = subprocess.Popen("ls -al",
                               bufsize=-1,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    try:
        # Noncompliant: fails to terminate the child process before
        # the timeout expires.
        outs, errs = process.communicate(timeout=15)
    except subprocess.TimeoutExpired:
        print("Timed out")
# {/fact}


# {fact rule=leaky-subprocess-timeout@v1.0 defects=0}
def subprocess_timeout_compliant():
    import subprocess
    process = subprocess.Popen("ls -al",
                               bufsize=-1,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    try:
        # Compliant: makes sure to terminate the child process when
        # the timeout expires.
        outs, errs = process.communicate(timeout=15)
    except subprocess.TimeoutExpired:
        process.kill()
        outs, errs = process.communicate()
# {/fact}
