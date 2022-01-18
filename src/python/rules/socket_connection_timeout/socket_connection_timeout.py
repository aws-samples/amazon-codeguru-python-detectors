#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=socket-connection-timeout@v1.0 defects=1}
def create_socket_noncompliant(samplehost, sampleport, samplebuffersize):
    import socket
    # Noncompliant: socket timeout is not set.
    socket = socket.create_connection((samplehost, sampleport))
    try:
        print(socket.recv(samplebuffersize))
    finally:
        socket.close()
# {/fact}


# {fact rule=socket-connection-timeout@v1.0 defects=0}
def create_socket_compliant(samplehost, sampleport, samplebuffersize):
    import socket
    # Compliant: socket timeout is set.
    socket = socket.create_connection((samplehost, sampleport), timeout=10)
    try:
        print(socket.recv(samplebuffersize))
    finally:
        socket.close()
# {/fact}
