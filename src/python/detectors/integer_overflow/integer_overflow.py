#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

import numpy as np
# {fact rule=integer-overflow@v1.0 defects=1}


def integer_overflow_noncompliant():
    # Noncompliant: Number larger than limit of the datatype is stored.
    arr = np.array([[100000000]], dtype=np.int8)
# {/fact}


# {fact rule=integer-overflow@v1.0 defects=0}
def integer_overflow_compliant(self, request_items):
    # Compliant: Number stored is within the limits of the specified datatype.
    arr = np.array([100000000], dtype=np.int32)
# {/fact}
