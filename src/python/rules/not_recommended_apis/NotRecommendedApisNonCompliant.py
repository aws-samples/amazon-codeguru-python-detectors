# {publish rule=not-recommended-apis@v1.0 defects=1}
import xml.sax
from xml import sax


class ContentHandler(xml.sax.ContentHandler):
    def __init__(self):
        xml.sax.ContentHandler.__init__(self)

    def start_element(self, name, attributes):
        print('start:', name)

    def end_element(self, name):
        print('end:', name)

    def characters(self, characters):
        print('characters:', characters)


def recommended_apis_non_compliant():
    xml_string = "<body>XML_STRING</body>"

    # Noncompliant: uses xml.sax which is an unrecommended API.
    xml.sax.parseString(xml_string, ContentHandler())
    xml.sax.parse('example.xml', ContentHandler())
    sax.parseString(xml_string, ContentHandler())
    sax.parse('example.xml', ContentHandler)


if __name__ == "__main__":
    recommended_apis_non_compliant()
# {/publish}
