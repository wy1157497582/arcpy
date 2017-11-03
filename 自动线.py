import arcpy
def fun(arg):
   arr =arg.getPath(0)
   arr.insert(arr.count,arg.getObject(0))
   geo=arcpy.polyline(arr)
   return geo