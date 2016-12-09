# Import acrpy
import arcpy
# Import os.
import os

# Set the arcpy environment workspace where the data resides.
arcpy.env.workspace = r"H:\rm_urisa\python_training\data\python_training.gdb"
arcpy.env.overwriteOutput = True

# Instead of using workspace one can use os.path.join.
data_folder = r"H:\rm_urisa\python_training\data"
data_workspace = os.path.join(data_folder, "python_training.gdb")
crime_fc = os.path.join(data_workspace, "crime")
# prj file location.
prj_file = os.path.join(data_workspace, "streets.prj")

fc = "foo.shp"
# Splitext function returns path and extension.
path =  os.path.splitext(fc)
basename = path[0]
print basename

# For loop to iterate over a list.
grocery_list = ["Apple", "Chicken", "Cookie"]
for i in grocery_list:
    print(i)

# For loop using xrange to interate from 99 to 0. xrange returns an
# xrange object. This is what is known as a generator in python.
for i in xrange(99, 0, -1):
    print("{0} bottles of beer on the wall, {0} bottle of beer "
         "take one down pass it around.".format(i))

# For loop using range to iterate from  99 to 0. range returns a list object.
# In python 3 xrange is deprecated and will be range.
for i in range(99, 0, -1):
        print("{0} bottles of beer on the wall, {0} bottle of beer "
         "take one down pass it around.".format(i))

# While loop example.
i = 0
while i < 100:
    print i
    i += 1

# While loop with infinite loop.
i = 101
while i < 100:
    print i
    i += 1

# While loop to iterate over a list.
fc_list = ["foo.shp", "too.shp"]
i = 0
while i < len(fc_list):
    print fc_list[i]
    i += 1

# While loop to iterate from 99 to 0.
i = 99
while i >= 0:
    print("{0} bottles of beer on the wall, {0} bottle of beer "
         "take one down pass it around.".format(i))
    i -= 1


# List Comprehension
numbers = [n for n in range(100)]
print numbers

# List Comprehension
fc = r"denver_parcel"
fields = [field.name for field in arcpy.ListFields(fc)]
print(fields)

# For loop to test if there is an even number in a list.
# Even numbers will have 0 remainder. This is done with if statement.
even = None
n = [1, 2, 3, 4, 5]
for i in n:
    if i % 2 == 0:
        even = True
        break
if even:
    print("List contains even number")
else:
    print("List does not contian even number.")

# For else. If the for loop finishes sucessfully then go into the else.
even = None
for i in n:
    if i % 2 == 0:
        print("List contains even numbers")
        break
else:
    print("List does not contains even numbers.")


# Sometimes one does not want to break out of the loop, but continue to the next
# iteration of the loop.
w = 50
for i in range(100):
    if i < 50:
        continue
    else:
        print i
    print "test"


# Break exits the loop. 
w = 50
for i in range(100):
    if i < 50:
        break
    else:
        print i
    print "test"

# Pass continues though the loop. Pass can be used when no action requires.
w = 50
for i in range(100):
    if i < 50:
        pass
    else:
        print i
    print "test"


# Feature class list.
fc_list = ["denver_parcel",
             "crime"]

# Set output coordinate system to 'NAD_1983_StatePlane_Colorado_
# Central_FIPS_0502_Feet'
# by using its factory code 26911 (available in *.prj file)
outCS = arcpy.SpatialReference()
outCS.factoryCode = 2232
outCS.create()


# For loop to interate over the list. Why will this only work with
# feature classes?
for i in fc_list:
    if arcpy.Exists(i):
        out_file = i + "prj"
        arcpy.Project_management(in_dataset=i, out_dataset=out_file,
                                out_coor_system=outCS)
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
        else:
            print("Please select a new file. The file cannot be MultiPoint or "
            "MultiPatch.")
            # Continue to the next iteration. Do not want to buffer.
            continue
        # Buffer each file. The output name is input name + buff.
        arcpy.Buffer_analysis(out_file, out_file + "buff", buffer_distance)
    # Else the file does not exist. Print message to the user.
    else:
        print("File does not exist")


# Set output coordinate system to 'NAD_1983_StatePlane_Colorado_
# Central_FIPS_0502_Feet'
# by using its factory code 26911 (available in *.prj file)
outCS = arcpy.SpatialReference()
outCS.factoryCode = 2232
outCS.create()

# For loop to interate over the list. Why will this only work with
# feature classes?
for i in fc_list:
    if arcpy.Exists(i):
        out_file = i + "prj"
        arcpy.Project_management(in_dataset=i, out_dataset=out_file,
                                out_coor_system=outCS)
        # Use describe to get file information.
        desc = arcpy.Describe(out_file)
        # Test if the shapetype.
        if desc.shapeType == "Polygon":
           # Buffer each file. The output name is input name + buff.
            arcpy.Buffer_analysis(out_file, out_file + "buff", 200)
        elif desc.shapeType == "Polyline":
            # Buffer each file. The output name is input name + buff.
            arcpy.Buffer_analysis(out_file, out_file + "buff", 100)
        elif desc.shapeType == "Point":
            # Buffer each file. The output name is input name + buff.
            arcpy.Buffer_analysis(out_file, out_file + "buff", 50)
        else:
            print("Please select a new file. The file cannot be MultiPoint or "
            "MultiPatch.")
    # Else the file does not exist. Print message to the user.
    else:
        print("File does not exist")













