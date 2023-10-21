#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=pytorch-avoid-softmax-with-nllloss-rule@v1.0 defects=1}
def pytorch_avoid_softmax_with_nllloss_rule_noncompliant():
    import math
    import torch
    import torch.nn as nn
    # Noncompliant: `softmax` output is used directly with `NLLLoss`.
    m = nn.functional.softmax(dim=1)
    loss = nn.NLLLoss()
    input = torch.randn(3, 5, requires_grad=True)
    target = torch.tensor([1, 0, 4])
    output = loss(m(input), target)
# {/fact}


# {fact rule=pytorch-avoid-softmax-with-nllloss-rule@v1.0 defects=0}
def pytorch_avoid_softmax_with_nllloss_rule_compliant():
    import math
    import torch
    import torch.nn as nn
    # Compliant: `LogSoftmax` is used with `NLLLoss`.
    m = nn.LogSoftmax(dim=1)
    loss = nn.NLLLoss()
    input = torch.randn(3, 5, requires_grad=True)
    target = torch.tensor([1, 0, 4])
    output = loss(m(input), target)
# {/fact}
