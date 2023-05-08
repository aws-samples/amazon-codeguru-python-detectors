#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0
# {fact rule=pytorch-use-nondeterministic-algorithm@v1.0 defects=1}
def pytorch_use_nondeterministic_algorithm_noncompliant():
    import torch
    # Noncompliant: `torch.bmm` doesn't use deterministic algorithms
    # by default.
    torch.bmm(torch.randn(2, 2, 2).to_sparse().cuda(),
              torch.randn(2, 2, 2).cuda())
# {/fact}


# {fact rule=pytorch-use-nondeterministic-algorithm@v1.0 defects=0}
def pytorch_use_nondeterministic_algorithm_compliant():
    import torch
    # Compliant: configure `torch.bmm` to use deterministic algorithms.
    torch.use_deterministic_algorithms(True)
    torch.bmm(torch.randn(2, 2, 2).to_sparse().cuda(),
              torch.randn(2, 2, 2).cuda())
# {/fact}
