# -*- coding: utf-8 -*-
"""
合并后有基因1270

@author: Administrator
"""
import os
import pandas as pd

data= pd.read_csv("Methylation Beta Value1.5.txt",sep='\t',index_col=0)
data=data.T
columns=list(data)

data1= pd.read_csv("Methylation Beta Value1.4.txt",sep='\t',index_col=0)
data1=data1.T
columns1=list(data1)


data2=data1[columns] 
data2.T.to_csv("Methylation Beta Value1.6.txt",sep='\t',header=True,index=True)               
    
            
        
        
        

    
