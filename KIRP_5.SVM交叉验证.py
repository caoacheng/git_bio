# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 15:29:03 2017

@author: Administrator
"""

# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from sklearn.svm import LinearSVC
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

def cm_plot(y, yp):
  from sklearn import metrics
  
  from sklearn.metrics import confusion_matrix #导入混淆矩阵函数

  cm = confusion_matrix(y, yp) #混淆矩阵
  
  import matplotlib.pyplot as plt #导入作图库
  plt.matshow(cm, cmap=plt.cm.Greens) #画混淆矩阵图，配色风格使用cm.Greens，更多风格请参考官网。
  plt.colorbar() #颜色标签
  
  for x in range(len(cm)): #数据标签
    for y in range(len(cm)):
      plt.annotate(cm[x,y], xy=(x, y), horizontalalignment='center', verticalalignment='center')
  
  plt.xlabel('True label') #坐标轴标签
  plt.ylabel('Predicted label') #坐标轴标签
  plt.savefig('cm-brca.jpg')
  plt.show()

  
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


def cross_v():
#    filename ="Methylation Beta Value4.5.txt"
    filename = "Methylation Beta Value4.0.1.txt"#交集（2和0.2）
#    filename='gene express file3.txt'
    #get_xunliandata(filename)
    #filename1='sample_train.txt'
    data1,target=read_data(filename)
#    data1,target=read_data(filename)
#    clf = svm.SVC(kernel='linear')
    clf=LinearSVC()
#    cv=KFold(len(target),n_folds=6)
    cv=StratifiedKFold(target,n_folds=6)
    y_p = cross_val_predict(clf, data1, target, cv=cv)
#    cm_plot(target, y_p)
#    y_3 = cross_val_score(clf, data1, target, cv=6)
#    print y_3
    cm = confusion_matrix(y_p,target)    
    TP = cm[0][0]
    FP = cm[0][1]
    FN = cm[1][0]
    TN = cm[1][1]
    SEN = TP/float((TP+FN))
    SPE = TN/float((FP+TN))
    ACC = metrics.accuracy_score(target, y_p)
    MCC = metrics.matthews_corrcoef(target, y_p)
    print classification_report(target,y_p)
    print 'ACC值为：%s...............MCC值为：%s'%(str(ACC),str(MCC))
    print '敏感性为：%s..............特异性为：%s'%(str(SEN),str(SPE))
    return SEN,SPE,ACC,MCC

def aver():
    n=10
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
   #aver()
    SEN,SPE,ACC,MCC=cross_v()


'''
             precision    recall  f1-score   support

        0.0       1.00      1.00      1.00        45
        1.0       1.00      1.00      1.00       168

avg / total       1.00      1.00      1.00       213

ACC值为：1.0...............MCC值为：1.0
敏感性为：1.0..............特异性为：1.0

'''
