#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=module-injection@v1.0 defects=1}
def module_injection_noncompliant():
    import yaml
    var = input()
    # Noncompliant: Load_all without processing is used.
    yaml.load_all(var)
# {/fact}


# {fact rule=module-injection@v1.0 defects=0}
def module_injection_compliant():
    import socket
    var = input()
    var = internalProcessing(var)
    # Compliant: Load_all after processing is used.
    val = yaml.load_all(var, Loader=yaml.Loader)
# {/fact}
