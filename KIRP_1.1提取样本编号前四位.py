# -*- coding: utf-8 -*-
"""
Created on Thu May 11 16:56:13 2017
转换样本编号，只提取前四位有效信息
@author: Administrator
"""

import pandas as pd
def ID(columns):
    sample_ids=[]
    for x in list(columns):
        sample=x.split('-')
        sample_id=sample[0:4]
        sample_ids.append(sample_id)
    for x in range(len(sample_ids)):
        sample_ids[x]="-".join(sample_ids[x])
    return sample_ids
#def readdata(filename)
if __name__=='__main__':
    data=pd.read_csv("Methylation Beta Value0.6.txt",sep='\t',index_col=0)
    #data1=pd.read_csv("gene express file.txt",sep='\t',index_col=0)
    gene=list(data.columns)
    #gene1=list(data1.columns)
    sample=ID(gene)
    #sample1=ID(gene1)
    print sample
    #print sample1
    data.columns=sample
    #data1.columns=sample1
    #data1=data1.reindex(columns=sample1)
    #data1.to_csv("gene express file1.1.txt",sep='\t',header=True,index=True)
    data.to_csv("Methylation Beta Value1.1.txt",sep='\t',header=True,index=True)
    print "保存完成。。。。"

