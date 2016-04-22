# Dictionary to store student grades.
dic = {1 : 99, 2 : 33, 3 : 85, 4 : 75 }
# Length of the dictionary.
print len(dic)
# Using the key of the dictionary return the value.
print dic[1]
# Delete a key in the dictionary.
del dic[4]
print dic

# Use iteritems to interate through the keys and values.
for key, value in dic.iteritems():
    print key, value

# Dictionaries values can be a list. This is useful for classifying data.
dic = {"water" : ["River", "stream", "Ocean"]}
print len(dic)
print dic

