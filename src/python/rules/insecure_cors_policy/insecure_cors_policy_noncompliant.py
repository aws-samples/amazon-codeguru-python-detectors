#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=insecure-cors-policy@v1.0 defects=1}
from flask import app, request
from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
# Noncompliant: the send_wildcard is set to allow any domain.
CORS(app, send_wildcard=True)
# {/fact}
