#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=detect-activated-debug-feature@v1.0 defects=1}
def detect_activated_debug_feature_noncompliant():
    from django.conf import settings
    # Noncompliant: The debug feature is enabled.
    settings.configure(DEBUG=True)
# {/fact}


# {fact rule=detect-activated-debug-feature@v1.0 defects=0}
def detect_activated_debug_feature_compliant():
    from django.conf import settings
    import os
    # Compliant: The debug feature is set through the environment variable.
    settings.configure(DEBUG=os.environ['DEBUG'])
# {/fact}
