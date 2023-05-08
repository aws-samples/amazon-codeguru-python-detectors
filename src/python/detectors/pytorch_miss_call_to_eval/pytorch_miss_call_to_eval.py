#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=pytorch-miss-call-to-eval@v1.0 defects=1}
def pytorch_miss_call_to_eval_noncompliant(model):
    import torch
    # Noncompliant: miss call to `eval()` after load.
    model.load_state_dict(torch.load("model.pth"))
# {/fact}


# {fact rule=pytorch-miss-call-to-eval@v1.0 defects=0}
def pytorch_miss_call_to_eval_compliant(model):
    model.load_state_dict(torch.load("model.pth"))
    # Compliant: `eval()` is called after load.
    model.eval()
# {/fact}
