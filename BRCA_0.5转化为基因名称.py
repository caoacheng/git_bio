# -*- coding: utf-8 -*-
"""
共有基因： 21049
"""

import pandas as pd
import datetime

def get_gene(filename):
    data=pd.read_csv(filename,sep='\t',index_col=0)
    gene=[]
    genes=data['Gene_Symbol']
#    print genes
    for gene1 in genes:
        dat=gene1.split(';')
        for x in dat:
            gene.append(x)
    return gene,data


def get_position(data):
    gene=[]
    genes=data['Position_to_TSS']
#    print genes
    for gene1 in genes:
        dat=gene1.split(';')
        for x in dat:
            gene.append(x)
    return gene

        

def get_weidian(data,filename):   
    #data=pd.read_csv(filename1,sep='\t',index_col=0)
    data_new=data[data.columns[-2]]
    changdu=[]
    for genes in data_new:
        gene=genes.split(';')
        changdu.append(len(gene))
    chre=[]
    weidian=[]
    i=0
    with open(filename,'r') as f:
        for line in f.readlines():
            line=line.strip('\n')
            data=line.split('\t')
            if i>0:
                for x in range(changdu[i-1]):
                    weidian.append(data[0])
                    chre.append(data[-3])
            i=i+1
    return weidian,chre

if __name__=="__main__":
    s_time=datetime.datetime.now()
    print "获取基因和位点。。。"
    filename="Methylation Beta Value0.4.txt"
    gene,data=get_gene(filename)
    
    TSS=get_position(data)
    
    
    weidian,chre=get_weidian(data,filename)
    

    
    print len(TSS),len(weidian)
    
    print "开始进行位点----基因替换。。。。。"
    data=data.reindex(index=weidian)
    
    data['Position_to_TSS']=TSS
         
    data['Chromosome']=chre     
    del data['Gene_Symbol']
    
    del gene[-1]
    
    gene.append('cancer')
    
    data=data.T
    
    data.columns=gene
    
    print "正在写入数据。。。。。。"
#    data.to_csv('Methylation Beta Value10.0.txt',sep='\t',header=True,index=True)
    data.T.to_csv('Methylation Beta Value0.5.txt',sep='\t',header=True,index=True)
    print "保存完成。。。。"
    e_time=datetime.datetime.now()
    time=e_time-s_time
    print "程序执行完成，共用时"+str(time)
    



    
    
            
        
        
