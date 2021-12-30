# {fact rule=pep8-recommendations@v1.0 defects=1}
def readable_non_compliant():
    # Noncompliant: violates PEP8 programming recommendations,
    # making it difficult to read.
    if not a is None:
        print(a)
# {/fact}


# {fact rule=pep8-recommendations@v1.0 defects=0}
def readable_compliant():
    # Compliant: follows the PEP8 programming recommendations,
    # improving readability.
    if a is not None:
        print(a)
# {/fact}
