#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

import jsonpickle
from flask import Flask, request, app
app = Flask(__name__)


# {fact rule=untrusted-deserialization@v1.0 defects=1}
@app.route('/someUrl')
def untrusted_deserialization_noncompliant():
    userobj = request.POST.get("user")
    # Noncompliant: Untrusted object deserialized without validation.
    obj = jsonpickle.decode(jsonify(userObj))
    return obj
# {/fact}


# {fact rule=untrusted-deserialization@v1.0 defects=0}
@app.route('/someUrl')
def untrusted_deserialization_compliant():
    userobj = request.POST.get("user")
    # Compliant: Untrusted object is validated before deserialization.
    if validate(userObj):
        obj = jsonpickle.decode(jsonify(userObj))
        return obj
# {/fact}
