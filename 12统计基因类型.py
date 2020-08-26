# -*- coding: utf-8 -*-
"""
Created on Fri Nov 03 14:59:03 2017
统计基因类型
@author: Administrator
"""

import numpy as np
#from pandas import DataFrame as df
import pandas as pd
import datetime

value12=[]
with open("Methlytion4.3-new.txt",'r') as f:
    m=0
    for line in f.readlines():
        line = line.strip('\n')
        data = line.split("\t")
        coll=len(data)
        m=m+1
        value12.append(data)
        
file12=[]
with open("geneGTF_file.txt",'r') as f1:
    for lines in f1.readlines():
        lines=lines.strip('\n')
        datas=lines.split('\t')
        file12.append(datas)

print m,coll
rows=m
cols=coll+1
myList = [([0] * cols) for i in range(rows)]   


def write_list_to_file(filename):
    matrix_a = np.array(myList)
    np.savetxt(filename,matrix_a,fmt=['%s']*matrix_a.shape[1],delimiter='\t',newline='\n')
    
    
if __name__ == '__main__':
    s_time=datetime.datetime.now()
    i=1             
    myList[0][:-1]=value12[0]
    myList[0][-1]=file12[0][-2]
    myList[-1][:-1]=value12[-1]
    myList[-1][-1]='NA'
    print myList[0]
    print myList[-1]
    
    del value12[0]
    del file12[0]
    del value12[-1]
    del file12[-1]
    
    type1=[]
    for x in value12:
        for xx in file12:
            if x[0]==xx[1]:
                myList[i][:-1]=x
                myList[i][-1]=xx[-2]
                type1.append(xx[-2])
                print "正在处理第"+str(i)+"行......"
                i=i+1
                break  
    type2=list(set(type1))
    for x in type2:
        print "%s共同有%s个"%(str(x),str(type1.count(x)))
    
    write_list_to_file("Methylation Beta Value9.txt") 
    data=pd.read_csv("Methylation Beta Value9.txt",sep='\t',index_col=0)
    g = data['gene_type'].unique()
    for i in list(g):
        print str(i)+"包括"+str(list(data[data['gene_type']==i].index))
#    data=data.T
#    del data['0']
#    data.T.to_csv("Methylation Beta Value1.3.txt",sep='\t',header=True,index=True)
##    
    print "保存完成。。。。。。。"
    e_time=datetime.datetime.now()
    time=e_time-s_time
    print "程序执行完成，共用时"+str(time)
'''
unitary_pseudogene共同有1个
sense_intronic共同有1个
lincRNA共同有10个
unprocessed_pseudogene共同有1个
antisense共同有6个
protein_coding共同有46个
transcribed_unprocessed_pseudogene共同有1个
processed_transcript共同有2个
rRNA共同有1个
miRNA共同有2个
misc_RNA共同有1个
processed_pseudogene共同有5个


protein_coding包括['PTPN22', 'PCDHGB4', 'CCDC36', 'PLAT', 'LDHC', 'CST7', 'PM20D1', 
                  'NYNRIN', 'CXCR3', 'KCNH8', 'CRB1', 'IL32', 'MPZ', 'LELP1', 'MOV10L1', 'C10orf71',
                  'HRNR', 'LIMCH1', 'OR6C1', 'LRRTM2', 'EVX2', 'S100A12', 'C1orf54', 'KLHL1', 'KIR3DX1',
                  'RUNX3', 'ZFP42', 'SULT1B1', 'CDH9', 'KLHDC8A', 'TCL1A', 'SDR42E2', 'FAP', 'CST9', 
                  'TAGLN', 'DEGS1', 'COL5A2', 'HIST1H3E', 'C4BPA', 'TRIM77', 'OR7D4', 'PI15', 'PLCZ1', 'DEFB131', 'SCN3B', 'CBLN4']
lincRNA包括['RP11-367G6.3', 'LINC00908', 'LINC00606', 'RP11-56L13.1', 'RP11-495P10.6', 'LINC01114',
            'LINC00486', 'LINC00977', 'RP11-25O3.1', 'RP11-744J10.3']
processed_transcript包括['AC016747.3', 'PCED1B-AS1']
processed_pseudogene包括['RP11-863K10.4', 'RP11-157G21.2', 'CASC4P1', 'RP11-69M1.3', 'TOMM20P2']
unitary_pseudogene包括['PRSS30P']
miRNA包括['MIR184', 'MIR16-2']
antisense包括['FAM83A-AS1', 'GRIK1-AS1', 'RP11-553L6.2', 'AC010127.3', 'RP11-1334A24.6', 'PABPC5-AS1']
misc_RNA包括['WT1-AS_7']
sense_intronic包括['RP11-103B5.4']
transcribed_unprocessed_pseudogene包括['PCDHB19P']
rRNA包括['RNA5SP77']
unprocessed_pseudogene包括['STK19B']
'''