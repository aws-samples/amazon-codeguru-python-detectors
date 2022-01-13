#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=string-concatenation@v1.0 defects=1}
def string_concatenation_noncompliant():
    samplelist = ['sampleString1', 'sampleString2', 'sampleString3']
    concatenatedstring = ''
    for item in samplelist:
        # Noncompliant: inefficient string concatenation inside a loop is used.
        concatenatedstring += item + "\n"
    return concatenatedstring
# {/fact}


# {fact rule=string-concatenation@v1.0 defects=0}
def string_concatenation_compliant():
    samplelist = ['sampleString1', 'sampleString2', 'sampleString3']
    concatenatedlist = []
    for item in samplelist:
        concatenatedlist.append(item)
        concatenatedlist.append("\n")
    # Compliant: join function is used for string concatenation
    concatenatedstring = ''.join(concatenatedlist)
    return concatenatedstring
# {/fact}
