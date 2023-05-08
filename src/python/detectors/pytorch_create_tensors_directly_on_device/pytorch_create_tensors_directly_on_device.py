# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

# {fact rule=pytorch-create-tensors-directly-on-device@v1.0 defects=1}
def pytorch_create_tensors_directly_on_device_noncompliant():
    import torch
    t = torch.ones(list(range(1, 11)), dtype=torch.float64)
    # Noncompliant: tensor is created on cpu and then moved to device.
    t.cuda()
# {/fact}


# {fact rule=pytorch-create-tensors-directly-on-device@v1.0 defects=0}
def pytorch_create_tensors_directly_on_device_compliant():
    import torch
    # Compliant: tensor is directly created on device.
    t = torch.tensor([1, 2, 3, 4], device="cuda")
# {/fact}
