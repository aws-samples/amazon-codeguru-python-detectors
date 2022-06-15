#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=untrusted-deserialization@v1.0 defects=1}
def untrusted_deserialization_noncompliant():
    import jsonpickle
    userobj = input("user")
    # Noncompliant: Untrusted object deserialized without validation.
    obj = jsonpickle.decode(userobj)
    return obj
# {/fact}


# {fact rule=untrusted-deserialization@v1.0 defects=0}
def untrusted_deserialization_compliant():
    import jsonpickle
    userobj = input("user")
    allowed_user_obj = ['example_module1', 'example_module2']
    # Compliant: Untrusted object is validated before deserialization.
    if userobj in allowed_user_obj:
        obj = jsonpickle.decode(userobj)
        return obj
# {/fact}
