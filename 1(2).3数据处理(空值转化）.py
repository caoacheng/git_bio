""""""""""
����NA��ȫ��ת��Ϊ0
"""""""""""""""

import os
import numpy as np
import pandas as pd

with open("Methylation Beta Value.txt",'r') as f:
    m=0
    for line in f.readlines():
        line=line.split("\t")
        coll=len(line)
        m=m+1
        
rows=m
cols=coll
myList = [([0] * cols) for i in range(rows)]     

def write_list_to_file(filename):
    matrix_a = np.array(myList)
    print matrix_a.shape
    np.savetxt(filename,matrix_a,fmt=['%s']*matrix_a.shape[1],delimiter='\t',newline='\n')
      
if __name__ == '__main__':
    i=0
    with open("Methylation Beta Value.txt",'r') as fp1:
        for line in fp1.readlines():
            line=line.strip('\n')
            data=line.split("\t")
            for x in range(len(data)):
                if data[x]=='NA':
                    data[x]=0
            myList[i]=data
            print"���ڴ����"+str(i)+"��.........."
            i=i+1
    print("����д�뵽txt�ļ������Ե�......")
    write_list_to_file("Methylation Beta Value0.0.txt")
#    data = pd.read_csv("Methylation Beta Value1.txt",sep='\t',index_col=0)
#    data.to_csv("Methylation Beta Value1.txt",sep='\t',header=True,index=True)
    print("����ִ�����!")
    
    

