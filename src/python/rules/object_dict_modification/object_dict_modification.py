#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=object-dict-modification@v1.0 defects=1}
def modify_dictionary_noncompliant():
    import os
    # Noncompliant: modifies the __dict__ object directly.
    os.__dict__ = value
# {/fact}


# {fact rule=object-dict-modification@v1.0 defects=0}
def modify_dictionary_compliant(test_args):
    from nettles_service.models.baseline import Baseline

    baseline = Baseline(**test_args)
    for arg, value in test_args.items():
        # Compliant: avoids modifying the __dict__ object directly.
        assert baseline.__dict__[arg] == value
# {/fact}
