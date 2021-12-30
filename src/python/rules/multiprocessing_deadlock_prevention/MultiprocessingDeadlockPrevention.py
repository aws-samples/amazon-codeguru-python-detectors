# {fact rule=multiprocessing-deadlock-prevention@v1.0 defects=1}
def deadlock_prevention_non_compliant():
    from subprocess import Popen, PIPE
    process = Popen('sh ~/example.sh', stdout=PIPE)
    # Noncompliant: uses the 'Popen.wait' with 'stdout=PIPE' or 'stderr=PIPE',
    # resulting in a potential deadlock and busy loop.
    process.wait()
    output = process.stdout.read()
    print(output)
# {/fact}


# {fact rule=multiprocessing-deadlock-prevention@v1.0 defects=0}
def deadlock_prevention_compliant():
    from subprocess import Popen, PIPE
    process = Popen('sh ~/example.sh', stdout=PIPE)
    # Compliant: uses 'Popen.communicate' method, avoiding a
    # potential deadlock and busy loop.
    print(process.communicate()[0])
# {/fact}
