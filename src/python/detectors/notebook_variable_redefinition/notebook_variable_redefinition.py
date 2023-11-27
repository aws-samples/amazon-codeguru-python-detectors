#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=notebook-variable-redefinition@v1.0 defects=1}
# —— Code Cell 1 —— #
import math
# —— Code Cell 2 —— #
x = int(input('x:'))
y = int(input('y:'))
# —— Code Cell 3 —— #
z = '5'
# —— Code Cell 4 —— #
z = math.sqrt(x**2 + y**2)
# —— Code Cell 5 —— #
# Noncompliant: variable `z` is assigned to different types of values in above
# cells 3 and 4. Then in cell 5, the value of `z` is used in a `print()` call,
# which can have different result depending on the execution order of cells.
print('z:', z)
# {/fact}


# {fact rule=notebook-variable-redefinition@v1.0 defects=0}
# —— Code Cell 1 —— #
import math
# —— Code Cell 2 —— #
x = int(input('x:'))
y = int(input('y:'))
# —— Code Cell 3 —— #
z = '5'
# —— Code Cell 4 —— #
# Compliant: Even though there are 2 different types assigned to variable `z`
# in two different cells, it is only used within one of the two cells.
z = math.sqrt(x**2 + y**2)
print('z:', z)
# {/fact}
