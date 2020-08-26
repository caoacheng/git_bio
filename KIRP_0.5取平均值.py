# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 17:32:22 2017
14975个基因
@author: Administrator
"""
import numpy as np
import datetime
import pandas as pd
s_time=datetime.datetime.now()
print "开始读取数据。。。。。"        
data = pd.read_csv("Methylation Beta Value0.4.txt",sep='\t',index_col=0)
del data['Chromosome']
data=data.T
gene=list(data)
gene1=list(set(gene))
gene1.sort(key=gene.index)
print "正在计算平均值"
m=0
for x in gene1:
    gene2=[]
    for i in range(len(data[x])):
        gene2.append(np.average(data[x].ix[i]))
    data[x]=gene2
    if m%500==0:
        print "正在处理第"+str(m)+"个基因"
    m=m+1
#hang_index=list(data.index)
print "删除重复基因。。。。"
data=data.T

				    
data.to_csv("Methylation Beta Value0.5.txt",sep='\t',header=True,index=True)
e_time=datetime.datetime.now()
time=e_time-s_time
print "程序执行完成，共用时"+str(time)
print "保存完成"        
    
        
