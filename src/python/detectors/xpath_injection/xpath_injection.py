#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=xpath-injection@v1.0 defects=1}
from flask import request, app


@app.route('/user')
def find_users_noncompliant():
    from flask import request
    import xml.etree.ElementTree as ET
    tree = ET.parse('users.xml')
    root = tree.getroot()
    username = request.args['username']
    query = "./users/user/[@name='"+username+"']/location"
    # Noncompliant: evaluating expression built from user-supplied parameter
    # can lead to XPath injection.
    elements = root.findall(query)
    return 'Location %s' % list(elements)
# {/fact}


# {fact rule=xpath-injection@v1.0 defects=0}
from flask import request, app


@app.route('/user')
def find_users_compliant():
    from flask import request
    from lxml import etree
    # Compliant: disabling external entities prevents XPath injection.
    parser = etree.XMLParser(resolve_entities=False)
    tree = etree.parse('users.xml', parser)
    root = tree.getroot()
    username = request.args['username']
    query = "/collection/users/user[@name = $parameter_name]/location/text()"
    elements = root.xpath(query, parameter_name=username)
    return 'Location %s' % list(elements)
# {/fact}
