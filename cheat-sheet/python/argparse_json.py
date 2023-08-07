#!/usr/bin/env python3

""" A sample python program that reads a JSON file.

Here I could say a little bit more.  This reads JSON from a file,
and takes a few optinal command line flags.

usage: argparse_json.py JSONFILE [-h] [-s]

optional arguments:
  -h, --help     show this help message and exit
  -s, --summary  Show Summary
"""

import json
import sys

class Program(object):
  def __init__(self, json_filename, verbose = False):
    self.json_filename = json_filename
    self.verbose = verbose

  def load(self):
    with open(self.json_filename) as f:
      self.data = json.load(f)

  def status(self):
    print(f'File: {self.json_filename}')
    print(f'Contents: {sys.getsizeof(self.data)}')

  def print(self):
    print(json.dumps(self.data, sort_keys = True, indent = 2))

import argparse
import sys

def main():
  parser = argparse.ArgumentParser()

  parser.add_argument("filename", help="required positional arg")
  parser.add_argument("-s", "--summary", action="store_true", help="Show Summary")
  parser.add_argument("-p", "--print", action="store_true", help="Print")

    # this call will exit the program, if the syntax fails...
  try:
    args = parser.parse_args()
  except:
    sys.exit(1)

  args = parser.parse_args()

  program = Program(args.filename, verbose = args.summary)
  program.load()
  if (args.summary):
    program.status()
  if (args.print):
    program.print()

if __name__ == "__main__":
  main()