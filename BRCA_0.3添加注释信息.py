# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 21:07:02 2017

@author: Administrator
"""

import pandas as pd
from pandas import DataFrame as df
import datetime
import os

with open("Methylation Beta Value0.2.1.txt",'r') as f:
    m=0
    for line in f.readlines():
        line=line.split("\t")
        coll=len(line) 
        m=m+1
print m,coll

rows=m
cols=coll+1+1+1
myList = [([0] * cols) for i in range(rows)]   
    

if __name__ == '__main__':
    s_time=datetime.datetime.now()
    i=1
    value12=[]
    with open("Methylation Beta Value0.2.1.txt",'r') as f:
         for line in f.readlines():
             line = line.strip('\n')
             data = line.split("\t")
             value12.append(data)

    file12=[]
    with open("biaohao.txt",'r') as f1:
         for lines in f1.readlines():
             lines=lines.strip('\n')
             datas=lines.split('\t')
             file12.append(datas)
             
    myList[0][:-3]=value12[0]
    myList[0][-3]=file12[0][2]#chr
    myList[0][-2]=file12[0][5]#gene_name
    myList[0][-1]=file12[0][8]#TSS 
    del value12[0]
    del file12[0]

    print myList[0]         
    for x in value12:
        for xx in file12:
            if x[0]==xx[0]:
                myList[i][:-3]=x
                myList[i][-3]=xx[2]
                myList[i][-2]=xx[5]
                myList[i][-1]=xx[8]
                if (i%1000==0):
                    print "正在处理第"+str(i)+"行......"
                    print len(myList[i])
                i=i+1
                break
                
    myList[i][:-3]=value12[-1]
    myList[i][-3]='na'
    myList[i][-2]='na'
    myList[i][-1]='na'

    col=myList[0][1:]
    indes=[] 
    del myList[0] 
    for x in myList:
        indes.append(x[0])
        del x[0]        
    data=df(myList,index=indes,columns=col)  
    
    data.to_csv("Methylation Beta Value0.3.txt",sep='\t',header=True,index=True)
#    data= pd.read_csv("Methylation Beta Value0.1.txt",sep='\t',index_col=0)
#    data=data.T
#    del data['0']
#    data.T.to_csv("Methylation Beta Value0.1.txt",sep='\t',header=True,index=True)
    print "保存完成。。。。。。。"
    e_time=datetime.datetime.now()
    time=e_time-s_time
    print "程序执行完成，共用时"+str(time)
'''

'''
