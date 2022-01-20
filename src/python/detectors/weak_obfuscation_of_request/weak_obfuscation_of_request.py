#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=weak-obfuscation-of-request@v1.0 defects=1}
def http_request_noncompliant(username, password, url):
    import urllib3 as urllib3
    from base64 import b64encode
    userpass = "%s:%s" % (username, password)
    # Noncompliant: weak encoding used in HTTP Basic Authentication.
    authorization = b64encode(str.encode(userpass)).decode("utf-8")
    headers = {'Authorization': 'Basic %s' % authorization}
    urllib3.disable_warnings()
    http = urllib3.PoolManager()
    response = http.request('GET', url, headers=headers)
# {/fact}
