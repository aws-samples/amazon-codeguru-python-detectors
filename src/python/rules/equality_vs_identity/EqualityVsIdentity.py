# {fact rule=equality-vs-identity@v1.0 defects=1}
def notequals_operator_non_compliant():
    phrase = "Thisisstring"
    # Noncompliant: uses checks for equality instead of identity.
    if phrase != None:
        print(True)
# {/fact}


# {fact rule=equality-vs-identity@v1.0 defects=0}
def isnot_operator_compliant():
    phrase = "Thisisstring"
    # Compliant: uses the correct mechanism for checking the identity.
    if phrase is not None:
        print(True)
# {/fact}
