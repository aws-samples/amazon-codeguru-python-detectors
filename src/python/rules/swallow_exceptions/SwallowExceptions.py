# {fact rule=swallow-exceptions@v1.0 defects=1}
def swallow_non_compliant():
    for i in range(10):
        try:
            raise ValueError()
        finally:
            # Noncompliant: uses continue or break or return statements
            # in finally block.
            continue
# {/fact}


# {fact rule=swallow-exceptions@v1.0 defects=0}
def swallow_compliant():
    for i in range(10):
        try:
            raise ValueError()
        finally:
            # Compliant: avoids using continue or break or return statements
            # in finally block.
            print("Done with iterations")
# {/fact}
