# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 13:23:17 2017

@author: Administrator
"""

import sklearn.datasets  
import sklearn.linear_model   
import pandas as pd
import numpy as np 
from sklearn.metrics import mean_squared_error
from sklearn.cross_validation import train_test_split

def loaddata(filename):
    data= pd.read_csv(filename,sep='\t',index_col=0)
    return data

def read_data(filename):
    data= pd.read_csv(filename,sep='\t',index_col=0)
    data=data.T
    data1=data.ix[:,:-1]
    target=data[data.columns[-1]]
    return data,data1,target 
#def tiqu(n):
if __name__ == "__main__":   
    filename='Methylation Beta Value6.1.txt'
    data,data1,target=read_data(filename)

#    x_train,x_test,y_train,y_test=train_test_split(data1,target,test_size=0.2,random_state=33)
    enets =sklearn.linear_model.ElasticNetCV(alphas = np.logspace(-5, 1, 60),max_iter=5000,cv=5)
    enet=enets.fit(data1, target)
    print("Alpha = ", enet.alpha_)  
    print("L1 Ratio = ", enet.l1_ratio_)
    gongxian=[]
    rs={}
    for x in enet.coef_:
        if x!=0:
            gongxian.append(x) 
    print len(gongxian)
    data2=data.ix[:,enet.coef_!=0]#回归系数!=0的特征，被提取得到
    state=list(data2).append('cancer')
    data2.reindex(columns=state)
    data2['cancer']=data['cancer']
    
    for i in range(len(gongxian)):
        rs[gongxian[i]]=i
    re=sorted(rs.iteritems(), key=lambda x : abs(x[0]), reverse=True)
    
    
    baoliu=[]
    for x in re:
        baoliu.append(x[1])
    print baoliu,len(baoliu)
    data3=data2.ix[:,baoliu]
    state=list(data3).append('cancer')
    data3.reindex(columns=state)
    data3['cancer']=data['cancer']
    print data3.columns   
    data3.T.to_csv('Methylation Beta Value6.2.txt',sep='\t',header=True,index=True)
#if __name__ == "__main__": 
#    for i in range(10):
#        print "正在提取前"+str(i+1)+"个基因........"
#        tiqu(i+1) 
#        i=i+1
'''

'''
