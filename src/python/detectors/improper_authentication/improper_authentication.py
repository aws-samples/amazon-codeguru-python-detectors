#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=improper-authentication@v1.0 defects=1}
def improper_authentication_noncompliant(token):
    import jwt
    # Noncompliant: The verify flag is set to false.
    jwt.decode(token, verify=False)
# {/fact}


# {fact rule=improper-authentication@v1.0 defects=0}
def improper_authentication_compliant(token):
    import jwt
    # Compliant: The verify flag is set to true.
    jwt.decode(token, verify=True)
# {/fact}
