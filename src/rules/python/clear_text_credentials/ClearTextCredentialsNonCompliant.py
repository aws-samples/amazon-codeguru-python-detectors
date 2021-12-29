# {fact rule=clear-text-credentials@v1.0 defects=1}
PASSWORD_HASHERS = [
        # Noncompliant: uses non-standard or insecure password hashers.
        "django.contrib.auth.hashers.MD5PasswordHasher",
        "django.contrib.auth.hashers.PBKDF2PasswordHasher"
    ]
# {/fact}
