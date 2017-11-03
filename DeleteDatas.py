import arcpy;
import os
from arcpy import env
env.workspace=r'F:\第三批数据\esri shp\zhengku\Ju1.gdb'
fcs = arcpy.ListDatasets("")
for fc in fcs:
     print fc 
    #arcpy.Delete_management(fc)
	
	
    
