# {fact rule=iterating-sequence-modification@v1.0 defects=1}
def modifying_list_non_compliant():
    words = ['cat', 'window', 'defenestrate']
    # Noncompliant: modifies the same list while iterating over it.
    for word in words:
        if len(word) > 6:
            words.insert(0, word)
# {/fact}


# {fact rule=iterating-sequence-modification@v1.0 defects=0}
def modifying_list_splice_compliant():
    words = ['cat', 'window', 'defenestrate']
    # Compliant: creates new list using splicing, hence loops iterate on one
    # list, modifying a different list.
    for word in words[:]:
        if len(word) > 6:
            words.insert(0, word)
# {/fact}
