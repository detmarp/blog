#!/usr/bin/env python3
import argparse

class Program(object):
    def __init__(self, verbose = False):
        self.verbose = verbose

    def run(self):
        print("Verbose {}".format(self.verbose))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", action="store_true", help="be verbose")
    args = parser.parse_args()

    program = Program(verbose = args.verbose)
    program.run()

if __name__ == "__main__":
    main()
