#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=module-injection@v1.0 defects=1}
def module_injection_noncompliant():
    import importlib
    module_name = input('module name')
    # Noncompliant: Untrusted user input is being passed to `import_module`.
    importlib.import_module(module_name)
# {/fact}


# {fact rule=module-injection@v1.0 defects=0}
def module_injection_compliant():
    import importlib
    allowed_module_names_list = ['example_module1', 'example_module2']
    module_name = input('module name')
    if module_name in allowed_module_names_list:
        # Compliant: User input is validated before using in `import_module()`.
        importlib.import_module(module_name)
# {/fact}
