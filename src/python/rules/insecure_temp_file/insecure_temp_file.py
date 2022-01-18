#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=insecure-temp-file@v1.0 defects=1}
def create_file_noncompliant(results):
    import tempfile
    # Noncompliant: uses a temporary file path to create a temporary file.
    filename = tempfile.mktemp()
    with open(filename, "w+") as f:
        f.write(results)
    print("Results written to", filename)
# {/fact}


# {fact rule=insecure-temp-file@v1.0 defects=0}
def create_temp_file_compliant(results):
    import tempfile
    # Compliant: uses the correct mechanism to create a temporary file.
    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as f:
        f.write(results)
    print("Results written to", f.name)
# {/fact}
