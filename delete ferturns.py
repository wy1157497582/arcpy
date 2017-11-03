# Name: DeleteFeatures_Example2.py
# Description: Delete features from a feature class based on an expression
# -*- coding: utf-8 -*-  
# Import system modules
import arcpy
 
# Set environment settings
arcpy.env.workspace = "C:/data/airport.gdb"
 
# Set local variables
inFeatures = "parcels"
outFeatures = "C:/output/output.gdb/new_parcels"
tempLayer = "parcelsLayer"
expression = arcpy.AddFieldDelimiters(tempLayer, "PARCEL_ID") + " = 'Cemetery'"
try:
    # Execute CopyFeatures to make a new copy of the feature class
    arcpy.CopyFeatures_management(inFeatures, outFeatures)
 
    # Execute MakeFeatureLayer
    #arcpy.MakeFeatureLayer_management(outFeatures, tempLayer)
 
    # Execute SelectLayerByAttribute to determine which features to delete
    arcpy.SelectLayerByAttribute_management(tempLayer, "NEW_SELECTION", 
                                            expression)
 
    # Execute GetCount and if some features have been selected, then 
    #  execute DeleteFeatures to remove the selected features.
    if int(arcpy.GetCount_management(tempLayer).getOutput(0)) > 0:
        arcpy.DeleteFeatures_management(tempLayer)
         
except Exception:
    e = sys.exc_info()[1]
    arcpy.AddError(e.args[0])
