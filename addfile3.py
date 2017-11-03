
import arcpy
import os
# 引入当前地图文档
mymxd =arcpy.mapping.MapDocument("current")
ary =arcpy.mapping.ListLayers(mymxd)
fieldname=["BSM","DKMC","DKXH","ZDZL","DKDZ","DKXZ","DKNZ","DKBZ","SYQXZ","CBJYQZBM","SCMJM","SCMJ","SFJBNT","HTMJ","ELYBMJM","ELYBMJ","TDLYLX","TDYT","DLDJ","CBFMC","CBFBM","DKLB"]
aliasname=["标识码","地块名称","地块序号","宗地坐落","地块东至","地块西至","地块南至","地块北至","所有权性质","承包经营权编码","实测面积(亩)","实测面积","是否基本农田","合同面积","二轮延包面积（亩）","二轮延包面积","土地利用类型","土地用途","地力等级","承包方名称","承包方编码","地块类别"]
def AddNewField2(in_table,fieldname):
    zidian ={}
    # #fieldname=["BSM","DKMC","DKXH","ZDZL","DKDZ","DKXZ","DKNZ","DKBZ","SYQXZ","CBJYQZBM","SCMJM","SCMJ","SFJBNT","HTMJ","ELYBMJM","ELYBMJ","TDLYLX","TDYT","DLDJ","CBFMC","CMFBM","DKLB"]
    # aliasname=["标识码","地块名称","地块序号","宗地坐落","地块东至","地块西至","地块南至","地块北至","所有权性质","承包经营权编码","实测面积(亩)","实测面积","是否基本农田","合同面积","二轮延包面积（亩）","二轮延包面积","土地利用类型","土地用途","地力等级","承包方名称","承包方编码","地块类别"]
    i= 0
    while i <=21:
         zidian[fieldname[i]]=aliasname[i]
         i=i+1
    for fn in fieldname:
            
             arcpy.AddField_management(in_table,fn,"TEXT")

for lyr in ary:
    in_table= lyr.dataSource
    if in_table.find(".shp") > 0:
          AddNewField2(in_table,fieldname)
    else:
          next
          
    arcpy.DeleteField_management(in_table,"Id")
del mymxd
arcpy.RefreshActiveView()












