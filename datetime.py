# -*- coding:utf-8-*-
import arcpy
import time
# import datetime
try:
    cursor = arcpy.da.InsertCursor(r'E:\苍穹软件\20171030_房屋\xy.shp', "SHAPE@")
    for x in range(0, 25):
        cursor.insertRow([x])
    del cursor
except arcpy.ExecuteError:
    print arcpy.GetMessages()

    
    