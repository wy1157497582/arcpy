import arcpy;
from arcpy import env
env.workspace=u'F:\第三批数据\GEOdata\Jn.mdb\wei2'
fcs = arcpy.ListFields()
for fc in fcs:
    arcpy.Delete_management(fc)
    

