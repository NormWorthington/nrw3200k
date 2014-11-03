import arcpy
from arcpy import env
env.overwriteOutput = True
env.workspace = "P:/python/exercise06"
fieldlist = arcpy.ListFields("cities.shp")
for field in fieldlist:
    print field.name + " " + field.type
