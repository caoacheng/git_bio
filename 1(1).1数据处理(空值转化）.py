""""""""""
将‘NA’全部转化为0
"""""""""""""""

import os
import numpy as np
import pandas as pd

with open("Methylation Beta Value.txt",'r') as f:
    for line in f.readlines():
        line=line.split("\t")
        coll=len(line)
        
rows=27581
cols=coll
myList = [([0] * cols) for i in range(rows)]     #60485行，1223列

def write_list_to_file(filename):
    matrix_a = np.array(myList)
    print matrix_a.shape
    np.savetxt(filename,matrix_a,fmt=['%s']*matrix_a.shape[1],delimiter='\t',newline='\n')
      
if __name__ == '__main__':
    curpath = os.getcwd()
    i=0
    with open("Methylation Beta Value0.txt",'r') as fp1:
        for line in fp1.readlines():
            line=line.split("\t")
            for x in range(len(line)):
                if line[x].find('NA')!=-1:
                    line[x]=0
            myList[i]=line
            print"正在处理第"+str(i)+"行.........."
            i=i+1
    os.chdir(curpath)
    print("正在写入到txt文件，请稍等......")
    write_list_to_file("Methylation Beta Value1.txt")
    data = pd.read_csv("Methylation Beta Value1.txt",sep='\t',index_col=0)
    data.to_csv("Methylation Beta Value1.txt",sep='\t',header=True,index=True)
    print("程序执行完毕!")
    
    

