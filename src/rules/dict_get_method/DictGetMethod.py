# {fact rule=dict-get-method@v1.0 defects=1}
def keyerror_non_compliant():
    mydict = {1: 1, 2: 2, 3: 3}
    key = 5
    try:
        # Noncompliant: uses [] and exceptions.
        count = mydict[key]
    except KeyError:
        count = 0
    return count
# {/fact}


# {fact rule=dict-get-method@v1.0 defects=0}
def keyerror_compliant():
    mydict = {1: 1, 2: 2, 3: 3}
    key = 5
    # Compliant: use get() with a default value.
    return mydict.get(key, 0)
# {/fact}
