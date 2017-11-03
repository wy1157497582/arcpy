import arcpy, string, math
from arcpy import env
env.overwriteOutput = True
env.workspace = r"F:/China_1km.gdb"
print("Deleting redundant feature classes...")
arcpy.DeleteFeatures_management("B_Provinces_Dis")
print("B_Provinces_Dis deleted.")

rPCLs = arcpy.ListFeatureClasses("PCL*")
for rPCL in rPCLs:
	arcpy.DeleteFeatures_management(rPCL)
	print(rPCL+" deleted.")
print("rPCLs clear.")

rPOIs = arcpy.ListFeatureClasses("POI*")
for rPOI in rPOIs:
	arcpy.DeleteFeatures_management(rPOI)
	print(rPOI+" deleted.")
print("rPOIs clear.")
print("---All Clear---")