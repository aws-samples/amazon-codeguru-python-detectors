#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=pytorch-assign-in-place-mod@v1.0 defects=1}
def pytorch_assign_in_place_mod_noncompliant():
    import torch
    x = torch.randn([2, 2])
    y = torch.randn([2, 2])
    # Noncompliant: in-place method is called as part of assignment statement.
    z = x.add_(y)
# {/fact}


# {fact rule=pytorch-assign-in-place-mod@v1.0 defects=0}
def pytorch_assign_in_place_mod_compliant():
    import torch
    x = torch.randn([2, 2])
    y = torch.randn([2, 2])
    # Compliant: in-place method is not called as part of assignment statement.
    x.add_(y)
    z = x
# {/fact}
