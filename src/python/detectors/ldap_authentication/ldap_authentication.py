#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=ldap-authentication@v1.0 defects=1}
def authenticate_connection_noncompliant():
    import ldap
    import os
    connect = ldap.initialize('ldap://127.0.0.1:1389')
    connect.set_option(ldap.OPT_REFERRALS, 0)
    # Noncompliant: authentication disabled.
    connect.simple_bind('cn=root')
# {/fact}


# {fact rule=ldap-authentication@v1.0 defects=0}
def authenticate_connection_compliant():
    import ldap
    import os
    connect = ldap.initialize('ldap://127.0.0.1:1389')
    connect.set_option(ldap.OPT_REFERRALS, 0)
    # Compliant: simple security authentication used.
    connect.simple_bind('cn=root', os.environ.get('LDAP_PASSWORD'))
# {/fact}
