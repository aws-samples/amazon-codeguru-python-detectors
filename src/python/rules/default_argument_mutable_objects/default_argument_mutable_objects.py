#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=default-argument-mutable-objects@v1.0 defects=1}
# Noncompliant: default arguments have mutable objects.
def with_complex_default_value_noncompliant(self, index=1, mydict={},
                                            mylist=[]):
    mydict[index] = mylist[index]
    return mydict
# {/fact}


# {fact rule=default-argument-mutable-objects@v1.0 defects=0}
# Compliant: default arguments are assigned to None or unmutable objects.
def with_unmutable_objects_compliant(mydict=None, number=1, str="hi",
                                     mytuple=(1, 2)):
    print(mydict, number, str, mytuple)
# {/fact}
