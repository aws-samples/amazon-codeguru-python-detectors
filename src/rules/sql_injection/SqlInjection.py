# {fact rule=sql-injection@v1.0 defects=1}
def execute_query_non_compliant(request):
    import sqlite3
    name = request.GET.get("name")
    query = "SELECT * FROM Users WHERE name = " + name + ";"
    connection = sqlite3.connect("example.db")
    cursor = connection.cursor()
    # Noncompliant: user input might contain malicious special characters.
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
    connection = sqlite3.connect("example.db")
    cursor = connection.cursor()
    # Compliant: user input is sanitized before use.
    cursor.execute(query)
    connection.commit()
    connection.close()
# {/fact}
