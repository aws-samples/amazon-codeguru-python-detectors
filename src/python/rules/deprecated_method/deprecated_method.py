#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=deprecated-method@v1.0 defects=1}
def deprecated_method_noncompliant(url):
    import botocore.vendored.requests as requests
    # Noncompliant: uses the deprecated botocore vendored method.
    return requests.get(url)
# {/fact}


# {fact rule=deprecated-method@v1.0 defects=0}
def deprecated_method_compliant(url, sigv4auth):
    import requests
    # Compliant: avoids using the deprecated methods.
    return requests.get(url, auth=sigv4auth).text
# {/fact}
