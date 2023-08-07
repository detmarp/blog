#!/usr/bin/env python
# http://www.tutorialspoint.com/python/python_lists.htm

a = range(0, 6)
# ... is the same as ...
a = [0, 1, 2, 3, 4, 5]
print a

a.append("end")

a.remove(4) # removes the item sith the value 4
del a[1] #removes the item at index 1
print a

print a[-1] # "end"
print a[1:] # from [1] to end
print a[:1] # just [0]
print a[2:4] # from [2] upto, but not including [4]

length = len(a)
find = 3 in a  # True
concatenated = a + a
for x in a:
    foo = x


