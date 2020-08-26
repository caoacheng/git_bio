# -*- coding: utf-8 -*-
"""
共有基因： 34016
"""

import pandas as pd
import datetime

def get_gene(filename):
    data1=pd.read_csv(filename,sep='\t',index_col=0)
    data=data1
    gene=[]
    genes=data['Gene_Symbol']
#    print genes
    for gene1 in genes:
        dat=gene1.split(';')
        for x in dat:
            gene.append(x)
#            print x
    print len(gene)
    gene_new=list(set(gene))
    gene_new.sort(key=gene.index)
    print gene[-1]
    print "共有基因：",str(len(gene_new)-1)
    return gene,data


def get_position(filename):
    data1=pd.read_csv(filename,sep='\t',index_col=0)
    data=data1
    gene=[]
    genes=data['Position_to_TSS']
#    print genes
    for gene1 in genes:
        dat=gene1.split(';')
        for x in dat:
            gene.append(x)
    return gene

    

def get_weidian(filename1):   
    data1=pd.read_csv(filename1,sep='\t',index_col=0)
    data_new=data1[data1.columns[-2]]
    changdu=[]
    for genes in data_new:
        gene=genes.split(';')
        changdu.append(len(gene))
    #print changdu
    weidian=[]
    i=0
    with open(filename1,'r') as f:
        for line in f.readlines():
            line=line.strip('\n')
            data=line.split('\t')
            if i>0:
                for x in range(changdu[i-1]):
                    weidian.append(data[0])
            i=i+1
    #print weidian 
    return weidian

if __name__=="__main__":
    s_time=datetime.datetime.now()
    print "获取基因和位点。。。"
    filename="Methylation Beta Value0.3.txt"
    gene,data=get_gene(filename)
    genee=get_position(filename)
    filename1="Methylation Beta Value0.3.txt"
    weidian=get_weidian(filename1)
    print "开始进行位点----基因替换。。。。。"
    data1=data.reindex(index=weidian)
    data1['Position_to_TSS']=genee
    del data1['Gene_Symbol']
    del gene[-1]
    gene.append('cancer')
    data1=data1.T
    data1.columns=gene
    print "正在写入数据。。。。。。"
#    data.to_csv('Methylation Beta Value10.0.txt',sep='\t',header=True,index=True)
    data1.T.to_csv('Methylation Beta Value0.4.txt',sep='\t',header=True,index=True)
    print "保存完成。。。。"
    e_time=datetime.datetime.now()
    time=e_time-s_time
    print "程序执行完成，共用时"+str(time)
    



    
    
            
        
        