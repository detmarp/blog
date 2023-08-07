#!/usr/bin/python
import sys
sys.dont_write_bytecode = True

import classone

def main():
    c1 = classone.ClassOne()
    c2 = classone.ClassOne.from_xy(11, 22)
    c3 = classone.ClassOne.from_ClassOne(c2)
    c4 = c2.add(c3)
    
    print str(c1)
    print str(c2)
    print str(c3)
    print str(c4)
    print c4.__dict__
    
if __name__ == "__main__":
    main()
