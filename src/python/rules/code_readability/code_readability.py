#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=code-readability@v1.0 defects=1}
def avoid_complex_comprehension_noncompliant():
    text = [['bar', 'pie', 'line'],
            ['Rome', 'Madrid', 'Houston'],
            ['aa', 'bb', 'cc', 'dd']]
    # Noncompliant: list comprehensions with more than two control
    # sub expressions are hard to read and maintain.
    text_3 = [y.upper() for x in text if len(x) == 3 for y in x
              if y.startswith('f')]
# {/fact}


# {fact rule=code-readability@v1.0 defects=0}
def avoid_complex_comprehension_compliant():
    text = [['bar', 'pie', 'line'],
            ['Rome', 'Madrid', 'Houston'],
            ['aa', 'bb', 'cc', 'dd']]
    text_1 = []
    # Compliant: easy to read and maintain.
    for x in text:
        if len(x) > 3:
            for y in x:
                text_1.append(y)
# {/fact}
