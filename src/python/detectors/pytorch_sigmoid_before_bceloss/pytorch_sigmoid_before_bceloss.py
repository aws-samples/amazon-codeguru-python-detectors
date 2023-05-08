#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=pytorch-sigmoid-before-bceloss@v1.0 defects=1}
def pytorch_sigmoid_before_bceloss_noncompliant():
    import torch
    import torch.nn as nn
    # Noncompliant: `Sigmoid` layer followed by `BCELoss`
    # is not numerically robust.
    m = nn.Sigmoid()
    loss = nn.BCELoss()

    input = torch.randn(3, requires_grad=True)
    target = torch.empty(3).random_(2)

    output = loss(m(input), target)
    output.backward()
# {/fact}


# {fact rule=pytorch-sigmoid-before-bceloss@v1.0 defects=0}
def pytorch_sigmoid_before_bceloss_compliant():
    import torch
    import torch.nn as nn
    # Compliant: `BCEWithLogitsLoss` function integrates a `Sigmoid`
    # layer and the `BCELoss` into one class
    # and is numerically robust.
    loss = nn.BCEWithLogitsLoss()

    input = torch.randn(3, requires_grad=True)
    target = torch.empty(3).random_(2)

    output = loss(input, target)
    output.backward()
# {/fact}
