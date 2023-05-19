#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=notebook-best-practice-violation@v1.0 defects=1}
# —— Code Cell 1, Execution Count 1 —— #
import numpy as np
# —— Code Cell 2, Execution Count 2 —— #
# Noncompliant: imports are not in the first code cell.
import pandas as pd
primary = pd.read_csv('attribute-primary-info.csv', sep='\t')
primary
# —— Code Cell 3, Execution Count 3 —— #
alias = pd.read_csv('attribute-alias-info-en_US.csv', sep='\t')
alias
# —— Code Cell 4, Execution Count 4 —— #
# Noncompliant: blank cells.
# —— Code Cell 5, Execution Count 5 —— #

# —— Code Cell 6, Execution Count 6 —— #

# —— Code Cell 7, Execution Count 7 —— #

# —— Code Cell 8, Execution Count 8 —— #

# —— Code Cell 9, Execution Count 9 —— #
print('Hello World!')
# —— Code Cell 10, Execution Count 10 —— #
print('Hello World!')
# —— Code Cell 11, Execution Count 11 —— #
print('Hello World!')
# —— Code Cell 12, Execution Count 12 —— #
print('Hello World!')
# —— Code Cell 13, Execution Count 13 —— #
print('Hello World!')
# —— Code Cell 14, Execution Count 14 —— #
print('Hello World!')
# —— Code Cell 15, Execution Count 15 —— #
print('Hello World!')
# —— Code Cell 16, Execution Count 16 —— #
print('Hello World!')
# —— Code Cell 17, Execution Count 17 —— #
print('Hello World!')
# —— Code Cell 18, Execution Count 18 —— #
print('Hello World!')
# —— Code Cell 19, Execution Count 19 —— #
print('Hello World!')
# —— Code Cell 20, Execution Count 20 —— #
print('Hello World!')
# —— Code Cell 21, Execution Count 21 —— #
print('Hello World!')
# —— Code Cell 22, Execution Count 22 —— #
print('Hello World!')
# —— Code Cell 23, Execution Count 23 —— #
print('Hello World!')
# —— Code Cell 24, Execution Count 24 —— #
print('Hello World!')
# —— Code Cell 25, Execution Count 25 —— #
print('Hello World!')
# —— Code Cell 26, Execution Count 26 —— #
print('Hello World!')
# —— Code Cell 27, Execution Count 27 —— #
# Noncompliant: too many code cells.
print('Hello World!')
# —— Code Cell 28, Execution Count 28 —— #
# —— Code Cell 29, Execution Count 29 —— #
# —— Code Cell 30, Execution Count 30 —— #
# {/fact}


# {fact rule=notebook-best-practice-violation@v1.0 defects=0}
# —— Code Cell 1, Execution Count 1 —— #
# Compliant: cell is not blank. Imports are in place.
# Cell limit is not exceeding.
import numpy as np
import pandas as pd
# —— Code Cell 2, Execution Count 2 —— #
primary = pd.read_csv('attribute-primary-info.csv', sep='\t')
primary
# —— Code Cell 3, Execution Count 3 —— #
alias = pd.read_csv('attribute-alias-info-en_US.csv', sep='\t')
alias
# {/fact}
