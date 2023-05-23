#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=notebook-best-practice-violation@v1.0 defects=1}
# —— Code Cell 1 —— #
import numpy as np
# —— Code Cell 2 —— #
# Noncompliant: imports are not in the first code cell.
import pandas as pd
primary = pd.read_csv('attribute-primary-info.csv', sep='\t')
primary
# —— Code Cell 3 —— #
alias = pd.read_csv('attribute-alias-info-en_US.csv', sep='\t')
alias
# —— Code Cell 4 —— #
# Noncompliant: blank cells.
# —— Code Cell 5 —— #

# —— Code Cell 6 —— #

# —— Code Cell 7 —— #

# —— Code Cell 8 —— #

# —— Code Cell 9 —— #
print('Hello World!')
# —— Code Cell 10 —— #
print('Hello World!')
# —— Code Cell 11 —— #
print('Hello World!')
# —— Code Cell 12 —— #
print('Hello World!')
# —— Code Cell 13 —— #
print('Hello World!')
# —— Code Cell 14 —— #
print('Hello World!')
# —— Code Cell 15 —— #
print('Hello World!')
# —— Code Cell 16 —— #
print('Hello World!')
# —— Code Cell 17 —— #
print('Hello World!')
# —— Code Cell 18 —— #
print('Hello World!')
# —— Code Cell 19 —— #
print('Hello World!')
# —— Code Cell 20 —— #
print('Hello World!')
# —— Code Cell 21 —— #
print('Hello World!')
# —— Code Cell 22 —— #
print('Hello World!')
# —— Code Cell 23 —— #
print('Hello World!')
# —— Code Cell 24 —— #
print('Hello World!')
# —— Code Cell 25 —— #
print('Hello World!')
# —— Code Cell 26 —— #
print('Hello World!')
# —— Code Cell 27 —— #
# Noncompliant: too many code cells.
print('Hello World!')
# —— Code Cell 28 —— #
# —— Code Cell 29 —— #
# —— Code Cell 30 —— #
# {/fact}


# {fact rule=notebook-best-practice-violation@v1.0 defects=0}
# —— Code Cell 1 —— #
# Compliant: cell is not blank. Imports are in place.
# Cell limit is not exceeding.
import numpy as np
import pandas as pd
# —— Code Cell 2 —— #
primary = pd.read_csv('attribute-primary-info.csv', sep='\t')
primary
# —— Code Cell 3 —— #
alias = pd.read_csv('attribute-alias-info-en_US.csv', sep='\t')
alias
# {/fact}
