# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 21:07:02 2017

@author: Administrator
"""

import numpy as np
#from pandas import DataFrame as df
import pandas as pd
import datetime

value12=[]
with open("Methylation Beta Value3.2.txt",'r') as f:
    m=0
    for line in f.readlines():
        line = line.strip('\n')
        data = line.split("\t")
        coll=len(data)
        m=m+1
        value12.append(data)
        
file12=[]
with open("gene express file3.2.3.txt",'r') as f1:
    for lines in f1.readlines():
        lines=lines.strip('\n')
        datas=lines.split('\t')
        file12.append(datas)

print m,coll
rows=m+m-2
cols=coll
myList = [([0] * cols) for i in range(rows)]   


def write_list_to_file(filename):
    matrix_a = np.array(myList)
    np.savetxt(filename,matrix_a,fmt=['%s']*matrix_a.shape[1],delimiter='\t',newline='\n')
    
    
if __name__ == '__main__':
    s_time=datetime.datetime.now()
    i=1             
    myList[0]=value12[0]
    myList[-1]=value12[-1]
    print myList[0]
    print myList[-1]
    
    del value12[0]
    del file12[0]
    del value12[-1]
    del file12[-1]
    
    
    for x in value12:
        for xx in file12:
            if x[0]==xx[0]:
                myList[i]=x
                myList[i+1]=xx
                print "正在处理第"+str(i)+"行......"
                print "正在处理第"+str(i+1)+"行......"
                i=i+2
                break             
    
    
#    col=myList[0][1:]
#    indes=[] 
#    del myList[0] 
#    for x in myList:
#        indes.append(x[0])
#        del x[0]
#        
#    data=df(myList,index=indes,columns=col)  
#    data.to_csv("Methylation Beta Value1.3.txt",sep='\t',header=True,index=True)

    
    write_list_to_file("Methylation Beta Value3.3.txt") 
#    data=pd.read_csv("Methylation Beta Value1.3.txt",sep='\t',index_col=0)
#    data=data.T
#    del data['0']
#    data.T.to_csv("Methylation Beta Value1.3.txt",sep='\t',header=True,index=True)
##    
    print "保存完成。。。。。。。"
    e_time=datetime.datetime.now()
    time=e_time-s_time
    print "程序执行完成，共用时"+str(time)
'''

'''