#-*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import pandas as pd
import datetime
import numpy as np





def write_list_to_file(filename,myList):
    matrix_a = np.array(myList)
    np.savetxt(filename,matrix_a,fmt=['%s']*matrix_a.shape[1],delimiter='\t',newline='\n')

def oneway_deal(data):
    lieshu = 0
    col=list(data)[:-1]
    gene=[]
    print len(col)/2
    for xx in range(len(col)/2):
        cor = abs(data.ix[:,xx+xx].corr(data.ix[:,xx+xx+1],method='pearson'))
        #cor = abs(data['stage'].corr(data[xx]))
        if lieshu%100==0:print cor
        lieshu = lieshu + 1
        if cor>=0.5:
            gene.append(xx+xx)
    print gene
    return gene


   
if __name__ == '__main__':
    s_time=datetime.datetime.now()
    print "正在读取数据。。。。"
    data_new=pd.read_csv("Methylation Beta Value1.4.txt",sep='\t',index_col=0)
    data= data_new.T
    gene= oneway_deal(data)
    print len(gene)-1
    
    ma=[]
    with open("Methylation Beta Value1.4.txt",'r') as f:
         for line in f.readlines():
             line = line.strip('\n')
             data1 = line.split("\t")
             coll=len(data1)
             ma.append(data1)
    rows=len(gene)+2
    cols=coll
    myList = [([0] * cols) for i in range(rows)]
    myList[0]=ma[0]
    myList[-1]=ma[-1]
    
    n=1         
    for a in gene:
        myList[n]=ma[a+1]
        n=n+1

    filename='Methylation Beta Value1.5.txt'
    write_list_to_file(filename,myList)
    e_time=datetime.datetime.now()
    use_time=e_time-s_time
    print "共耗时%s"%(str(use_time))
'''
共有基因399
'''
