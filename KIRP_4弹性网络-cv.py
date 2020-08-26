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
    filename='Methylation Beta Value3.txt'
    data,data1,target=read_data(filename)

#    x_train,x_test,y_train,y_test=train_test_split(data1,target,test_size=0.2,random_state=33)
    enet =sklearn.linear_model.ElasticNetCV(alphas = np.logspace(-2, 2, 1000),l1_ratio=[.1,.3, .5, .7, .9, .95, .99, 1],max_iter=50000,cv=10,\
                                            n_alphas=100, n_jobs=1, normalize=False, positive=False,\
                                            precompute='auto', random_state=None, selection='cyclic',\
                                            tol=0.0001, verbose=0).fit(data1, target)
    scores=enet.score(data1,target)
    y=enet.predict(data1)

    gongxian=[]
    rs={}
    for x in enet.coef_:
        if x!=0:
            gongxian.append(x)         
    data2=data.ix[:,enet.coef_!=0]#回归系数!=0的特征，被提取得到
    #state=list(data2).append('cancer')
    #data2.reindex(columns=state)
    #data2['cancer']=data['cancer']
    
    for i in range(len(gongxian)):
        rs[gongxian[i]]=i
    re=sorted(rs.iteritems(), key=lambda x : abs(x[0]), reverse=True)
    
    
    baoliu=[]
    for x in re:
        baoliu.append(x[1])
    print("Alpha = ", enet.alpha_)  
    print("L1 Ratio = ", enet.l1_ratio_)
    print("score = ", scores)
    print("iter = ",enet.n_iter_)
    print('RMSE=',np.sqrt(mean_squared_error(target,y)))
    print '模型评价{}，特征个数{}'.format(scores,len(baoliu))

    data3=data2.ix[:,baoliu]
    #state=list(data3).append('cancer')
    #data3.reindex(columns=state)
    data_append=data['cancer'] 
    data4=pd.concat([data3,data_append],axis=1)
    filename1='Methylation Beta Value4.0.1.txt'
    data4.T.to_csv(filename1,sep='\t',header=True,index=True)


'''
('Alpha = ', 0.01)
('L1 Ratio = ', 0.10000000000000001)
('score = ', 0.9631650329877075)
('iter = ', 924)
('RMSE=', 0.078345027428791111)
模型评价0.963165032988，特征个数163
'''
