# {fact rule=public-method-parameter-validation@v1.0 defects=1}
def login_non_compliant(username, password):
    # Noncompliant: not all public method parameters are validated for
    # nullness,unexpected values, and malicious values.
    if password is not None and len(password) >=8:
        login(username, password)
# {/fact}


# {fact rule=public-method-parameter-validation@v1.0 defects=0}
def login_compliant(username, password):
    import re
    regex = r'^[a-z0-9]+[\\._]?[a-z0-9]+[@]\\w+[.]\\w{2,3}$'
    # Compliant: all the public method parameters are validated for nullness,
    # unexpected values, and malicious values.
    if username is not None and password is not None \
            and username.isalnum() and len(passoword) >=8 \
            and re.search(regex, username):
        login(username, password)
# {/fact}: