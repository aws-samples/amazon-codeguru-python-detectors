# {fact rule=insecure-cryptography@v1.0 defects=1}
def cryptography_non_compliant():
    from cryptography.hazmat.primitives import hashes, hmac
    import secrets
    # Noncompliant: keysize too small for this algorithm.
    key = secrets.token_bytes(12)
    hash_key = hmac.HMAC(key, hashes.SHA1())
# {/fact}


# {fact rule=insecure-cryptography@v1.0 defects=0}
def cryptography_compliant():
    from cryptography.hazmat.primitives import hashes, hmac
    import secrets
    # Compliant: keysize sufficient for this algorithm.
    key = secrets.token_bytes(48)
    hash_key = hmac.HMAC(key, algorithm=hashes.SHA512_224())
# {/fact}
