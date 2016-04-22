# Python operators.
a = 2
b = 2

# Equality
print a == b

# Identity tests if the two objects in memory are the same. is and is not.
a = [1, 2, 3]
b = [1, 2, 3]
print(id(a))
print(id(b))
print(a is b)

# Set b object equal to a object.
a = b
print(id(a))
print(id(b))
print(a is b)

a = 10
b = 2
# Not equal.
print a!= b
# Not equal.
print a <> b
# Less than.
print a < b
# Less then or equal to.
print a <= b

a = 10
# In operator.
a in [10, 11, 13]
# Not in operator.
a not in [10, 11, 13]

# Add and.
b = 2
b += 1
print b

# Subtract AND
b = 2
b -= 1
print b



