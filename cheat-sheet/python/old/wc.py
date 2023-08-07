#!/usr/bin/env python

# Detmar note to self
# I never finished writing this program, but at least it does something
# it only fakes the line and word counting; and the output isn't formatted
# right.  mostly I wanted to figure out some of the arg parsing.

import argparse
import sys

def main():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('infile', nargs='*', type=argparse.FileType('r'), default=sys.stdin)    
    parser.add_argument("-c", "--characters", action="store_true", help="count bytes")
    parser.add_argument("-w", "--words", action="store_true", help="count words")
    parser.add_argument("-l", "--lines", action="store_true", help="count lines")
    
    # this call will exit the program, if the syntax fails...
    args = parser.parse_args()

    characters = args.characters
    lines = args.lines
    words = args.words

    if  not characters and not lines and not words:
        characters = True
        words = True
        lines = True

    for f in args.infile:
        text = f.read()
        if characters:
            print " {}".format(len(text))
        if words:
            print " {}".format(text.count(' '))
        if lines:
            print " {}".format(text.count('\n'))
    
if __name__ == "__main__":
    main()