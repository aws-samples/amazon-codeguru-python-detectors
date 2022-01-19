#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=not-recommended-apis@v1.0 defects=1}
import xml.sax


class ContentHandler(xml.sax.ContentHandler):
    def __init__(self):
        xml.sax.ContentHandler.__init__(self)

    def start_element(self, name, attributes):
        print('start:', name)

    def end_element(self, name):
        print('end:', name)

    def characters(self, characters):
        print('characters:', characters)


def recommended_apis_noncompliant():
    xml_string = "<body>XML_STRING</body>"

    # Noncompliant: uses xml.sax which is an unrecommended API.
    xml.sax.parseString(xml_string, ContentHandler())


if __name__ == "__main__":
    recommended_apis_noncompliant()
# {/fact}
