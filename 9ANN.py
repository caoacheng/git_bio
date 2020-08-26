#-*- coding: utf-8 -*-
import os
import pandas as pd

from sklearn.cross_validation import StratifiedKFold
from sklearn import metrics
import numpy as np
from sklearn.preprocessing import label_binarize
import datetime
from sklearn.cross_validation import KFold
from sklearn.metrics import confusion_matrix
from numpy.random import seed
seed(1234)


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

#def read_data1(filename):
#    data= pd.read_csv(filename,sep='\t',index_col=0)
#    data1=data[data.columns[:-1]]
#    target=data[data.columns[-1]]
#    return data1,target

def read_data1(filename):
    print ('reading data...')
    data_old = pd.read_csv(filename,sep='\t',index_col=0)            
    data = data_old.as_matrix() #将表格转换为矩阵
    X = data[:,:-1]
    Y = data[:,-1]
    return X,Y
def cross_v():

    print "LOADing data......"

    filename = "Methylation Beta Value6.2.txt"
    get_xunliandata(filename)
    filename1='sample_train.txt'
    
    X,Y = read_data1(filename1)  #读取数据        
    acc=[]
    mcc=[]
    sen=[]
    spe=[]
    from keras.models import Sequential #导入神经网络初始化函数
    from keras.layers.core import Dense, Activation #导入神经网络层函数、激活函数

    #使用6折交叉验证，并且画ROC曲线  
    cv = StratifiedKFold(Y, n_folds=6)
#    cv = KFold(len(Y), n_folds=6)
    for train, test in cv:
      net = Sequential() #建立神经网络
      net.add(Dense(input_dim = X.shape[1], output_dim = 1000)) #添加输入层（3节点）到隐藏层（10节点）的连接
      net.add(Activation('relu')) #隐藏层使用relu激活函数
      net.add(Dense(input_dim = 1000, output_dim = 2)) #添加隐藏层（10节点）到输出层（1节点）的连接
      net.add(Activation('softmax')) #输出层使用sigmoid激活函数
 #     net.add(Activation('svm'))
      net.compile(loss = 'categorical_crossentropy', optimizer = 'adam') #编译模型，使用adam方法求解

      from keras.utils.np_utils import to_categorical   #将类别转换为二进制数，以便使用损失函数
      y_train_6 = to_categorical(Y[train],2)
      net.fit(X[train], y_train_6, nb_epoch=15, batch_size=5) 
      test_yp = net.predict_classes(X[test]).reshape(len(X[test])) #预测结果变形
      #这里要提醒的是，keras用predict给出预测概率，predict_classes才是给出预测类别，而且两者的预测结果都是n x 1维数组，而不是通常的 1 x n
      
      cm = confusion_matrix(Y[test],test_yp)
      TP = cm[0][0]
      FP = cm[0][1]
      FN = cm[1][0]
      TN = cm[1][1]
      SEN = TP/float((TP+FN))
      SPE = TN/float((FP+TN))
      ACC = metrics.accuracy_score(Y[test],test_yp)
      MCC = metrics.matthews_corrcoef(Y[test],test_yp)
      acc.append(ACC)
      mcc.append(MCC)
      sen.append(SEN)
      spe.append(SPE) 
    print "The average acc....%s,mcc.....%s,sen.....%s,spe.....%s"%(str(np.mean(acc)),str(np.mean(mcc)),str( np.mean(sen)),str(np.mean(spe)))
    return SEN,SPE,ACC,MCC
    
    
def aver():
    n=20
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
    print "平均敏感性：%s...%s...........特异性：%s...%s"%(str(np.mean(se)),str(np.std(se)),str(np.mean(sp)),str(np.std(sp)))
    print "平均ACC值为：%s...%s...............MCC值为：%s...%s"%(str(np.mean(acc)),str(np.std(acc)),str(np.mean(mcc)),str(np.std(mcc)))
    
if __name__=='__main__': 
   aver()


'''
平均敏感性：1.0...0.0...........特异性：1.0...0.0
平均ACC值为：1.0...0.0...............MCC值为：1.0...0.0
'''
