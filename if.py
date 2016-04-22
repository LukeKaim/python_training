# Import module
import arcpy

a = True
b = False
# Test if a is True.
if a == True:
    print(True)

# Test if value is True. This is shorter to write then the above test.
if a:
    print(True)

if b:
    print(True)

# Test if a is true or b is true.
if a == True or b == True:
    print(True)

# Test if a and b are both true.
if a == True and b == True:
    print(True)
else:
    print(False)

c = 10
d = 15
# Test if c does not equal d.
if c != d:
    print("A and B are not equal.")
else:
    print("A and B are equal.")

# Test if value is in list.
a = 1
if a in [1, 2, 4]:
    print("yes")
else:
    print("{0} is not in the list.".format(a))

value = 51
# Nested if statements example. Be careful of control flow.
# This can be useful for classifying data or making decisions.
if value > 0:
    rank = "low"
    if value > 50:
        rank = "medium"
        if value > 75:
            rank = "high"
print(rank)

# If elif statement to classify data.
if value > 0 and value <= 50:
    rank = "low"
elif value > 50 and value <= 75:
    rank = "medium"
elif value > 75:
    rank = "high"
print(rank)

# Test product infromation.
product_info = arcpy.ProductInfo()
if product_info == "ArcInfo":
    product = product_info
elif product_info == "ArcEditor":
    product = product_info
elif product_info == "ArcView":
    product = product_info
elif product_info == "ArcServer":
    product = product_info
print(product)

# Test what version esri is installed on the computer.
dic = arcpy.GetInstallInfo()
version = dic['Version']
if version == '10.3.1':
    print(version)
elif version == '10.2.1':
    print(version)

# Feature class path. The location might be different.
# Later we will conver how to avoid having absolute file paths.
fc = r"H:\rm_urisa\data\python_training.gdb\denver_parcel"
# Test if a file exists.
if arcpy.Exists(fc):
    print("exists")
else:
    print("File does not exist.")

# Use the describe function to get the shape type of the file.
desc = arcpy.Describe(fc)
print desc.shapeType


# Test if the file exists and then test if the file shape type equals Polygon
if arcpy.Exists(fc):
    desc = arcpy.Describe(fc)
    if desc.shapeType == "Polygon":
        print(desc.shapeType)
    # Please finish the logic.
else:
    print("{0} does not exist.".format(fc))


# Code to test if a file exists.
if arcpy.Exists(fc):
    # Use Describe to get the shape type of the file. Test if the shape type
    # is polygon, polyline or point.
    desc = arcpy.Describe(fc)
    if desc.shapeType == "Polygon":
        shape_type = desc.shapeType
    elif desc.shapeType == "Polyline":
        shape_type = desc.shapeType
    elif desc.shapeType == "Point":
        shape_type = desc.shapeType
    # Else the user has to select a different file.
    # This software does not handle MultiPatch or MultiPoint.
    else:
        shape_type = "Please select another file"
    print shape_type
else:
    print("{0} does not exist.".format(fc))

# Code to test if a file exists and then test if the shape type is polyline,
# polygon or point.
if arcpy.Exists(fc):
    desc = arcpy.Describe(fc)
    if desc.shapeType in ["Polygon", "Polyline", "Point"]:
        print desc.shapeType
    else:
        print("Please select another file")
else:
    print("{0} does not exist.".format(fc))












=======
# Import module
import arcpy

a = True
b = False
# Test if a is True.
if a == True:
    print(True)

# Test if value is True. This is shorter to write then the above test.
if a:
    print(True)

if b:
    print(True)

# Test if a is true or b is true.
if a == True or b == True:
    print(True)

# Test if a and b are both true.
if a == True and b == True:
    print(True)
else:
    print(False)

c = 10
d = 15
# Test if c does not equal d.
if c != d:
    print("A and B are not equal.")
else:
    print("A and B are equal.")

# Test if value is in list.
a = 1
if a in [1, 2, 4]:
    print("yes")

value = 51
# Nested if statements example. Be careful of control flow.
# This can be useful for classifying data or making decisions.
if value > 0:
    rank = "low"
    if value > 50:
        rank = "medium"
        if value > 75:
            rank = "high"
print rank

# Test product infromation.
product_info = arcpy.ProductInfo()
if product_info == "ArcInfo":
    product = "ArcInfo"
elif product_info == "ArcEditor":
    product = "ArcEditor"
elif product_info == "ArcView":
    product = "ArcView"
elif product_info == "ArcServer":
    product = "ArcServer"
print product

# Test what version esri is installed on the computer.
dic = arcpy.GetInstallInfo()
version = dic['Version']
if version == '10.3.1':
    print("10.3.1")
elif version == '10.2.1':
    print('10.2.1')

# Feature class path. The location might be different.
# Later we will conver how to avoid having absolute file paths.
fc = r"H:\rm_urisa\data\python_training.gdb\denver_parcel"
# Test if a file exists.
if arcpy.Exists(fc):
    print("exists")
else:
    print("File does not exist.")

# Use the describe function to get the shape type of the file.
desc = arcpy.Describe(fc)
print desc.shapeType





# Test if the file exists and then test if the file shape type equals Polygon
if arcpy.Exists(fc):
    desc = arcpy.Describe(fc)
    if desc.shapeType == "Polygon":
        print("Polygon")
    # Please finish the logic.
else:
    print("{0} does not exist.".format(fc))



# Code to test if a file exists and then test if the shape type is polyline,
# polygon or point.
if arcpy.Exists(fc):
    desc = arcpy.Describe(fc)
    if desc.shapeType == "Polygon":
        shape_type = "Polygon"
    elif desc.shapeType == "Polyline":
        shape_type = "Polyline"
    elif desc.shapeType == "Point":
        shape_type = "point"
    else:
        shape_type = "Please select another file"
    print shape_type
else:
    print("{0} does not exist.".format(fc))

# Code to test if a file exists and then test if the shape type is polyline,
# polygon or point.
if arcpy.Exists(fc):
    desc = arcpy.Describe(fc)
    if desc.shapeType in ["Polygon", "Polyline", "Point"]:
        print desc.shapeType
    else:
        shape_type = "Please select another file"
else:
    print("{0} does not exist.".format(fc))












>>>>>>> origin/master
