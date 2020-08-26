# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 17:32:22 2017

@author: Administrator
"""
import pandas as pd
print "开始查找全零行。。。。。"
data= pd.read_csv("Methylation Beta Value3.3.txt",sep='\t',index_col=0)
data=data.T
del data['0']
data.T.to_csv("Methylation Beta Value3.4.txt",sep='\t',header=True,index=True) 

print "保存完成"        
    
        