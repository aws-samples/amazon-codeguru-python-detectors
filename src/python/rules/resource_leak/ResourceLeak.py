# {fact rule=resource-leak@v1.0 defects=1}
from flask import app


@app.route('/upload')
def flask_non_compliant():
    from flask import request
    import re

    username = request.args.get('username')
    filename = request.files.get('attachment').filename

    # Noncompliant: constructs regular expression from user input
    # without sanitization.
    re.search(username, filename)
# {/fact}


# {fact rule=resource-leak@v1.0 defects=0}
from flask import app


@app.route('/upload')
def flask_compliant():
    from flask import request
    import re

    username = re.escape(request.args.get('username'))
    filename = request.files.get('attachment').filename

    # Compliant: user input is sanitized before constructing
    # a regular expression.
    re.search(username, filename)
# {/fact}
