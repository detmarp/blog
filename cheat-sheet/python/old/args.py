#!/usr/bin/env python
import sys

def main(argv):
    print 'Number of arguments:', len(argv), 'arguments.'
    print 'Argument List:', argv

if __name__ == "__main__":
    main(sys.argv[1:])