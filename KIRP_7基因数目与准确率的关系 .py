# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 15:29:03 2017

@author: Administrator
"""

# -*- coding: utf-8 -*-
import pandas as pd
from sklearn import svm
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_predict
from sklearn.cross_validation import StratifiedKFold
import os
#from random import shuffle


def read_data(filename,n):
    data= pd.read_csv(filename,sep='\t',index_col=0)
    data=data.T
    data1=data.ix[:,:n]
    target=data.ix[:,-1]
    data=pd.concat([data1,target],axis=1)  
    data2=data[data.columns[:-1]]
    target2=data[data.columns[-1]]
    return data2,target2,  
def cross_v(n):
    filename='Methylation Beta Value4.0.1.txt'
#    filename = "Methylation Beta Value8."+str(n)+".txt"#交集（2和0.2）
    data1,target=read_data(filename,n)
    clf = svm.SVC(kernel='linear')
    cv=StratifiedKFold(target,n_folds=6)
    y_p = cross_val_predict(clf, data1, target, cv=cv)
    cm = confusion_matrix(y_p,target)
    TP = cm[0][0]
    FP = cm[0][1]
    FN = cm[1][0]
    TN = cm[1][1]
    SPE = TN/float((FP+TN))
    SEN = TP/float((TP+FN))
    ACC = metrics.accuracy_score(target, y_p)
    MCC = metrics.matthews_corrcoef(target, y_p)
    return ACC,SPE,MCC,SEN
  
if __name__=='__main__': 
    result={}
    for n in range(163):
        print ("正在计算第"+str(n+1)+"个基因")
        print n
        resul=[]
        acc,spe,mcc,sen=cross_v(n+1)
        resul.append(acc)
        resul.append(spe)
        resul.append(mcc)
        resul.append(sen)
        result[n+1]=resul        
        
    results_ACC=sorted(result.iteritems(), key=lambda x : x[1][0], reverse=False)
    print ("显示基因数目与ACC的关系")
    print (results_ACC)
'''
optimal is 165,[ACC,SPE,MCC,SEN]
3, [1.0, 1.0, 1.0,1.0]
'''    

