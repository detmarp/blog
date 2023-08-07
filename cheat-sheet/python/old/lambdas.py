#!/usr/bin/env python

# call three functions, passed in as parameters
def call_a_b_c(a, b, c):
    print "A returns: " + str(a(1))
    print "B returns: " + str(b(2))
    print "C returns: " + str(c(3))

def B(x):
    print "(inside of B: {})".format(x)

call_a_b_c(
    lambda x: "here's A: " + str(x),
    B,
    lambda x: 42
    )
