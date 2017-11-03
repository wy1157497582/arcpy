# -*- coding: utf-8 -*-
import arcpy
import fileinput


shp=r'C:\myFile\develop\python\addFiledAndsetXY\yichuxing.shp'
filed=["date","time","value","lon","lat","SHAPE@"]
cursor = arcpy.da.InsertCursor(shp, (filed))
file=r'C:\myFile\develop\python\addFiledAndsetXY\yichuxing.txt'
count=0
for point in fileinput.input(file):
    #date
    date=point.split(" ")[0]
    # time
    time=point.split(" ")[1].split(",")[0]
    #value
    value=point.split(" ")[1].split(",")[3]
    lon=point.split(" ")[1].split(",")[1]
    lat=point.split(" ")[1].split(",")[2]
    p=arcpy.Point(lon,lat)
    cursor.insertRow((date,time,value,lon,lat,p))
    print date,time,value,lon,lat,p
    count+=1
del cursor
print count,"条记录"



