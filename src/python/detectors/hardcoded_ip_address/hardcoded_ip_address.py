#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

from socket import AF_INET, SOCK_STREAM, socket


# {fact rule=hardcoded-ip-address@v1.0 defects=1}
def hardcoded_ip_address_noncompliant():
    sock = socket(AF_INET, SOCK_STREAM)
    # Noncompliant: IP address is hardcoded.
    sock.bind(('193.168.14.31', 80))
# {/fact}


# {fact rule=hardcoded-ip-address@v1.0 defects=0}
def hardcoded_ip_address_compliant(ip_add=None):
    sock = socket(AF_INET, SOCK_STREAM)
    # Compliant: IP address is not hardcoded.
    sock.bind((ip_add, 5080))
# {/fact}
