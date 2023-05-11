#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=pytorch-redundant-softmax@v1.0 defects=1}
def pytorch_redundant_softmax_noncompliant():
    import matplotlib.pyplot as plt
    import pandas as pd
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
            self.softmax = nn.Softmax().cuda()

        def forward(
            self,
            text,
            labels,
            attention_mask=None,
            token_type_ids=None,
        ):

            outputs = self.bert(
                text,
                attention_mask=attention_mask,
                token_type_ids=token_type_ids,
            )

            pooled_output = outputs[1]

            pooled_output = self.dropout(pooled_output)

            # Noncompliant: Softmax is used with CrossEntropyLoss.
            logits = self.softmax(self.classifier(pooled_output))

            loss_fct = nn.CrossEntropyLoss(weight=torch.Tensor(
                    default_constants.class_weight)).cuda(
                        default_constants.DEVICE)
            loss = loss_fct(logits.view(-1, self.num_labels), labels.view(-1))

            return (
                loss,
                logits,
            )
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
