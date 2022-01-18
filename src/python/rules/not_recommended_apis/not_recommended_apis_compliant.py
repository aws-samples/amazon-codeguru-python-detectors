#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=not-recommended-apis@v1.0 defects=0}
import xml
import defusedxml.sax


class ContentHandler(xml.sax.ContentHandler):
    def __init__(self):
        xml.sax.ContentHandler.__init__(self)

    def start_element(self, name, attributes):
        print('start:', name)

    def end_element(self, name):
        print('end:', name)

    def characters(self, characters):
        print('characters:', characters)


def not_recommended_apis_compliant():
    xml_string = "<body>XML_STRING</body>"

    # Compliant: avoids using unrecommended APIs.
    defusedxml.sax.parseString(xml_string, ContentHandler())


if __name__ == "__main__":
    not_recommended_apis_compliant()
# {/fact}
