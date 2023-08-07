#!/usr/bin/env python

print "one string plus " + "another"
print "number is " + str(5)
print "list is " + str(range(3))

print '''this is a
long string
with linebreaks
in it'''

print "The %% operator does %s formatting: %d" % ("built-in", 42)

print "{} + {} = {}".format(0, 1, 2)    # deprecated (not using postions)
print "{2} = {0} + {1}".format(1, 21, 22) # do it this way

joined = ", ".join(["one", "two", "three"])
print joined

split = joined.split(",")
print split
