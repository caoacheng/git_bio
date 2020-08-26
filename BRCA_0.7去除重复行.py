# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 21:07:02 2017
22794个基因
@author: Administrator
"""

import numpy as np
import pandas as pd
#from pandas import DataFrame as df
import datetime
s_time=datetime.datetime.now()
print '删除TSS列和CGI列'
data0 = pd.read_csv("Methylation Beta Value0.6.txt",sep='\t',index_col=0)
del data0['Position_to_TSS']

data0.to_csv("Methylation Beta Value0.6.txt",sep='\t',header=True,index=True)
print '开始执行删除任务'
data=[]
with open("Methylation Beta Value0.6.txt",'r') as f:
    for line in f.readlines():
        line = line.strip('\n')
        data.append(line)
print len(data)
print '删除重复行'
data1=list(set(data))
data1.sort(key=data.index)
print len(data1)
data2=[]
for x in data1:
    xx=x.split('\t')
    data2.append(xx)
#print data2[0:10]
print '保存数据'
matrix_a = np.array(data2)
np.savetxt("Methylation Beta Value0.7.txt",matrix_a,fmt=['%s']*matrix_a.shape[1],delimiter='\t',newline='\n')
#    
print "保存完成。。。。。。。"
e_time=datetime.datetime.now()
time=e_time-s_time
print "程序执行完成，共用时"+str(time)
'''

'''
