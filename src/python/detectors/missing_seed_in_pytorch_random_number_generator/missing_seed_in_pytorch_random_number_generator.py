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
    import numpy as np
    import random

    # Compliant: seed has been set.
    np.random.seed(10)
    torch.manual_seed(5)
    random.seed(10)

    x = np.random.randint(3, 2)
    y = torch.svd_lowrank(x, q=2)
    z = random.randrange(1, 8)
# {/fact}
