# {fact rule=multidimension-list-using-replication@v1.0 defects=1}
def error_prone_multidimensional_list_non_compliant():
    # Noncompliant: initialises a multidimensional list using replication.
    multi_dimension_list = [[None]]*3
# {/fact}


# {fact rule=multidimension-list-using-replication@v1.0 defects=0}
def error_prone_multidimensional_list_compliant():
    # Compliant: avoids initialising a multidimensional list using replication.
    multi_dimension_list = [None]*2
# {/fact}