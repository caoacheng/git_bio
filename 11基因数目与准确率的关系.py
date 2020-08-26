# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 15:29:03 2017

@author: Administrator
"""

# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from sklearn import svm
from sklearn import metrics
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict
from sklearn.cross_validation import StratifiedKFold
from sklearn.cross_validation import KFold
#from random import shuffle
def dataT(filename):
    data= pd.read_csv(filename,sep='\t',index_col=0)
    filenameT="value_translate.txt"
    data.T.to_csv(filenameT,sep='\t',header=True,index=True)
    return filenameT
def get_xunliandata(filename): #只针对一个数据集的下采样
    data1,target=read_data(filename) #加载数据
    pos_num = 0; pos_indexs = []; neg_indexs = []   
    for i in range(len(target)):#统计正负样本的下标    
        if target[i] == 0.0:
            pos_num +=1
            pos_indexs.append(i)
            continue
        neg_indexs.append(i)
    np.random.shuffle(neg_indexs)
    neg_indexs = neg_indexs[0:pos_num]
    filenameT=dataT(filename)
    fr = open(filenameT, 'r')
    files = fr.readlines()
    onefile=[]
    for i in range(len(files)):
        onefile.append( files[i].strip('\n').split('\t'))
    outfile = []
    outfile.append(onefile[0])
    for i in range(pos_num):
        pos_line = onefile[pos_indexs[i]+1]    
        outfile.append(pos_line)
        neg_line= onefile[neg_indexs[i]+1]      
        outfile.append(neg_line)   
    array1=np.array(outfile)
    np.savetxt('sample_train.txt',array1,fmt="%s", delimiter='\t')
def read_data(filename):
    data= pd.read_csv(filename,sep='\t',index_col=0)
    data=data.T
    data1=data[data.columns[:-1]]
    target=data[data.columns[-1]]
    return data1,target,  
def read_data1(filename):
    data= pd.read_csv(filename,sep='\t',index_col=0)
    data1=data[data.columns[:-1]]
    target=data[data.columns[-1]]
    return data1,target
def cross_v(n):
#    filename ="Methylation Beta Value4.5.txt"
    filename = "Methlytion5."+str(n)+".txt"#交集（2和0.2）
#    filename='gene express file3.txt'
#    get_xunliandata(filename)
#    filename1='sample_train.txt'
    data1,target=read_data(filename)
    clf = svm.SVC(kernel='linear')
#    cv=KFold(len(target),n_folds=6)
    cv=StratifiedKFold(target,n_folds=6)
    y_p = cross_val_predict(clf, data1, target, cv=cv)
#    y_3 = cross_val_score(clf, data1, target, cv=6)
#    print y_3
    cm = confusion_matrix(target,y_p)    
    TP = cm[0][0]
    FP = cm[0][1]
    FN = cm[1][0]
    TN = cm[1][1]
    SEN = TP/float((TP+FN))
    SPE = TN/float((FP+TN))
    ACC = metrics.accuracy_score(target, y_p)
    MCC = metrics.matthews_corrcoef(target, y_p)
#    print classification_report(target,y_p)
#    print 'ACC值为：%s...............MCC值为：%s'%(str(ACC),str(MCC))
#    print '敏感性为：%s..............特异性为：%s'%(str(SEN),str(SPE))
    return ACC
def aver():
    n=1
    se=[]
    sp=[]
    acc=[]
    mcc=[] 
    for i in range(n):
        SEN,SPE,ACC,MCC=cross_v()
        se.append(SEN)
        sp.append(SPE)
        acc.append(ACC)
        mcc.append(MCC)
    print "平均ACC值为：%s...%s...............MCC值为：%s...%s"%(str(np.mean(acc)),str(np.std(acc)),str(np.mean(mcc)),str(np.std(mcc)))
    print "平均敏感性：%s...%s...........特异性：%s...%s"%(str(np.mean(se)),str(np.std(se)),str(np.mean(sp)),str(np.std(sp)))    
if __name__=='__main__': 
    ACC={}
    for n in range(65):
        print "正在计算第"+str(n+1)+"个基因"
        acc=cross_v(n+1)
        ACC[(n+1)]=acc
#    print ACC
    re=sorted(ACC.iteritems(), key=lambda x : abs(x[0]), reverse=False)
    print re
'''   
[(1, 0.98598130841121501), (2, 0.99065420560747663), (3, 0.99065420560747663), (4, 0.99065420560747663), (5, 0.99532710280373837), 
(6, 0.99532710280373837), (7, 0.99532710280373837), (8, 0.99065420560747663), (9, 0.99065420560747663), (10, 0.99065420560747663),
(11, 0.99065420560747663), (12, 0.99532710280373837), (13, 0.99532710280373837), (14, 0.99532710280373837), (15, 0.99532710280373837), 
(16, 0.99532710280373837), (17, 0.99532710280373837), (18, 0.99532710280373837), (19, 0.99532710280373837), (20, 0.99532710280373837),
 (21, 0.99532710280373837), (22, 0.99532710280373837), (23, 0.99532710280373837), (24, 0.99532710280373837), (25, 0.99532710280373837), 
 (26, 0.99532710280373837), (27, 0.99532710280373837), (28, 0.99532710280373837), (29, 0.99532710280373837), (30, 0.99532710280373837),
 (31, 0.99532710280373837), (32, 0.99532710280373837), (33, 0.99532710280373837), (34, 0.99532710280373837), (35, 0.99532710280373837),
 (36, 0.99532710280373837), (37, 0.99532710280373837), (38, 0.99532710280373837), (39, 0.99532710280373837), (40, 0.99532710280373837), 
 (41, 0.99532710280373837), (42, 0.99532710280373837), (43, 0.99532710280373837), (44, 0.99532710280373837), (45, 0.99532710280373837), 
 (46, 0.99532710280373837), (47, 0.99532710280373837), (48, 0.99532710280373837), (49, 0.99065420560747663), (50, 0.99532710280373837), 
 (51, 0.99532710280373837), (52, 0.99065420560747663), (53, 0.99065420560747663), (54, 0.99532710280373837), (55, 0.99532710280373837), 
 (56, 0.99532710280373837), (57, 0.99532710280373837), (58, 0.99532710280373837), (59, 0.99532710280373837), (60, 0.99532710280373837),
 (61, 0.99065420560747663), (62, 0.99532710280373837), (63, 0.99065420560747663), (64, 0.99532710280373837), (65, 0.99532710280373837)]        
'''
