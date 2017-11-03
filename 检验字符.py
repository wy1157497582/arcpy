#-*-coding:utf-8 -*-
__author__ = 'kikita'
import os,arcpy
import struct
dbf = 'E:\cs\4\Export_Output_4.dbf'
dat = open(dbf, 'rb').read(30)[29:]
id = struct.unpack('B', dat)[0]
print(id, hex(id))
print  u'恭喜你成功显示出来'

