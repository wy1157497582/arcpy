#-*- coding:utf-8-*-
import arcpy,os  
inPath = u"F:\第四批数据\beizh\ls.mdb"  
arcpy.env.workspace = inPath  
arcpy.env.overwriteoutput=1  
outPath =u"F:"
outName = "dian.mdb"  
try:
  
#'''''复制要素类函数'''  
  def copyAll(outPath,outName):  
    for fc in arcpy.ListFeatureClasses():  
    #print(" Feature Class: {0}".format(fc))  
      arcpy.FeatureClassToFeatureClass_conversion(fc, outPath , os.path.splitext(fc)[0])  
    #iFeatureClassFull = None  
#[python] view plain copy print?在CODE上查看代码片派生到我的代码片
#输出路径1，直接将原数据库中的要素类输出到新的数据库中  
  outPath1 = outPath + os.sep + outName  
  arcpy.CreateFileGDB_management(outPath, outName)  
  copyAll(outPath1, outName) 
  for iFD in arcpy.ListDatasets("","Feature"):  
    #print("Feature Dataset {0}:".format(iFD))  
    desc = arcpy.Describe(iFD)  
    sr = desc.spatialReference  
    arcpy.CreateFeatureDataset_management(outPath1, iFD , sr)  
  #更改工作空间  
    arcpy.env.workspace = inPath + r"/" + str(iFD)  
  #输出路径2，将原数据库要素数据集中的要素类输出到新数据库要素数据集中  
  #outPath2 = outPath1 + r"/" + str(iFD)  
  #copyAll(outPath2, outName)  
  #更改工作空间  
  #arcpy.env.workspace = inPath  
except arcpy.ExecuteError:
   print(arcpy.GetMessages())