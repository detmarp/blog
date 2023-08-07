#!/usr/bin/env python

# arrays

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

ten_zeroes = [0] * 10

# dictionaries

dog = {"name":"elvis","age":25}

dog2 = {}
dog2["name"] = "petey"
dog2["age"] = 14

for key in dog2:
    print "in dog2, {0} -> {1}".format(key, dog2[key])

if "age" in dog2:
    print "key exists"

dog3 = dict([("name", "yeller"), ("age", 8)]) # from a list of tuples

print(dog)
print(dog2)
print(dog3)

keys = range(5)  # 0 - 4
values = ["a","b","c","d","e"]
print zip(keys, values)
d = dict(zip(keys, values))
print d

# pythonic collection management
# pythonic collection management
# pythonic collection management

# new list, from items in list
a = [1, 2, 3]
print([n**2 for n in a])
