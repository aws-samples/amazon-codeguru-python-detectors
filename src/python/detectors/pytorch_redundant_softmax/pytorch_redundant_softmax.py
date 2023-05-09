#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=pytorch-redundant-softmax@v1.0 defects=1}
def pytorch_redundant_softmax_noncompliant():
    import torch
    from torch import nn
    from torch.utils.data import DataLoader
    from torchvision import datasets
    from torchvision.transforms import ToTensor

    training_data = datasets.FashionMNIST(
        root="data",
        train=True,
        download=True,
        transform=ToTensor()
    )

    test_data = datasets.FashionMNIST(
        root="data",
        train=False,
        download=True,
        transform=ToTensor()
    )

    train_dataloader = DataLoader(training_data, batch_size=64)
    test_dataloader = DataLoader(test_data, batch_size=64)

    class NeuralNetwork(nn.Module):
        def __init__(self):
            super().__init__()
            self.flatten = nn.Flatten()
            self.linear_relu_stack = nn.Sequential(
                nn.Linear(28 * 28, 512),
                nn.ReLU(),
                nn.Linear(512, 512),
                nn.ReLU(),
                nn.Linear(512, 10)
            )

        def forward(self, x):
            x = self.flatten(x)
            logits = self.linear_relu_stack(x)
            # Noncompliant: Softmax used with CrossEntropyLoss.
            logits = nn.functional.softmax(logits)
            return logits

    model = NeuralNetwork()

    def train_loop(dataloader, model, loss_fn, optimizer):
        size = len(dataloader.dataset)
        for batch, (x, y) in enumerate(dataloader):
            # Compute prediction and loss
            pred = model(x)
            loss = loss_fn(pred, y)

            # Backpropagation
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            if batch % 100 == 0:
                loss, current = loss.item(), (batch + 1) * len(x)
                print(f"loss: {loss:>7f}  [{current:>5d}/{size:>5d}]")

    def test_loop(dataloader, model, loss_fn):
        size = len(dataloader.dataset)
        num_batches = len(dataloader)
        test_loss, correct = 0, 0

        with torch.no_grad():
            for x, y in dataloader:
                pred = model(x)
                test_loss += loss_fn(pred, y).item()
                correct += (pred.argmax(1) == y).type(torch.float).sum().item()

        test_loss /= num_batches
        correct /= size
        print(f"Test Error: \n Accuracy: {(100 * correct):>0.1f}%, "
              f"Avg loss: {test_loss:>8f} \n")

    loss_fn = nn.CrossEntropyLoss()
    learning_rate = 0.05
    optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)

    epochs = 10
    for t in range(epochs):
        print(f"Model - Epoch {t + 1}\n-------------------------------")
        train_loop(train_dataloader, model, loss_fn, optimizer)
        test_loop(test_dataloader, model, loss_fn)

    print("Done!")
# {/fact}


# {fact rule=pytorch-redundant-softmax@v1.0 defects=0}
def pytorch_redundant_softmax_compliant():
    import torch
    import torch.nn as nn
    from transformers import BertModel, BertForSequenceClassification
    import default_constants

    class BERT(nn.Module):
        def __init__(self, tokenizer, bert_variant=default_constants.BERT):
            super(BERT, self).__init__()

            self.num_labels = default_constants.num_labels
            self.hidden_dim = default_constants.hidden_dim
            self.dropout_prob = default_constants.dropout_prob

            self.bert = BertModel.from_pretrained(bert_variant)
            self.bert.resize_token_embeddings(len(tokenizer))

            self.dropout = nn.Dropout(self.dropout_prob).cuda()
            self.classifier = nn.Linear(
                self.hidden_dim, self.num_labels).cuda()
            torch.nn.init.xavier_uniform(self.classifier.weight)

        def forward(
                self,
                text,
                labels,
                attention_mask=None,
                token_type_ids=None
        ):
            outputs = self.bert(
                text,
                attention_mask=attention_mask,
                token_type_ids=token_type_ids
            )

            pooled_output = outputs[1]

            pooled_output = self.dropout(pooled_output)
            logits = self.classifier(pooled_output)

            # Compliant: Softmax is not used with CrossEntropyLoss.
            loss_fct = nn.CrossEntropyLoss(weight=torch.Tensor(
                default_constants.class_weight)).cuda(default_constants.DEVICE)
            loss = loss_fct(logits.view(-1, self.num_labels), labels.view(-1))

            return (
                loss,
                logits,
            )
# {/fact}
