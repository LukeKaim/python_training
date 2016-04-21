# List
a = ["apple", "Microsoft", "Samsung"]
# Length function.
print len(a)
# Append function. Adds items at the end of the list.
a.append("lenovo")
print a
# Extend the list by appending all items in a given list.
a.extend("foo")
print a
# Remove item in list.
a.pop(a.index("Samsung"))
print a
# Get index of item in list.
print a.index("apple")

a = ["apple", "Microsoft", "Samsung"]
# List reverse function. This can also be done using slicing.
# Python slicing. Start, stop, step.
print a[::-1]
a.reverse()
print a
# Nested list
a = [["john", "smith", "GIS programmer", 60,000],
    ["Will", "Smith", "Actor", 1000000]]

# Create a list from a comma delimited string.
string = "John, Smith, GIS programmer"
w = string.split(",")
print w

# Make clone of variable.
a = [1, 2, 3]
b = list(a)
b.append(4)
print a
print b


