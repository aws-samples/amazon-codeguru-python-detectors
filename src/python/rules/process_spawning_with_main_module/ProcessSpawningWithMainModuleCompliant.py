# {fact rule=process-spawning-with-main-module@v1.0 defects=0}
from multiprocessing import Process, set_start_method


def fork_compliant(message):
    print(str(message) + "fork use case!!")


# Compliant: safely imports main module prior to executing the function.
if __name__ == '__main__':
    set_start_method('fork', force=True)
<<<<<<< HEAD
    Process(target=fork_compliant).start()
=======
    Process(target=fork_compliant, args=('Compliant',)).start()
>>>>>>> 0c4b35e (Add examples of python/equality-vs-identity@v1.0, python/multiple-values-in-return@v1.0, python/multiprocessing-deadlock-prevention@v1.0, python/mutually-exclusive-calls-found@v1.0, python/naive-datetime-time-zone-issues@v1.0, python/object-dict-modification@v1.0, python/partial-encryption@v1.0, python/pep8-recommendations@v1.0, python/process-spawning-with-main-module@v1.0, python/resource-leak@v1.0 and change lint.yml)
# {/fact}
