# {fact rule=process-spawning-with-main-module@v1.0 defects=1}
from multiprocessing import Process, set_start_method


def fork_non_compliant():
    print('fork use case!!')


# Noncompliant: fails to import main module prior to executing the function.
set_start_method('fork', force=True)
Process(target=fork_non_compliant).start()
# {/fact}
