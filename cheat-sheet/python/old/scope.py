#!/usr/bin/env python

x = 100 # global; outside any function or lambda

def boo():
    z = x + 1 # z is local; but x is global (on the right side of an equals)
    print z
    print locals()

def foo():
    x = 200 # local; a variable on the left side of an equals is a local
    print x
    print locals()

def goo():
    global x # using the global 'x'
    x = 300 # sets the global
    print x
    print locals() # 'x' will not show up as a local

print x
boo()
foo()
goo() # will modify the global 'x'
print x
print locals()
print globals()

# by convention, module functions starting with underscore should be treated as private
def _i_am_private():
    print "woot"
