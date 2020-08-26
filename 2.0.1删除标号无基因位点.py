"""""""""""""""
位点与基因进行匹配
"""""""""""""""
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import datetime

with open("biaohao.txt",'r') as f:
    m=0
    for line in f.readlines():
        line=line.split("\t")
        coll=len(line) 
        m=m+1
print m,coll

rows=m
cols=coll
myList = [([0] * cols) for i in range(rows)]   

def write_list_to_file(filename):
    matrix_a = np.array(myList)
    np.savetxt(filename,matrix_a,fmt=['%s']*matrix_a.shape[1],delimiter='\t',newline='\n')
if __name__ == '__main__':
    s_time=datetime.datetime.now()
    i=0             
    biaohao=[]
    with open("biaohao.txt",'r') as f2: 
         for lines in f2.readlines():
             lines = lines.strip('\n')
             data2 = lines.split("\t")
             biaohao.append(data2)
    for x in biaohao:
        if x[5]!='.':
            myList[i]=x
            print "正在处理第"+str(i)+"行......"  
            i=i+1
    print "正在写入文件"
    write_list_to_file("biaohao_new.txt")
    data= pd.read_csv("biaohao_new.txt",sep='\t',index_col=0)
    data=data.T
    del data['0']
    data.T.to_csv("biaohao_new.txt",sep='\t',header=True,index=True)
    e_time=datetime.datetime.now()
    time=e_time-s_time
    print "程序执行完成，共用时"+str(time)