#!/usr/bin/env python
# Normally, python won't create a .pyc file for programs run directly.
# But for files you import, it will create a .pyc

# But you can do this

import sys
sys.dont_write_bytecode = True

# ... which will prevent any further imports from barfing out a .pyc file
# It looks like it's too late to stop the file it's in from writing a .pyc
# however.

def main():
    print "Hello world."

if __name__ == "__main__":
    main()