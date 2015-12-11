import arcpy

### For loop to iterate over a list.
##grocery_list = ["Apple", "Chicken", "Cookie"]
##for i in grocery_list:
##    print(i)
##
### For loop using xrange to interate from 99 to 0. xrange returns an
### xrange object. This is what is known as a generator in python.
##for i in xrange(99, 0, -1):
##    print("{0} bottles of beer on the wall, {0} bottle of beer "
##         "take one down pass it around.".format(i))
##
### For loop using range to iterate from  99 to 0. range returns a list object.
### In python 3 xrange is deprecated and will be range.
##for i in range(99, 0, -1):
##        print("{0} bottles of beer on the wall, {0} bottle of beer "
##         "take one down pass it around.".format(i))
##
##
##
### While loop example.
##i = 0
##while i < 100:
##    print i
##    i += 1
##
### While loop with infinite loop.
##i = 101
##while i < 100:
##    print i
##    i += 1
##
### While loop to iterate over a list.
##fc_list = ["foo.shp", "too.shp"]
##i = 0
##while i < len(fc_list):
##    print fc_list[i]
##    i += 1
##
##
### List Comprehension
##numbers = [n for n in range(100)]
##print numbers
##
##
### For loop to test if there is an even number in a list.
###Even numbers will have 0 remainder. This is done with if statement.
##even = None
##n = [1, 2, 3, 4, 5]
##for i in n:
##    if i % 2 == 0:
##        even = True
##        break
##if even:
##    print("List contains even number")
##else:
##    print("List does not contian even number.")
##
### For else. If the for loop finishes sucessfully then go into the else.
##even = None
##for i in n:
##    if i % 2 == 0:
##        evev = True
##        print("List contains even numbers")
##        break
##else:
##    print("Lists contains even numbers.")
##


# Feature class list.
fc_list = [r"H:\rm_urisa\python_training\data\python_training.gdb\denver_parcel",
             r"H:\rm_urisa\python_training\data\python_training.gdb\crime"]
prj_file = r"H:\rm_urisa\python_training\data\streets.prj"

# For loop to interate over the list.
for i in fc_list:
    if arcpy.Exists(i):
        out_file = i + "prj"
        arcpy.Project_management(in_dataset=i, out_dataset=out_file,  out_coor_system=prj_file)
        # Use describe to get file information.
        desc = arcpy.Describe(out_file)
        # Test if the shapetype.
        if desc.shapeType == "Polygon":
            # set buffer distance to 200.
            buffer_distance = 200
        elif desc.shapeType == "Polyline":
             buffer_distance = 100
        elif desc.shapeType == "Point":
            buffer_distance = 50
        # Buffer each file. The output name is input name + buff.
        arcpy.Buffer_analysis(out_file, out_file + "buff", buffer_distance)
    # Else the file does not exist. Print message to the user.
    else:
        print("File does not exist")










