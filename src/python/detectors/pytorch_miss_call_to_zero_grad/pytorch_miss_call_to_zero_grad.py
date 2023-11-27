#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=pytorch-miss-call-to-zero-grad@v1.0 defects=1}
def pytorch_miss_call_to_zero_grad_noncompliant(
 model, dataloader, criterion, optimizer, i_epoch):
    model.train()
    avg_loss = 0
    true_pos = 0
    true_neg = 0
    false_pos = 0
    false_neg = 0

    for i_batch, (data, offset, label) in enumerate(dataloader):
        output = model(data, offset)
        loss = criterion(output, label)
        # Noncompliant: gradients are not set to
        # zero before doing a backward pass.
        loss.backward()
        optimizer.step()
# {/fact}


# {fact rule=pytorch-miss-call-to-zero-grad@v1.0 defects=0}
def pytorch_miss_call_to_zero_grad_compliant(
 model, dataloader, criterion, optimizer, i_epoch):
    model.train()
    avg_loss = 0
    true_pos = 0
    true_neg = 0
    false_pos = 0
    false_neg = 0

    for i_batch, (data, offset, label) in enumerate(dataloader):
        output = model(data, offset)
        loss = criterion(output, label)
        # Compliant: gradients are set to zero before doing a backward pass.
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
# {/fact}
