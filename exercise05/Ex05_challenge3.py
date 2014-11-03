import arcpy
from arcpy import env
env.workspace = "P:/Python/Exercise05"
in_features = "parks.shp"
tempLayer = "parkslyr.shp"
expression = arcpy.AddFieldDelimiters(in_features, "PARK_TYPE")
outFeatureClass = "P:/Python/Exercise05/Results/parks_diss.shp"
dissolveFields = ["PARK_TYPE"]
arcpy.MakeFeatureLayer_management(in_features, tempLayer)
