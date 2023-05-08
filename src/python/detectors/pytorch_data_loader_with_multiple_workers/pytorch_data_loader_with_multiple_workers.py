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
    import torch.optim
    import torchvision.datasets as datasets
    # Data loading code
    traindir = os.path.join(args.data, 'train')
    valdir = os.path.join(args.data, 'val')
    normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                     std=[0.229, 0.224, 0.225])

    train_dataset = datasets.ImageFolder(traindir, imagenet_transforms)
    train_sampler = torch.utils.data.distributed\
        .DistributedSampler(train_dataset)

    # Compliant: args.workers value is assigned to num_workers,
    # but native python 'list/dict' is not used here to store the dataset.
    train_loader = torch.utils.data.DataLoader(train_dataset,
                                               batch_size=args.batch_size,
                                               shuffle=(train_sampler is None),
                                               num_workers=args.workers,
                                               pin_memory=True,
                                               sampler=train_sampler)

# {/fact}
