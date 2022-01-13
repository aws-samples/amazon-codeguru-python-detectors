#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=os-command-injection@v1.0 defects=1}
def os_command_noncompliant():
    import os
    from flask import request
    # Noncompliant: address argument is not sanitized.
    address = request.args.get("address")
    cmd = "ping -c 1 %s" % address
    os.popen(cmd)
# {/fact}


# {fact rule=os-command-injection@v1.0 defects=0}
def os_command_compliant():
    import shlex
    import os
    from flask import request
    # Compliant: address argument is sanitized(shell-escaped).
    address = shlex.quote(request.args.get("address"))
    cmd = "ping -c 1 %s" % address
    os.popen(cmd)
# {/fact}
