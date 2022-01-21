#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=insecure-cookie@v1.0 defects=1}
def secure_cookie_noncompliant():
    from http.cookies import SimpleCookie
    cookie = SimpleCookie()
    cookie['sample'] = "sample_value"
    # Noncompliant: the cookie is insecure.
    cookie['sample']['secure'] = 0
    print(cookie)
# {/fact}


# {fact rule=insecure-cookie@v1.0 defects=0}
def secure_cookie_compliant():
    from http.cookies import SimpleCookie
    cookie = SimpleCookie()
    cookie['sample'] = "sample_value"
    # Compliant: the cookie is secure.
    cookie['sample']['secure'] = True  # compliant
    print(cookie)
# {/fact}
