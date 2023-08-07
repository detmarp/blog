#!/usr/bin/env python
import subprocess

def main():
    # in this version, we manually break the command into its parts
    print subprocess.check_output(['ls', '-l', '-d', '..'], stderr=subprocess.STDOUT)

    # or,
    # in this version we just throw the string at the shell and gather the results
    p = subprocess.Popen("ls -l | head -3", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    p_stdout = p.stdout.read()
    p_stderr = p.stderr.read()
    print p_stdout

if __name__ == "__main__":
    main()