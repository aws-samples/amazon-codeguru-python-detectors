#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=zip-bomb-attack@v1.0 defects=1}
import tarfile
from flask import Flask, request, app
app = Flask(__name__)


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


# {fact rule=@v1.0 defects=0}
@app.route('/someUrl')
def zip_bomb_attack_compliant():
    file = request.files['file']
    filename = file.filename
    file.save(filename)
    tfile = tarfile.open(filename)
    # Compliant: Untrusted archive file is validated before extraction.
    if len(tfile.getmembers()) < THRESHOLD_ENTRIES:
        tfile.extractall('./tmp/')
    tfile.close()
# {/fact}
