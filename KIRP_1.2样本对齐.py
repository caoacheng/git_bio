# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
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
    data=pd.read_csv("Methylation Beta Value1.1.txt",sep='\t',index_col=0)
    data1=pd.read_csv("gene express file1.1.txt",sep='\t',index_col=0)
    gene=list(data.columns)
    gene1=list(data1.columns)
    genes=[]
    for x in gene:
        for xx in gene1:
            if x==xx:
                genes.append(x)
                break
    print "两者样本交集有%s个"%(str(len(genes)))
    data=data.reindex(columns=genes)
    data1=data1.reindex(columns=genes)
    data1.to_csv("gene express file1.2.txt",sep='\t',header=True,index=True)
    data.to_csv("Methylation Beta Value1.2.txt",sep='\t',header=True,index=True)
    print "保存完成。。。。"
"""
两者样本交集有207个
"""