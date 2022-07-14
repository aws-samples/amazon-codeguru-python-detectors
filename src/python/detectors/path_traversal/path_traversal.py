#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=path-traversal@v1.0 defects=1}
def verify_file_path_noncompliant():
    from flask import request
    file_path = request.args["file"]
    # Noncompliant: user input file path is not sanitized.
    file = open(file_path)
    file.close()
# {/fact}


# {fact rule=path-traversal@v1.0 defects=0}
def verify_file_path_compliant():
    from flask import request
    file_path = request.args["file"]
    # Compliant: user input file path is sanitized.
    file_path = file_path.replace("..", "")
    file = open(file_path)
    file.close()
# {/fact}
