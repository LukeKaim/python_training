# Strings
a = "foo"
b = "bat"

# String concatenation produces a new string.
c = a + b
print c


# Length function.
a = "Fooo"
print len(a)

# Join function.
c = ("A", "B", "C")
print "-".join(c)

#print a[5]
print a[2]

# Replace function.
b = a.replace("foo", "too")
print b

# find function.
print a.find("fo")
# evaluate if fo is in a.
print "fo" in a


# Python slicing. Slice start, stop, step
# slicing is very powerful and can be used on strings, lists or tuples.
# Index starts at 0.
w = "yadf;lkbdfmbdfklmbmbkm"
# Can start at the end of the string, list or tuple.
print w[0:-1]
print w[0:21]
print w[:21]
print w[0:6]

# Reverse order of string. This works on lists as well.
# This can be useful when deleting elements out of a list because one needs
# to start at the end of the list first .
print w[21:0:-1]
