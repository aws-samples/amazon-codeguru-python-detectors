#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=notebook-invalid-execution-order@v1.0 defects=0}
# Compliant: execution order of cells is linear.
# —— Code Cell 1, Execution Count 1 —— #
x = 12
y = 13
# —— Code Cell 2, Execution Count 2 —— #
sum = x + y
product = x * y
exp = x ** y
# —— Code Cell 3, Execution Count 3 —— #
print(sum, product, exp)
# {/fact}
