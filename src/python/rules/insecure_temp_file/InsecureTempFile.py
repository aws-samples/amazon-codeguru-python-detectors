# {fact rule=insecure-temp-file@v1.0 defects=1}
def create_file_non_compliant(results):
    import tempfile
    filename = tempfile.mktemp()
    # Noncompliant: uses a temporary file path to create a temporary file.
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
