import arcpy
from arcpy import env
env.workspace = "P:/python/exercise05"
if arcpy.CheckExtension("spatial") == "Available":
    arcpy.CheckOutExtension("spatial")
    out_distance = arcpy.sa.EucDistance("bike_routes.shp", cell_size = 100)
    out_distance.save("P:/python/exercise05/results/bike_dist")
    arcpy.CheckInExtension("spatial")
else:
    print "Spatial Analyst license is not available"
    
