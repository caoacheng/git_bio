# -*- coding: utf-8 -*-
"""
合并后有基因3421

@author: Administrator
"""

import pandas as pd
import numpy as np
import os
curpath=os.getcwd()
data= pd.read_csv("Methylation Beta Value1.5.txt",sep='\t',index_col=0)
data=data.T
columns=list(data)
del columns[-1]


data1= pd.read_csv("Methylation Beta Value2.2.txt",sep='\t',index_col=0)
data1=data1.T
columns1=list(data1)

data2= pd.read_csv("Methylation Beta Value0.6.txt",sep='\t',index_col=0)
data2=data2.T

colu=columns+columns1
col=list(set(colu))
col.sort(key=colu.index)
print len(col)


data2=data2[col] 
data2.T.to_csv("Methylation Beta Value3.txt",sep='\t',header=True,index=True)               
    
            
        
        
        

    
