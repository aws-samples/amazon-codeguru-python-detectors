#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

def __CELL_EDGE__(x):
    pass


# {fact rule=notebook-best-practice-violation@v1.0 defects=1}
# Noncompliant: cell is blank.
__CELL_EDGE__(0)

__CELL_EDGE__(1)
x = 12
__CELL_EDGE__(2)
y = 13
__CELL_EDGE__(3)
sum = x + y
__CELL_EDGE__(4)
print('End of program')
# {/fact}
