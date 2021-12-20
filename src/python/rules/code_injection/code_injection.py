import flask

{fact rule=code-injection@v1.0 defects=1}
@app.route('/')
def non_conformant1(urllib_version):
    # Noncompliant: evaluates unsanitized code.
    exec("import urllib%s as urllib" % urllib_version)
{/fact}

{fact rule=code-injection@v1.0 defects=0}
@app.route('/')
def conformant1():
    from flask import request
    module = request.args.get("urllib_version")
    # Compliant: only evaluates sanitized code.
    exec("import urllib%d as urllib" % int(urllib_version))
{/fact}
