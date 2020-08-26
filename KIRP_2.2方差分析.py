#-*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from scipy import stats
import datetime
'''
使用pandas模块读取数据
先用scipy 的 stats进行齐性分析，方式取'mean'是和spss所做结果一样，默认 'median'，如果为非齐性则进行多个独立样本的非参数检验（Cruskal-Wallis秩和检验），p<0.05的具有显着性差异，保留下来，其余基因删除
如果齐性，则进行单因素方差分析，如果有显着性差异则保留，没有的基因删去
用pandas模块进行存储
'''
with open("Methylation Beta Value2.1.txt",'r') as f:
    for line in f.readlines():
        line=line.split("\t")
        coll=len(line) #列数

def gene_sort(RSN):
    gened= sorted(RSN.iteritems(), key=lambda x : x[1], reverse=False)
    return gened

def write_list_to_file(filename,myList):
    matrix_a = np.array(myList)
    np.savetxt(filename,matrix_a,fmt=['%s']*matrix_a.shape[1],delimiter='\t',newline='\n')

def oneway_deal(data):
    g = data['cancer'].unique()     #返回唯一值
    print g
    num_fei_qici = 0
    num_fei_qici_youchayi = 0
    num_qici_youchayi = 0
    num_gene = 0
    gene_list = list(data)[:-1]
    RSN={}
    for xx in range(len(gene_list)):
        num_gene = num_gene + 1 
        if(num_gene%100==0):print "正在单因素方差分析：%d" %(num_gene)
        args = []
        for i in list(g):
            args.append(data[data['cancer']==i].ix[:,xx])
        #方差齐性检验
        w,p = stats.levene(*args,center = 'median')     #方式取'mean'是和spss所做结果一样，默认 'median'        #print "基因%s齐次性检验结果P值为：%.4f" %(xx,p)
        if p<0.05:
            num_fei_qici = num_fei_qici + 1
            #print ("警告：levene Test显示基因%s方差齐性假设不成立（p=%.2f）" %(xx,p))
            w1,p1 = stats.kruskal(*args)   #对于非齐次的基因，继续做非参检验（Cruskal-Wallis秩和检验）
            if p1<0.05:
                num_fei_qici_youchayi = num_fei_qici_youchayi + 1
                RSN[xx]=p1
#            else:
#                del data[xx]
                continue
        f,p = stats.f_oneway(*args)
        #print f,p
        if p<0.05:
            num_qici_youchayi = num_qici_youchayi + 1
            RSN[xx]=p
#        else:
#            del data[xx]
    print "一共有基因数%d，\n其中方差齐性假设不成立的有%d，这些不满足齐性的基因非参检验具有显着性差异的有%d，\n满足方差齐性假设的有%d，单因素方差分析显示与分期有显著差异的有%d" %(num_gene,num_fei_qici,num_fei_qici_youchayi,num_gene-num_fei_qici,num_qici_youchayi)
#    return data
    return RSN

if __name__ == '__main__':
    start_time = datetime.datetime.now()
    print "正在读取数据..."
    data_old = pd.read_csv("Methylation Beta Value2.1.txt",sep='\t',index_col=0)
    data_t = data_old.T
    print "正在进行数据单因素方差分析，并删去无显著性差异的基因...."
#    data_oneway_deal = oneway_deal(data_t)
    RS=oneway_deal(data_t)
    RSN=gene_sort(RS)
    k=1
    gene=[]
    for x in RSN:
        if x[1]<=(k*0.01)/len(RSN):
            gene.append(x[0])
            k=k+1
    print "FDR<0.01的条件下有%s个位点入选"%(str(len(gene)))
    x=0
    n=0
    rows=len(gene)+2
    cols=coll
    myList = [([0] * cols) for i in range(rows)]   
    with open("Methylation Beta Value2.1.txt",'r') as f:
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
    print "正在存储数据...."
    filename = "Methylation Beta Value2.2.txt"
    write_list_to_file(filename,myList)
      
    end_time = datetime.datetime.now()
    meal_time = (end_time - start_time)
    print("程序执行完毕! 一共耗时 %s " %(str(meal_time)))


'''
其中方差齐性假设不成立的有2742，这些不满足齐性的基因非参检验具有显着性差异的有2742，
满足方差齐性假设的有428，单因素方差分析显示与分期有显著差异的有428
FDR<0.01的条件下有3170个位点入选
'''
