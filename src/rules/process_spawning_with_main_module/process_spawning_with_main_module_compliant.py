#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=process-spawning-with-main-module@v1.0 defects=0}
from multiprocessing import Process, set_start_method


def fork_compliant(message):
    print(str(message) + "fork use case!!")


# Compliant: safely imports main module prior to executing the function.
if __name__ == '__main__':
    set_start_method('fork', force=True)
    Process(target=fork_compliant, args=('Compliant',)).start()
# {/fact}
