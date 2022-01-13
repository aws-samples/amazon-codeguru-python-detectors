#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=multiprocessing-deadlock-prevention@v1.0 defects=1}
def deadlock_prevention_noncompliant():
    from subprocess import Popen, PIPE
    process = Popen('sh ~/example.sh', stdout=PIPE)
    # Noncompliant: uses the 'Popen.wait' with 'stdout=PIPE' or 'stderr=PIPE',
    # resulting in a potential deadlock and busy loop.
    process.wait()
    print(process.returncode)
# {/fact}


# {fact rule=multiprocessing-deadlock-prevention@v1.0 defects=0}
def deadlock_prevention_compliant():
    from subprocess import Popen, PIPE
    process = Popen('sh ~/example.sh', stdout=PIPE)
    # Compliant: uses 'Popen.communicate' method, avoiding a
    # potential deadlock and busy loop.
    process.communicate()[0]
    print(process.returncode)
# {/fact}
