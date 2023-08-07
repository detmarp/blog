#!/usr/bin/env python
import sys
import json

def main(argv):
    if len(argv) != 2:
        print 'Error - expected 2 arguments'
    else:
        with open(argv[0], 'r') as f:
            data = json.load(f)     
        with open(argv[1], 'w') as f:
            json.dump(data, f)
        # Reading data back
        print 'ok'

if __name__ == "__main__":
    main(sys.argv[1:])
