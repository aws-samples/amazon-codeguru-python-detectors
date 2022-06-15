#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=do-not-auto-add-or-warning-missing-hostkey-policy@v1.0 defects=1}
def do_not_auto_add_or_warning_missing_hostkey_policy_noncompliant():
    from paramiko import AutoAddPolicy
    from paramiko.client import SSHClient
    ssh_client = SSHClient()
    # Noncompliant: Insecure `AutoAddPolicy` is used as missing hostkey policy.
    ssh_client.set_missing_host_key_policy(policy=AutoAddPolicy)
# {/fact}


# {fact rule=do-not-auto-add-or-warning-missing-hostkey-policy@v1.0 defects=0}
def do_not_auto_add_or_warning_missing_hostkey_policy_compliant():
    from paramiko import RejectPolicy
    from paramiko.client import SSHClient
    ssh_client = SSHClient()
    # Compliant: Secure `RejectPolicy` is used as missing hostkey policy.
    ssh_client.set_missing_host_key_policy(RejectPolicy)
# {/fact}
