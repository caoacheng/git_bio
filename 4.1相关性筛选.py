#-*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import pandas as pd
import datetime
import numpy as np

with open("Methylation Beta Value.txt",'r') as f:
    for line in f.readlines():
        line=line.split("\t")
        coll=len(line) #列数
      



def write_list_to_file(filename,myList):
    matrix_a = np.array(myList)
    np.savetxt(filename,matrix_a,fmt=['%s']*matrix_a.shape[1],delimiter='\t',newline='\n')

def oneway_deal(data):
    cor_fuhe_num =0
    lieshu = 0
    gene=[]
    for xx in range(len(list(data))):
        cor = abs(data['cancer'].corr(data.ix[:,xx],method='spearman'))
        if lieshu%100==0:print cor
        lieshu = lieshu + 1
        if cor>=0.5:
            cor_fuhe_num = cor_fuhe_num + 1
            gene.append(xx)
    print gene
    return gene

def getgene(suoyin,data):
    genes=list(data.columns[:-1])
    gene=[]
    for i in suoyin:
        gene.append(genes[i])
    return gene

   
if __name__ == '__main__':
    s_time=datetime.datetime.now()
    x=0
    n=0
    print "正在读取数据。。。。"
    data_old = pd.read_csv("Methylation Beta Value.txt",sep='\t',index_col=0)
    data= data_old.T
    gene= oneway_deal(data)
#    print RSN
    print len(gene)
    rows=len(gene)+1
    cols=coll
    myList = [([0] * cols) for i in range(rows)]   
    with open("Methylation Beta Value.txt",'r') as f:
         for line in f.readlines():
             line = line.strip('\n')
             data1 = line.split("\t")
             if x==0:
                 myList[n]=data1
                 n=n+1
             for a in gene:
                 if a+1==x:
                   myList[n]=data1
                   n=n+1
             x=x+1
             if n==rows-1:
                 myList[n]=data1
    filename='Methylation Beta Value4.1.txt'
    write_list_to_file(filename,myList)
    data1=pd.read_csv("Methylation Beta Value4.1.txt",sep='\t',index_col=0)
    genes=list(data1.T)                
    Gene=list(set(genes))
    Gene.sort(key=genes.index)
    print Gene
    print len(Gene)-1        
    e_time=datetime.datetime.now()
    use_time=e_time-s_time
    print "共耗时%s"%(str(use_time))
'''
共有基因4697
'''
