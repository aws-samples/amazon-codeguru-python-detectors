# {fact rule=improper-error-handling@v1.0 defects=1}
def error_handling_pass_non_compliant():
    number = input("Enter number:\n")
    try:
        int(number)
    except Exception:
        # Noncompliant: has improper error handling.
        pass
# {/fact}


# {fact rule=improper-error-handling@v1.0 defects=1}
def error_handling_continue_non_compliant():
    number = input("Enter number:\n")
    try:
        int(number)
    except Exception:
        # Noncompliant: has improper error handling.
        continue
# {/fact}


# {fact rule=improper-error-handling@v1.0 defects=0}
def error_handling_compliant():
    number = input("Enter number:\n")
    try:
        int(number)
    except ValueError:
        # Compliant: has proper error handling.
        print(number, "is not an integer.")
# {/fact}
