import arcpy.mapping

print dir(arcpy.mapping)

mxd_file = r"H:\rm_urisa\python_training\data\python_training.mxd"
mxd = arcpy.mapping.MapDocument(mxd_file)
for df in arcpy.mapping.ListDataFrames(mxd):
    mxd.title = "Denver"
    mxd.saveACopy(r"H:\rm_urisa\python_training\data\python_training2.mxd")
del mxd

