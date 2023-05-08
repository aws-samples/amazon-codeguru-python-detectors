#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=tensorflow-enable-op-determinism@v1.0 defects=1}
def tensorflow_enable_op_determinism_noncompliant():
    import tensorflow as tf
    # Noncompliant: seed is not set and doesn't use enable_op_determinism().
    data = tf.ones((1, 1))
    layer = tf.keras.layers.Input(shape=[1])
    model = tf.keras.models.Model(inputs=layer, outputs=layer)
    model.compile(loss="categorical_crossentropy", metrics="AUC")
    model.fit(x=data, y=data)

# {/fact}


# {fact rule=tensorflow-enable-op-determinism@v1.0 defects=0}
def tensorflow_enable_op_determinism_compliant():
    import tensorflow as tf
    # Compliant: sets the seed and enable_op_determinism() is used.
    tf.keras.utils.set_random_seed(1)
    tf.config.experimental.enable_op_determinism()
    data = tf.ones((1, 1))
    layer = tf.keras.layers.Input(shape=[1])
    model = tf.keras.models.Model(inputs=layer, outputs=layer)
    model.compile(loss="categorical_crossentropy", metrics="AUC")
    model.fit(x=data, y=data)
# {/fact}
