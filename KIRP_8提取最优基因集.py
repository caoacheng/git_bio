# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 15:29:03 2017

@author: Administrator
"""

# -*- coding: utf-8 -*-
import pandas as pd
import os

  
if __name__=='__main__': 
    path=os.getcwd()
    print ("开始处理")
    filename='Methylation Beta Value4.0.1.txt'
    data= pd.read_csv(filename,sep='\t',index_col=0)
    data=data.T
    data1=data.ix[:,:3]
    target=data.ix[:,-1]
    data=pd.concat([data1,target],axis=1)
    os.chdir(path)
    print ("保存数据")
    data.T.to_csv('Methylation Beta Value8.txt',sep='\t',header=True,index=True)
