#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=insecure-hashing@v1.0 defects=1}
def hashing_noncompliant():
    import hashlib
    from hashlib import pbkdf2_hmac
    # Noncompliant: insecure hashing algorithm used.
    derivedkey = hashlib.pbkdf2_hmac('sha224', password, salt, 100000)
    derivedkey.hex()
# {/fact}


# {fact rule=insecure-hashing@v1.0 defects=0}
def hashing_compliant():
    import hashlib
    from hashlib import pbkdf2_hmac
    # Compliant: secure hashing algorithm used.
    derivedkey = hashlib.pbkdf2_hmac('sha256', password, salt, 100000)
    derivedkey.hex()
# {/fact}
