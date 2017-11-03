# import system modules 
import arcpy
from arcpy import env

# Set environment settings
env.workspace = u"F:/"

# Set local parameters
inFeatures = []
outFeatureClass = "c:/output/output.gdb/habitat_areas"
clusTol = "0.05 Meters"

# Use the FeatureToPolygon function to form new areas
arcpy.FeatureToPolygon_management(inFeatures, outFeatureClass, clusTol,
                                  "NO_ATTRIBUTES", "")
								  
								  
								  
								  
								  