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
    base_path = "/var/data/images/"
    file_path = request.args["file"]
    allowed_path = ["example_path1", "example_path2"]
    # Compliant: user input file path is sanitized.
    if file_path in allowed_path:
        file = open(base_path + file_path)
        file.close()
# {/fact}
