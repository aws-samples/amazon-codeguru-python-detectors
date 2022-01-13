#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=sql-injection@v1.0 defects=1}
def execute_query_noncompliant(request):
    import sqlite3
    name = request.GET.get("name")
    query = "SELECT * FROM Users WHERE name = " + name + ";"
    with sqlite3.connect("example.db") as connection:
        cursor = connection.cursor()
        # Noncompliant: user input is used without sanitization.
        cursor.execute(query)
        connection.commit()
        connection.close()
# {/fact}


# {fact rule=sql-injection@v1.0 defects=0}
def execute_query_compliant(request):
    import re
    import sqlite3
    name = request.GET.get("name")
    query = "SELECT * FROM Users WHERE name = "
    + re.sub('[^a-zA-Z]+', '', name) + ";"
    with sqlite3.connect("example.db") as connection:
        cursor = connection.cursor()
        # Compliant: user input is sanitized before use.
        cursor.execute(query)
        connection.commit()
        connection.close()
# {/fact}
