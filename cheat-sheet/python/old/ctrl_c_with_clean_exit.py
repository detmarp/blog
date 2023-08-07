#!/usr/bin/env python

import sys
try:
    n=1
    while True:
        print('{}{}'.format("Press Ctrl-C  ", n))
        n=n+1
except KeyboardInterrupt:
    sys.exit(0) # ...or 1, or whatever