#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=socket-close-platform-compatibility@v1.0 defects=1}
def create_socket_noncompliant(samplehost, sampleport, samplebuffersize):
    import socket
    socket.socket.settimeout(10.0)
    socket = socket.socket()
    socket.connect((samplehost, sampleport))
    print(socket.recv(samplebuffersize))
    # Noncompliant: socket.shutdown is not called before closing the socket.
    socket.close()
# {/fact}


# {fact rule=socket-close-platform-compatibility@v1.0 defects=0}
def create_socket_compliant(samplehost, sampleport, samplebuffersize):
    import socket
    socket.socket.settimeout(10.0)
    socket = socket.socket()
    socket.connect((samplehost, sampleport))
    try:
        print(socket.recv(samplebuffersize))
    finally:
        # Compliant: socket.shutdown is called before closing the socket.
        socket.shutdown(socket.SHUT_WR)
        socket.close()
# {/fact}
