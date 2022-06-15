#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

import tarfile
from flask import Flask, request
app = Flask(__name__)


# {fact rule=zip-bomb-attack@v1.0 defects=1}
@app.route('/someUrl')
def zip_bomb_attack_noncompliant():
    file = request.files['file']
    filename = file.filename
    file.save(filename)
    tfile = tarfile.open(filename)
    # Noncompliant: Untrusted archive file extracted without any validation.
    tfile.extractall('./tmp/')
    tfile.close()
# {/fact}


# {fact rule=zip-bomb-attack@v1.0 defects=0}
@app.route('/someUrl')
def zip_bomb_attack_compliant():
    file = request.files['file']
    filename = file.filename
    file.save(filename)
    tfile = tarfile.open(filename)
    threshold_entries = 100  # some threshold value
    # Compliant: Untrusted archive file is validated before extraction.
    if len(tfile.getmembers()) < threshold_entries:
        tfile.extractall('./tmp/')
    tfile.close()
# {/fact}
