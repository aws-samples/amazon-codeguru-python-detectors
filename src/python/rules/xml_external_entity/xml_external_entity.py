#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=xml-external-entity@v1.0 defects=1}
def xml_parse_noncompliant():
    from lxml import etree
    # Noncompliant: resolve_entities is not disabled
    # and is set to true by default.
    parser = etree.XMLParser()
    tree1 = etree.parse('resources/xxe.xml', parser)
# {/fact}


# {fact rule=xml-external-entity@v1.0 defects=0}
def xml_parse_compliant():
    from lxml import etree
    # Compliant: resolve_entities is disabled.
    parser = etree.XMLParser(resolve_entities=False)
    tree1 = etree.parse('resources/xxe.xml', parser)
# {/fact}
