# {fact rule=improper-wildcard-sanitization@v1.0 defects=1}
def wildcard_sanitization_non_compliant():
    import os
    import subprocess
    # Noncompliant: vulnerable to wildcard injection.
    os.system("/bin/tar xvzf *")
    os.system('/bin/chown *')
    os.popen2('/bin/chmod *')
    subprocess.Popen('/bin/chown *', shell=True)
# {/fact}


# {fact rule=improper-wildcard-sanitization@v1.0 defects=0}
def wildcard_sanitization_compliant():
    import os
    import subprocess
    # Compliant: not vulnerable to wildcard injection.
    subprocess.Popen('/bin/rsync *')
    subprocess.Popen("/bin/chmod *")
    subprocess.Popen(['/bin/chown', '*'])
    subprocess.Popen(["/bin/chmod", sys.argv[1], "*"],
                     stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    os.spawnvp(os.P_WAIT, 'tar', ['tar', 'xvzf', '*'])
# {/fact}
