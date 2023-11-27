#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=pytorch-miss-call-to-eval@v1.0 defects=1}
def pytorch_miss_call_to_eval_noncompliant(model):
    import torch
    model.load_state_dict(torch.load("model.pth"))
    # Noncompliant: miss call to `eval()` before evaluating the model.
    classes = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
               "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]
    x, y = test_data[0][0], test_data[0][1]
    with torch.no_grad():
        pred = model(x)
        predicted, actual = classes[pred[0].argmax(0)], classes[y]
        print(f'Predicted: "{predicted}", Actual: "{actual}"')
# {/fact}


# {fact rule=pytorch-miss-call-to-eval@v1.0 defects=0}
def pytorch_miss_call_to_eval_compliant(model):
    import torch
    model.load_state_dict(torch.load("model.pth"))
    classes = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
               "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]
    # Compliant: `eval()` is called before evaluating the model.
    model.eval()
    x, y = test_data[0][0], test_data[0][1]
    with torch.no_grad():
        pred = model(x)
        predicted, actual = classes[pred[0].argmax(0)], classes[y]
        print(f'Predicted: "{predicted}", Actual: "{actual}"')
# {/fact}
