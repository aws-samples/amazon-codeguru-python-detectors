#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=improper-certificate-validation@v1.0 defects=1}
def create_connection_noncompliant():
    import socket
    import ssl
    host, port = 'example.com', 443
    with socket.socket(socket.AF_INET) as sock:
        context = ssl.SSLContext()
        # Noncompliant: security certificate validation disabled.
        context.verify_mode = ssl.CERT_NONE
        conn = context.wrap_socket(sock, server_hostname=host)
        try:
            conn.connect((host, port))
            handle(conn)
        finally:
            conn.close()
# {/fact}


# {fact rule=improper-certificate-validation@v1.0 defects=0}
def create_connection_compliant():
    import socket
    import ssl
    host, port = 'example.com', 443
    with socket.socket(socket.AF_INET) as sock:
        context = ssl.SSLContext()
        # Compliant: security certificate validation enabled.
        context.verify_mode = ssl.CERT_REQUIRED
        conn = context.wrap_socket(sock, server_hostname=host)
        try:
            conn.connect((host, port))
            handle(conn)
        finally:
            conn.close()
# {/fact}
