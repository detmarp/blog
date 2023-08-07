 #!/usr/bin/env python
import sys
import os
import inspect

def do_import(module_name):
    try:
        __import__(module_name)
    except ImportError:
        return False
    else:
        return True

def test_import(module_name):
    print "Trying to import " + module_name
    ok = do_import(module_name)
    print "  result " + str(ok)
    
def main():
    test_import("sys")
    test_import("image")
    test_import("foobar")
    
if __name__ == "__main__":
    main()
