#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=tensorflow-redundant-softmax@v1.0 defects=1}
def tensorflow_redundant_softmax_noncompliant():
    import tensorflow as tf
    logits = [[4.0, 2.0, 1.0], [0.0, 5.0, 1.0]]
    labels = [[1.0, 0.0, 0.0], [0.0, 0.8, 0.2]]
    # Noncompliant: using `tf.nn.softmax` with
    # `tf.nn.softmax_cross_entropy_with_logits` is redundant.
    tf.nn.softmax_cross_entropy_with_logits(
     labels=labels, logits=tf.nn.softmax(logits))
# {/fact}


# {fact rule=tensorflow-redundant-softmax@v1.0 defects=0}
def tensorflow_redundant_softmax_compliant():
    import tensorflow as tf
    logits = [[4.0, 2.0, 1.0], [0.0, 5.0, 1.0]]
    labels = [[1.0, 0.0, 0.0], [0.0, 0.8, 0.2]]
    # Compliant: unscaled `logits` is passed directly
    # to `tf.nn.softmax_cross_entropy_with_logits`.
    tf.nn.softmax_cross_entropy_with_logits(labels=labels, logits=logits)
# {/fact}
