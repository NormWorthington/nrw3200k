

import arcpy
from arcpy import env
env.overwriteOutput = True
env.workspace = "P:/python/exercise06"
arcpy.CreateFileGDB_management("P:/python/exercise06/results", "new.gdb")
fclist = arcpy.ListFeatureClasses()
for fc in fclist:
    fcdesc = arcpy.Describe(fc)
    if fcdesc.shapeType == "Polygon":
        arcpy.CopyFeatures_management(fc, "P:/Python/Exercise06/Results/new.gdb/" + fcdesc.basename)
   
