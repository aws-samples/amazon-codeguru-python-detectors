#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

from flask import Flask, jsonify
from werkzeug.exceptions import HTTPException
import traceback

app_flask = Flask(__name__)


# {fact rule=stack-trace-exposure@v1.0 defects=1}
@app_flask.route('/noncompliant/<text>')
def stack_trace_exposure_noncompliant(text):
    try:
        if text == 'error':
            raise HTTPException
        return jsonify({'data': 'some_data'}), 200
    except HTTPException:
        # Noncompliant: Stack trace is returned from api call.
        return traceback.format_exc()
# {/fact}


# {fact rule=stack-trace-exposure@v1.0 defects=0}
@app_flask.route('/compliant/<text>')
def stack_trace_exposure_compliant(text):
    try:
        if text == 'error':
            raise HTTPException
        return jsonify({'data': 'some_data'}), 200
    except HTTPException:
        # Compliant: Custom json response with message as cause of error.
        return jsonify({'message': 'Internal error occurred!'}), 404
# {/fact}
