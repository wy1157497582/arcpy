import arcpy, string, math
from arcpy import env
env.overwriteOutput = True
env.workspace = r"F:/China_1km.gdb"
# Change to the absolute directory of China_1km.gdb


ln = "Grids1km"
POIs = "Flickr_Photos_China"    # Change to the Name of the provided dataset
prov = "B_Provinces"

print ("Reading province list")
lstCODE=[]
dictNAME={}
cur = arcpy.SearchCursor(prov)
row = cur.next()
while row:
    if row.PROV_ID not in lstCODE: 	
        lstCODE.append(str(row.PROV_ID)) 
	dictNAME[str(row.PROV_ID)]=str(row.Name_ENG)				
    row = cur.next()
del row, cur

# lstCODE = ['1']  # for test only
lenP = len(lstCODE) # the length of province
k = 1
 
for P in lstCODE:
    print "Now "+ dictNAME[P] + " " + P + "  " + str(k) + "/" + str(lenP) 	
    print "...selecting parcels"
    fc = "PCL"+P								
    sql = "PROV_ID = "+P 							
    arcpy.MakeFeatureLayer_management(ln,"lyr_ln") 
    arcpy.SelectLayerByAttribute_management("lyr_ln","NEW_SELECTION",sql)
    arcpy.CopyFeatures_management("lyr_ln", fc)
    arcpy.RefreshCatalog(env.workspace)
    arcpy.RepairGeometry_management(fc)

    print "...selecting POIs"
    poi = "POI"+P
    sql = "PROV_ID = "+P
    arcpy.MakeFeatureLayer_management(POIs,"lyr_poi")
    arcpy.SelectLayerByAttribute_management("lyr_poi","NEW_SELECTION",sql)
    arcpy.CopyFeatures_management("lyr_poi", poi)
    arcpy.RefreshCatalog(env.workspace)
    arcpy.RepairGeometry_management(poi)

    print "...spatial joining"
    fc_jn = fc+"_jn"
    arcpy.SpatialJoin_analysis(fc, poi, fc_jn, "#", "#", "#", "CONTAINS")
    arcpy.RefreshCatalog(env.workspace)
    arcpy.RepairGeometry_management(fc_jn)
    k+=1
print "Spatial Join Finished."

print("Now appending...")
arcpy.CreateFeatureclass_management(env.workspace, "Appended_PCL_jn", "POLYGON", "PCL2_jn")
fcs = arcpy.ListFeatureClasses("PCL*_jn")
print("Feature Classes to be appended:"+str(fcs))
arcpy.Append_management(fcs, "Appended_PCL_jn", "NO_TEST")
print("Appending finished.")

print("All Finished.")



