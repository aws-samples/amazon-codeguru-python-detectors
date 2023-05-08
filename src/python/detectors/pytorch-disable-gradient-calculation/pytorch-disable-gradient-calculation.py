# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

# {fact rule=pytorch-disable-gradient-calculation@v1.0 defects=1}
def disable_gradient_calculation_noncompliant():
    import torch
    # Noncompliant: disables gradient calculation using `torch.no_grad()`.
    with torch.no_grad():
        model.eval()
# {/fact}


# {fact rule=pytorch-disable-gradient-calculation@v1.0 defects=0}
def disable_gradient_calculation_compliant():
    import torch
    # Compliant: disables gradient calculation using `torch.inference_mode()`.
    with torch.inference_mode():
        model.eval()
# {/fact}
