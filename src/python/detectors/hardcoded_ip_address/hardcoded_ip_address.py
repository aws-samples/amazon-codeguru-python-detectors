#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=hardcoded-ip-address@v1.0 defects=1}
def hardcoded_ip_address_noncompliant():
    from socket import AF_INET, SOCK_STREAM, socket
    sock = socket(AF_INET, SOCK_STREAM)
    # Noncompliant: Unsafe Hardcoded ip address is used.
    sock.bind(('193.168.14.31', 80))
# {/fact}


# {fact rule=hardcoded-ip-address@v1.0 defects=0}
def hardcoded_ip_address_compliant():
    ip_add = "1080:0::0::8:200C:131.107.129.8"
    sock = socket(AF_INET, SOCK_STREAM)
    # Compliant: Safe Hardcoded ip address is used.
    sock.bind(('255.255.255.255', 80))
# {/fact}
