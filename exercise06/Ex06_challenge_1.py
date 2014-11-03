

import arcpy
from arcpy import env
env.overwriteOutput = True
env.workspace = "P:/python/exercise06"
fclist = arcpy.ListFeatureClasses("")
for fc in fclist:
    fcdesc = arcpy.Describe(fc)
    print fcdesc.name + " is a " + fcdesc.shapeType
       
