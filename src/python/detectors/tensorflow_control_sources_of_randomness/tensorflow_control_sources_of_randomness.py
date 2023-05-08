#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=tensorflow-control-sources-of-randomness@v1.0 defects=1}
def tensorflow_control_sources_of_randomness_noncompliant():
    import tensorflow as tf
    # Noncompliant: seed is not set.
    print(tf.random.uniform([1]))
# {/fact}


# {fact rule=tensorflow-control-sources-of-randomness@v1.0 defects=0}
def tensorflow_control_sources_of_randomness_compliant(seed):
    import tensorflow as tf
    # Compliant: sets the seed.
    tf.random.set_seed(seed)
    print(tf.random.uniform([1]))
# {/fact}
