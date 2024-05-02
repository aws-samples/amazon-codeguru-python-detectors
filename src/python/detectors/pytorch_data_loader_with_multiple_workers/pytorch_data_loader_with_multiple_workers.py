#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=pytorch-data-loader-with-multiple-workers@v1.0 defects=1}
def pytorch_data_loader_with_multiple_workers_noncompliant():
    import torch
    from torch.utils.data import DataLoader
    import numpy as np
    sampler = InfomaxNodeRecNeighborSampler(g, [fanout] * (n_layers),
                                            device=device, full_neighbor=True)
    pr_node_ids = list(sampler.hetero_map.keys())
    pr_val_ind = list(np.random.choice(len(pr_node_ids),
                                       int(len(pr_node_ids) * val_pct),
                                       replace=False))
    pr_train_ind = list(set(list(np.arange(len(pr_node_ids))))
                        .difference(set(pr_val_ind)))

    # Noncompliant: num_workers value is 8 and native python 'list'
    # is used here to store the dataset.
    loader = DataLoader(dataset=pr_train_ind,
                        batch_size=batch_size,
                        collate_fn=sampler.sample_blocks,
                        shuffle=True,
                        num_workers=8)

    optimizer = torch.optim.Adam(model.parameters(),
                                 lr=lr,
                                 weight_decay=l2norm)

    # training loop
    print("start training...")

    for epoch in range(n_epochs):
        model.train()
# {/fact}


# {fact rule=pytorch-data-loader-with-multiple-workers@v1.0 defects=0}
def pytorch_data_loader_with_multiple_workers_compliant(args):
    from torch.utils.data import Dataset, DataLoader
    import numpy as np
    import torch

    class DataIter(Dataset):
        def __init__(self):
            self.data_np = np.array([x for x in range(24000000)])

        def __len__(self):
            return len(self.data_np)

        def __getitem__(self, idx):
            data = self.data_np[idx]
            data = np.array([data], dtype=np.int64)
            return torch.tensor(data)

    train_data = DataIter()
    # Compliant: native python `list/dict` is not used to store the dataset
    # for non zero `num_workers`.
    train_loader = DataLoader(train_data, batch_size=300,
                              shuffle=True,
                              drop_last=True,
                              pin_memory=False,
                              num_workers=8)

    for i, item in enumerate(train_loader):
        if i % 1000 == 0:
            print(i)
# {/fact}
