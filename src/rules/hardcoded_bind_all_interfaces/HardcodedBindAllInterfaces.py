# {fact rule=hardcoded-bind-all-interfaces@v1.0 defects=1}
def bind_socket_non_compliant():
    import socket

    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Noncompliant: binds socket to all interfaces.
    my_socket.bind(('0.0.0.0', 8080))
# {/fact}


# {fact rule=hardcoded-bind-all-interfaces@v1.0 defects=0}
def bind_socket_compliant():
    import socket

    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Compliant: binds socket to specific interfaces only.
    my_socket.bind(('192.168.55.77', 8080))
    my_socket.bind(('192.168.12.34', 8080))
# {/fact}
