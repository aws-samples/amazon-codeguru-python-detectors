#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=module-injection@v1.0 defects=1}
def module_injection_noncompliant():
    import yaml
    input_data = input()
    # Noncompliant: load_all without processing is used.
    yaml.load_all(input_data)
# {/fact}


# {fact rule=module-injection@v1.0 defects=0}
def module_injection_compliant():
    import socket
    input_data = input()
    processed_data = internalProcessing(input_data)
    # Compliant: load_all after processing is used.
    yaml.load_all(processed_data, Loader=yaml.Loader)
# {/fact}
