
#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=code-injection@v1.0 defects=1}
from flask import app


@app.route('/')
def execute_input_noncompliant():
    from flask import request
    module_version = request.args.get("module_version")
    # Noncompliant: executes unsanitized inputs.
    exec("import urllib%s as urllib" % module_version)
# {/fact}


# {fact rule=code-injection@v1.0 defects=0}
from flask import app


@app.route('/')
def execute_input_compliant():
    from flask import request
    module_version = request.args.get("module_version")
    # Compliant: executes sanitized inputs.
    exec("import urllib%d as urllib" % int(module_version))
# {/fact}
