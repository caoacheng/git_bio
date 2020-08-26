# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 17:32:22 2017

@author: Administrator
"""
import datetime
import numpy as np
s_time=datetime.datetime.now()
import pandas as pd
print "开始查找全零行。。。。。"
all_hang = 0
quan0_Num = 0
filename="Methylation Beta Value.txt"
i=0
with open(filename,'r') as f:
    for line in f.readlines():
        all_hang = all_hang + 1
        line = line.strip('\n')
        data = line.split("\t")
        lin=len(data)-1
        ling_num=0
        for xx in data[1:]:
            if xx == 'NA':
                ling_num=ling_num+1
        if ling_num > (lin*0.5):
            quan0_Num = quan0_Num + 1        
print "一共读取数据行数：{} ，其中出现缺失值>50%的探针数：{}".format(all_hang,quan0_Num)


rows=all_hang-quan0_Num
cols=lin+1
myList = [([0] * cols) for i in range(rows)]


print "删除全零行。。。。。" 
i=0
with open(filename,'r') as f:
    for line in f.readlines():
        all_hang = all_hang + 1
        line = line.strip('\n')
        data = line.split("\t")
        lin=len(data)-1
        ling_num=0
        for xx in data[1:]:
            if xx == 'NA':
                ling_num=ling_num+1
        if ling_num > (lin*0.5):
            quan0_Num = quan0_Num + 1
        else:
            myList[i]=data
            i=i+1
print "一共读取数据行数：{} ".format(i)


print "保存数据"
filename_out=filename.replace('.txt','0.1.txt')
matrix_a = np.array(myList)
np.savetxt(filename_out,matrix_a,fmt=['%s']*matrix_a.shape[1],delimiter='\t',newline='\n')


e_time=datetime.datetime.now()
time=e_time-s_time

print "程序执行完成，共用时"+str(time)      
    
        
