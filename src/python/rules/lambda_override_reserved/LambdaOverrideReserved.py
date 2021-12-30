# {fact rule=lambda-override-reserved@v1.0 defects=1}
def create_variable_non_compliant():
    import os
    # Noncompliant: overrides reserved environment variable names
    # in a Lambda function.
    os.environ['_HANDLER'] = "value"
# {/fact}


# {fact rule=lambda-override-reserved@v1.0 defects=0}
def create_variable_compliant():
    import os
    # Compliant: prevents overriding reserved environment variable names
    # in a Lambda function.
    os.environ['SOME_ENV_VAR'] = "value"
# {/fact}
