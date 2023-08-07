#!/usr/bin/env python
import sys
import os
import re

def main():
    # match - matches at the start of a string
    print(re.match("s[^\s]*", "should match this first word").group(0))
    print(re.match("[\d]*", "not found"))

if __name__ == "__main__":
    main()