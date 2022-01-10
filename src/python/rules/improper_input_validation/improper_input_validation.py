#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=improper-input-validation@v1.0 defects=1}
def yaml_load_noncompliant():
    import json
    import yaml
    response = yaml.dump({'a': 1, 'b': 2, 'c': 3})
    # Noncompliant: uses unsafe yaml load.
    result = yaml.load(response)
    yaml.dump(result)
# {/fact}


# {fact rule=improper-input-validation@v1.0 defects=0}
def yaml_load_compliant():
    import json
    import yaml
    response = yaml.dump({'a': 1, 'b': 2, 'c': 3})
    # Compliant: uses safe yaml load.
    result = yaml.load(response, Loader=yaml.CSafeLoader)
    yaml.dump(result)
# {/fact}
