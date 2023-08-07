#!/usr/bin/env python
import os, sys

def make_folder(name):
    folder = os.path.abspath(name)
    if not os.path.exists(folder):
        os.makedirs(folder)
    return folder

# make a data folder, that's a child of this script's folder
def make_data_folder():
    this_scripts_folder = os.path.dirname(os.path.abspath(sys.argv[0]))
    folder = os.path.join(this_scripts_folder, "data")
    return make_folder(folder)


print "Current folder: %s" % os.getcwd()

print "this script's folder: %s" % os.path.dirname(os.path.abspath(sys.argv[0]))

# make a sub folder, and write a file to it
filename = os.path.join(make_data_folder(), "folders.txt")
print "Data filename is: %s"% filename
with open(filename, "w") as file:
    file.write("Hi\n")

