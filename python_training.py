









# Feature class list.
fc_list = [r"H:\rm_urisa\data\python_training.gdb\denver_parcel",
             r"H:\rm_urisa\data\python_training.gdb\crime"]

# For loop to interate over the list.
for i in fc_list:
    if arcpy.Exists(i):
        # Use describe to get file information.
        desc = arcpy.Describe(i)
        # Test if the shapetype.
        if desc.shapeType == "Polygon":
            # set buffer distance to 200.
            buffer_distance = 200
        elif desc.shapeType == "Polyline":
             buffer_distance = 100
        elif desc.shapeType == "Point":
            buffer_distance = 50
        # Buffer each file. The output name is input name + buff.
        arcpy.Buffer_analysis(i, i + "buff", buffer_distance)














