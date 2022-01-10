#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=unrestricted-file-upload@v1.0 defects=1}
from flask import app


@app.route('/', methods=['GET', 'POST'])
def file_upload_non_compliant():
    import os
    from flask import request
    upload_file = request.files['file']
    # Noncompliant: the uploaded file can have any extension.
    upload_file.save(os.path.join('/path/to/the/uploads',
                                  upload_file.filename))
# {/fact}


# {fact rule=unrestricted-file-upload@v1.0 defects=0}
from flask import app


@app.route('/', methods=['GET', 'POST'])
def file_upload_compliant():
    import os
    from flask import request
    extensions = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
    upload_file = request.files['file']
    # Compliant: the uploaded file must have one of the allowed extensions.
    if '.' in upload_file.filename and \
            upload_file.filename.split('.')[-1] in extensions:
        upload_file.save(os.path.join('/path/to/the/uploads',
                                      upload_file.filename))
# {/fact}
