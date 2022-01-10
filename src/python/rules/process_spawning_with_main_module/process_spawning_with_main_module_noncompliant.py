#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=process-spawning-with-main-module@v1.0 defects=1}
from multiprocessing import Process, set_start_method


def fork_noncompliant(message):
    print(str(message) + "fork use case!!")


# Noncompliant: fails to import main module prior to executing the function.
set_start_method('fork', force=True)
Process(target=fork_non_compliant, args=('NonCompliant',)).start()
# {/fact}
