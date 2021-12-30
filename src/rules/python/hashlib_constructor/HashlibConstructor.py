# {fact rule=hashlib-constructor@v1.0 defects=1}
def constructor_non_compliant():
    import hashlib

    text = "AWSGuruRules"

    # Noncompliant: uses the new() constructor instead of the hashlib
    # constructor, which is slower.
    result = hashlib.new('sha256', text.encode())

    print("The hexadecimal equivalent of SHA256 is : ")
    print(result.hexdigest())
# {/fact}


# {fact rule=hashlib-constructor@v1.0 defects=0}
def constructor_non_compliant():
    import hashlib

    text = "AWSGuruRules"

    # Compliant: uses the hashlib constructor over the new(), which is faster.
    result = hashlib.sha256(text.encode())

    print("The hexadecimal equivalent of SHA256 is : ")
    print(result.hexdigest())
# {/fact}
