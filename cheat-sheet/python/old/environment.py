#!/usr/bin/env python3
import sys
import os

def main(argv):
    print("Python version: " + sys.version)
    print("Executable: " + sys.executable)
    print("This file: " + os.path.realpath(__file__))
    print("Number of arguments: " + str(len(argv)))
    print("Argument list:" + str(argv))

if __name__ == "__main__":
    main(sys.argv[1:])
