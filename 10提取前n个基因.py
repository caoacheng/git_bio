# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 13:23:17 2017

@author: Administrator
"""

import sklearn.datasets  
import sklearn.linear_model   
import pandas as pd
import numpy as np 
from sklearn.cross_validation import train_test_split

#def loaddata(filename):
#    data= pd.read_csv(filename,sep='\t',index_col=0)
#    return data

#def read_data(filename):
#    data= pd.read_csv(filename,sep='\t',index_col=0)
#    data=data.T
#    data1=data.ix[:,:-1]
#    target=data[data.columns[-1]]
#    return data,data1,target 
def readdata():  
    filename='Methlytion4.1-new.txt'
    data= pd.read_csv(filename,sep='\t',index_col=0)
    data=data.T
    
    return data
  
    
if __name__ == "__main__":
    data=readdata()
    n=len(list(data))-1
    for i in range(n):
        print "正在提取前"+str(i+1)+"个基因........"
        gene=list(data)[:i+1]
        gene.append('cancer')
        data1=data[gene]
        data1.T.to_csv('Methlytion5.'+str(i+1)+'.txt',sep='\t',header=True,index=True)
    
        
    
#    for i in range(10):
#        
#        tiqu(i+1) 
#        i=i+1
'''

'''
