# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 21:07:02 2017

@author: Administrator
"""
import numpy as np
import pandas as pd
import datetime 
    
if __name__ == '__main__':
    s_time=datetime.datetime.now()
    i=1
    value=[]
    with open("Methylation Beta Value0.7.txt",'r') as f:
         for line in f.readlines():
             line = line.strip('\n')
             data = line.split("\t")
             value.append(data)

    file1=[]
    with open("gene_GTF.txt",'r') as f1:
         for lines in f1.readlines():
             lines=lines.strip('\n')
             datas=lines.split('\t')
             file1.append(datas)

        
    for x in value:
        for xx in file1:
            if (x[0]==xx[1] and x[-1]==xx[-2]):
                x[0]=xx[0]
                print "共有"+str(len(value)-1)+"行，正在处理第"+str(i)+"行......"
                print x[0]
                i=i+1
    matrix_a = np.array(value)
    np.savetxt("Methylation Beta Value0.8.txt",matrix_a,fmt=['%s']*matrix_a.shape[1],delimiter='\t',newline='\n')
    print "保存完成。。。。。。。"
    print '删除染色体列'
    data0 = pd.read_csv("Methylation Beta Value0.8.txt",sep='\t',index_col=0)
    del data0['Chromosome']

    data0.to_csv("Methylation Beta Value0.8.txt",sep='\t',header=True,index=True)
    e_time=datetime.datetime.now()
    time=e_time-s_time
    print "程序执行完成，共用时"+str(time)
'''

'''
