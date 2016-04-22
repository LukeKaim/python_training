import os

files = []
# os.walk example. Recursively walk the tree.
w = os.walk(r"C:\temp\test")
for root, dirs, file in w:
    files.append(file)
print files

files_2 = []
# os.listdir example. Need to iterate over each folder and then each file in
# that folder.
name = os.listdir(r"C:\temp\test")
# Iterate over the items in
d = []
for i in name:
    if os.path.isdir(os.path.join(r"C:\temp\test", i)):
        t = []
        for f in os.listdir(os.path.join(r"C:\temp\test", i)):
            t.append(f)
        files_2.append(t)
    else:
        d.append(i)

files_2.append(d)
print files_2












