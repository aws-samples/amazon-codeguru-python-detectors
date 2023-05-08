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

        avg_loss += loss.item()
        # train_error += torch.sum((output > 0) != label)
        true_pos += torch.sum((output >= 0).float() * label)
        false_pos += torch.sum((output >= 0).float() * (1.0 - label))
        true_neg += torch.sum((output < 0).float() * (1.0 - label))
        false_neg += torch.sum((output < 0).float() * label)

        print(f'\rEpoch {i_epoch},\
        Training {i_batch+1:3d}/{len(dataloader):3d} batch, '
              f'loss {loss.item():0.6f}    ', end='')

    avg_loss /= len(dataloader)
    tpr = float(true_pos) / float(true_pos + false_neg)
    fpr = float(false_pos) / float(false_pos + true_neg)
    return avg_loss, tpr, fpr
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

        avg_loss += loss.item()
        # train_error += torch.sum((output > 0) != label)
        true_pos += torch.sum((output >= 0).float() * label)
        false_pos += torch.sum((output >= 0).float() * (1.0 - label))
        true_neg += torch.sum((output < 0).float() * (1.0 - label))
        false_neg += torch.sum((output < 0).float() * label)

        print(f'\rEpoch {i_epoch},\
        Training {i_batch+1:3d}/{len(dataloader):3d} batch, '
              f'loss {loss.item():0.6f}    ', end='')

    avg_loss /= len(dataloader)
    tpr = float(true_pos) / float(true_pos + false_neg)
    fpr = float(false_pos) / float(false_pos + true_neg)
    return avg_loss, tpr, fpr
# {/fact}
