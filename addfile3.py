
import arcpy
import os
# ���뵱ǰ��ͼ�ĵ�
mymxd =arcpy.mapping.MapDocument("current")
ary =arcpy.mapping.ListLayers(mymxd)
fieldname=["BSM","DKMC","DKXH","ZDZL","DKDZ","DKXZ","DKNZ","DKBZ","SYQXZ","CBJYQZBM","SCMJM","SCMJ","SFJBNT","HTMJ","ELYBMJM","ELYBMJ","TDLYLX","TDYT","DLDJ","CBFMC","CBFBM","DKLB"]
aliasname=["��ʶ��","�ؿ�����","�ؿ����","�ڵ�����","�ؿ鶫��","�ؿ�����","�ؿ�����","�ؿ鱱��","����Ȩ����","�а���ӪȨ����","ʵ�����(Ķ)","ʵ�����","�Ƿ����ũ��","��ͬ���","�����Ӱ������Ķ��","�����Ӱ����","������������","������;","�����ȼ�","�а�������","�а�������","�ؿ����"]
def AddNewField2(in_table,fieldname):
    zidian ={}
    # #fieldname=["BSM","DKMC","DKXH","ZDZL","DKDZ","DKXZ","DKNZ","DKBZ","SYQXZ","CBJYQZBM","SCMJM","SCMJ","SFJBNT","HTMJ","ELYBMJM","ELYBMJ","TDLYLX","TDYT","DLDJ","CBFMC","CMFBM","DKLB"]
    # aliasname=["��ʶ��","�ؿ�����","�ؿ����","�ڵ�����","�ؿ鶫��","�ؿ�����","�ؿ�����","�ؿ鱱��","����Ȩ����","�а���ӪȨ����","ʵ�����(Ķ)","ʵ�����","�Ƿ����ũ��","��ͬ���","�����Ӱ������Ķ��","�����Ӱ����","������������","������;","�����ȼ�","�а�������","�а�������","�ؿ����"]
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












