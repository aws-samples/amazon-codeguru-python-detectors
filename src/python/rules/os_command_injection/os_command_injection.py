#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=os-command-injection@v1.0 defects=1}
def exec_command_noncompliant():
    from paramiko import client
    from flask import request
    address = request.args.get("address")
    cmd = "ping -c 1 %s" % address
    client = client.SSHClient()
    client.connect("ssh.samplehost.com")
    # Noncompliant: address argument is not sanitized.
    client.exec_command(cmd)
# {/fact}


# {fact rule=os-command-injection@v1.0 defects=0}
def exec_command_compliant():
    from paramiko import client
    from flask import request
    address = request.args.get("address")
    # Compliant: address argument is sanitized (shell-escaped).
    address = shlex.quote(request.args.get("address"))
    cmd = "ping -c 1 %s" % address
    client = client.SSHClient()
    client.connect("ssh.samplehost.com")
    client.exec_command(cmd)
# {/fact}
