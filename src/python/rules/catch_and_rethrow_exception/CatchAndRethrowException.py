# {fact rule=catch-and-rethrow-exception@v1.0 defects=1}
def nested_non_compliant():
    try:
        try_something()
    except KeyError as e:
        try:
            catch_and_try_something()
        # Noncompliant: unnecessary `except` clause.
        except ValueError:
            raise
        raise e
# {/fact}


# {fact rule=catch-and-rethrow-exception@v1.0 defects=0}
def nested_compliant():
    try:
        try_something()
    except KeyError as e:
        try:
            catch_and_try_something()
        except ValueError:
            # Compliant: operation in `except` clause.
            rethrow_exception_something()
            raise
        raise e
# {/fact}
