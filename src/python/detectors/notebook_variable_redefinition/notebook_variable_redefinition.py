#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=notebook-variable-redefinition@v1.0 defects=1}
# —— Code Cell 1, Execution Count 1 —— #
import math
# —— Code Cell 2, Execution Count 2 —— #
x = int(input('x:'))
y = int(input('y:'))
# —— Code Cell 3, Execution Count 3 —— #
z = '5'
# —— Code Cell 4, Execution Count 4 —— #
z = math.sqrt(x**2 + y**2)
# —— Code Cell 5, Execution Count 5 —— #
# Noncompliant: variable `z` is assigned to different types of values in above
# cells 3 and 4. Then in cell 5, the value of `z` is used in a `print()` call.
print('z:', z)
# {/fact}


# {fact rule=notebook-variable-redefinition@v1.0 defects=0}
# —— Code Cell 1, Execution Count 1 —— #
import math
# —— Code Cell 2, Execution Count 2 —— #
x = int(input('x:'))
y = int(input('y:'))
# —— Code Cell 3, Execution Count 3 —— #
z = '5'
# —— Code Cell 4, Execution Count 4 —— #
# Compliant: Even though there are 2 different types assigned to variable `z`
# in two different cells, it is only used within one of the two cells.
z = math.sqrt(x**2 + y**2)
print('z:', z)
# {/fact}
