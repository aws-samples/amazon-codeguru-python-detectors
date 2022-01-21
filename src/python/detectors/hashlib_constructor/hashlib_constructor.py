#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=hashlib-constructor@v1.0 defects=1}
def constructor_noncompliant():
    import hashlib

    text = "ExampleString"

    # Noncompliant: uses the new() constructor instead of the hashlib
    # constructor, which is slower.
    result = hashlib.new('sha256', text.encode())

    print("The hexadecimal equivalent of SHA256 is : ")
    print(result.hexdigest())
# {/fact}


# {fact rule=hashlib-constructor@v1.0 defects=0}
def constructor_compliant():
    import hashlib

    text = "ExampleString"

    # Compliant: uses the hashlib constructor over the new(), which is faster.
    result = hashlib.sha256(text.encode())

    print("The hexadecimal equivalent of SHA256 is : ")
    print(result.hexdigest())
# {/fact}
