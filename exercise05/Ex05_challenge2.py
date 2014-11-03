import arcpy
from arcpy import env

env.workspace = "P:/Python/Exercise05"

in_data = "hospitals.shp"
in_features = "hospitalsXYpts.shp"

Arcpy.Copy_management(in_data, in_features)

Arcpy.AddXY_management(in_features)
