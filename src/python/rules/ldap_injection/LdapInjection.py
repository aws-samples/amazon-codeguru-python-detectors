# {fact rule=ldap-injection@v1.0 defects=1}
from flask import app


@app.route('/getUsers')
def get_users_non_compliant():
    import ldap
    from flask import request
    username = request.args['username']
    # Noncompliant: user-supplied filter is not sanitized.
    filter_string = '(uid=' + username + ')'
    ldap_conn = ldap.initialize('ldaps://ldap.amazon.com:636')
    result = ldap_conn.search_s('o=amazon.com',
                                ldap.SCOPE_SUBTREE,
                                filter_string)
    return result
# {/fact}


# {fact rule=ldap-injection@v1.0 defects=0}
from flask import app


@app.route('/getUsers')
def get_users_compliant(request):
    import ldap
    from flask import request
    username = request.args['username']
    # Compliant: user-supplied filter is checked for allowed characters.
    filter_string = "(uid=%s)" % ('username')
    ldap_conn = ldap.initialize('ldaps://ldap.amazon.com:636')
    result = ldap_conn.search('o=amazon.com',
                              ldap.SCOPE_SUBTREE,
                              filter_string)
    return result
# {/fact}
