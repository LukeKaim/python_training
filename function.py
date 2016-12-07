# Import modules.
import arcpy
import os
import sys
import arcpy.sa


def ends_with(string, suffix, start=0, end=-1):
    """
    Using slicing to detrimine if the the suffix is in the string. If the suffix
    is in the string then the function will return True else thee function will
    return False.
    Parameters:
        1. The string that will be used to search through.
        2. The suffix that will be used to see if the suffix is in the string
        3. String start position.
        4. string end position
    """
    # String_val is the python slice specified by the user.
    string_val = string[start][end]
    # Test if the string_val is in the suffix. Using in allows the suffix to be
    # a string or a tuple. If string_val in suffix then return True.
    if string_val in suffix:
        return True
    # Else return false. The suffix is not in the string.
    else:
        return False

def rename(value):
    """
    function will rename value if it is in the field.
    Parameters:
        1. field value.
    """
    if value in ["ST"]:
        return "Street"
    else:
        return value


def create_gdb(workspace, out_name, version="CURRENT"):
    """
    Function tests if the file geodatabase exists. If the geodatabase exists
    already then do not create it. If the file geodatabase does not exist create
    the file geodatabase.

    Parameters:
        1. workspace is the folder location.
        2. out_name is the basename of the file geodatabase.
        3. version is the geostabase version.

    """
    # Test if the geodatabase does not exist.
    if not arcpy.Exists(os.path.join(workspace, out_name)):
        arcpy.CreateFileGDB_management(workspace, out_name, version)


def field_exist(dataset, field):
    """
    Test if a field exists in a table aready. This is done using ListFields. One
    could iterate over every field and test for it that way, but this method is
    faster.
    Parameters:
        1. Dataset path that one is interested in seeing if the field exists in.
        2. The field name that one is intersted in testing if it is in the table.
    """
    try:
        list_field = arcpy.ListFields(dataset, field)
    except:
        print("error with list fields.")
        sys.exit(543)

    # If the length of the list equals 1 then the field is in the list.
    if len(list_field) == 1:
        return True
    else:
        return False

def buf_shape(fc_list, prj_code):
    """
    Function to buffer feature classes based on the shape type.
    Parameters:
        1. The feature class list.
        2. prj code.
    """
    # Set output coordinate system to 'NAD_1983_StatePlane_Colorado_
    # Central_FIPS_0502_Feet'
    # by using its factory code 26911 (available in *.prj file)
    out_cs = arcpy.SpatialReference()
    out_cs.factoryCode = prj_code
    out_cs.create()

    # For loop to interate over the list.
    for i in fc_list:
        if arcpy.Exists(i):
            out_file = i + "prj"
            arcpy.Project_management(in_dataset=i, out_dataset=out_file,
                                    out_coor_system=out_cs)
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

def main():
    """
    Main function is run if this script is not imported.
    Because this function calls other functions one is using encapsulation which
    means variables inside a function are considered local. This is very
    important.

    Parameters:
        None
    """
    # Allows esri to overwrite files.
    arcpy.overwriteOutput = True

    # Prints all of the functions in the module.
    print dir(arcpy)
    # Print the doc string of the Intersect function.
    print arcpy.Intersect_analysis.__doc__


    print ends_with("luke", ("luke" "foo"))
    print ends_with("luke", "ke", -2, -1)
    print "ffo".endswith("o")
    print str.endswith.__doc__

    # Create a geodatabase.
    create_gdb(r"C:\temp", "foom")

    fc = r"H:\rm_urisa\data\python_training.gdb\denver_parcel"
    if not field_exist(fc, "LAND"):
         arcpy.AddField_management(fc, "LAND", "TEXT")


    # Feature class list.
    file_list = [r"H:\rm_urisa\python_training\data\python_training.gdb\denver_parcel",
                 r"H:\rm_urisa\python_training\data\python_training.gdb\crime"]
    # Projection file.
    projection = r"H:\rm_urisa\python_training\data\streets.prj"
    # call the buf_shape function.
    buf_shape(fc_list=file_list, prj_file=projection)
    # Feature class list.
    file_list = [r"H:\rm_urisa\python_training\data\python_training.gdb\streets"]
    # Call the buf_shape function.
    buf_shape(fc_list=file_list, prj_file=projection)

if __name__ == "__main__":
    # Use the modules name attribute to determine if the module is being
    # imported or not.

    # Call the main function.
    main()


