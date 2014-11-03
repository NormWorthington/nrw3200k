import arcpy
from arcpy import env
env.workspace = "P:/Python/Exercise05"
print "The following extensions are available:"
extensions = ["3D", "Network", "Spatial"]

for extension in extensions:
    if arcpy.CheckExtension(extension) == "Available":
        print extension
    
