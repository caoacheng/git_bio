# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 21:07:02 2017
29144个基因
@author: Administrator
"""

import numpy as np
#from pandas import DataFrame as df
import datetime
s_time=datetime.datetime.now()
data=[]
with open("Methylation Beta Value0.6.txt",'r') as f:
    for line in f.readlines():
        line = line.strip('\n')
        data.append(line)
print len(data)
data1=list(set(data))
data1.sort(key=data.index)
print len(data1)
data2=[]
for x in data1:
    xx=x.split('\t')
    data2.append(xx)
#print data2[0:10]
matrix_a = np.array(data2)
np.savetxt("Methylation Beta Value0.7.txt",matrix_a,fmt=['%s']*matrix_a.shape[1],delimiter='\t',newline='\n')
#    
print "保存完成。。。。。。。"
e_time=datetime.datetime.now()
time=e_time-s_time
print "程序执行完成，共用时"+str(time)
'''
23063
'''
