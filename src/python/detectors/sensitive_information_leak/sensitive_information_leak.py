#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=sensitive-information-leak@v1.0 defects=1}
def sensitive_information_leak_noncompliant():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Noncompliant: Empty IP Address is passed when binding to a socket.
    s.bind(('', 0))
# {/fact}


# {fact rule=sensitive-information-leak@v1.0 defects=0}
def sensitive_information_leak_compliant():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Compliant: Non-empty IP Address is passed when binding to a socket.
    s.bind(('192.168.1.1', 0))
# {/fact}
