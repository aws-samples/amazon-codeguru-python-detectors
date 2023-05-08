#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=tensorflow-avoid-using-nondeterministic-api@v1.0 defects=1}
def tensorflow_avoid_using_nondeterministic_api_noncompliant():
    import tensorflow as tf
    data = tf.ones((1, 1))
    # Noncompliant: Determinism of tf.compat.v1.Session
    # can not be guaranteed in TF2.
    tf.config.experimental.enable_op_determinism()
    tf.compat.v1.Session(
        target='', graph=None, config=None
    )
    layer = tf.keras.layers.Input(shape=[1])
    model = tf.keras.models.Model(inputs=layer, outputs=layer)
    model.compile(loss="categorical_crossentropy", metrics="AUC")
    model.fit(x=data, y=data)
# {/fact}


# {fact rule=tensorflow-avoid-using-nondeterministic-api@v1.0 defects=0}
def tensorflow_avoid_using_nondeterministic_api_compliant():
    import tensorflow as tf
    tf.random.set_seed(0)
    # Compliant: uses deterministic API.
    tf.config.experimental.enable_op_determinism()
    data = tf.ones((1, 1))
    layer = tf.keras.layers.Input(shape=[1])
    model = tf.keras.models.Model(inputs=layer, outputs=layer)
    model.compile(loss="categorical_crossentropy", metrics="AUC")
    model.fit(x=data, y=data)
# {/fact}
