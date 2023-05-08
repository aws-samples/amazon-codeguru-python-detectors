#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=missing-seed-in-pytorch-random-number-generator@v1.0 defects=1}
def missing_seed_in_pytorch_random_number_generator_noncompliant():
    import torch
    # Noncompliant: seed has not been set.
    tensor_1 = torch.randint(3, 10, (2, 2))
    print(tensor_1)
# {/fact}


# {fact rule=missing-seed-in-pytorch-random-number-generator@v1.0 defects=0}
def missing_seed_in_pytorch_random_number_generator_compliant():
    import torch
    seed = 42
    # Compliant: seed has been set.
    torch.manual_seed(seed)
    tensor_2 = torch.rand(2)
    print(tensor_2)
# {/fact}
