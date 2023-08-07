#!/usr/bin/env python
import sys
import os

def main():
    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    parent = os.path.dirname(path)
    print(parent)

    print("all files")
    for root, folders, files in os.walk(parent, topdown=True):
        for file in files:
            print("  " + os.path.join(root, file))

    print
    print("all folders")
    for root, folders, files in os.walk(parent, topdown=True):
        print("  " + root + "/")

    # just find all .py files, in flat folder
    print
    print(".py files, in current")
    for py in [file for file in os.listdir(path)
        if os.path.isfile(file) and file.endswith(".py")]:
        print("  " + py)

    # ... or
    print
    print(".py files, in current, simpler")
    for file in os.listdir(path):
        if os.path.isfile(file) and file.endswith(".py"):
            print("  " + file)

if __name__ == "__main__":
    main()