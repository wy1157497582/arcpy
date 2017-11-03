# -*- coding: utf-8 -*-
    '''
    删除数据集下面空的要素
    '''
    import sys, os
    import arcpy
    def clear_feature(feature):
        '''
        如果要素存在，则删除
        '''
        if arcpy.Exists(feature):
            try:            
                arcpy.Delete_management(feature)            
            except :
                print "The feature " + feature + " can not be deleted."
                # sys.exit()
            print('Delteed:' + feature)
    def is_null_feature(infea):
        '''
        判断是否是空的要素
        '''
        rows = arcpy.SearchCursor(infea)
        row = rows.next()
        if row:
            return False
        else:
            return True
    def del_null_feature(infea):
        if arcpy.Exists(infea):
            pass
        else:
            return 0
        if is_null_feature(infea) == True:
            clear_feature(infea)
    if __name__ == '__main__':
        inws = sys.argv[1]
        arcpy.env.workspace = inws
        feas = arcpy.ListFeatureClasses()
        for fea in feas:
            infea = os.path.join(inws, fea)
            del_null_feature(infea)