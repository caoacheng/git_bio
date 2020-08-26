#-*-coding: utf-8 -*-
import numpy as np
import pandas as pd
from pandas import DataFrame as df
import datetime
'''
删去表达值全为0的基因
提取癌旁样本、第I分期样本
二次删去表达值全为0的基因
'''
def get_file_info(filename):
    all_hang = 0
    quan0_Num = 0 
    with open(filename ,'r') as f:
        for line in f.readlines():
            all_hang = all_hang + 1
            if(all_hang>1):   #第一行数据去掉
                line = line.strip('\n')
                data = line.split("\t")
                lin =len(data)
                ling_number=0
                for xx in data:
                    if xx == '0' or xx=='0.0':
                        ling_number=ling_number + 1
                    if ling_number == lin:
                        quan0_Num = quan0_Num + 1
    print ("一共读取数据行数：%d ，其中出现全0行数：%d" %(all_hang,quan0_Num))
    last_hang = all_hang - quan0_Num
    last_lie = lin
    return last_hang,last_lie


#def write_list_to_file(filename,myList):
#    matrix_a = np.array(myList)
#    np.savetxt(filename,matrix_a,fmt=['%s']*matrix_a.shape[1],delimiter='\t',newline='\n')



if __name__ == '__main__':
    s_time=datetime.datetime.now()
    print "读取中gene express file..."
    filename = "Methylation Beta Value0.3.txt"
    rows,cols = get_file_info(filename)
    myList = [([0] * cols) for i in range(rows)]
    print rows,cols

    numm = 0
    print "正在删除"
    with open(filename ,'r') as f:
        for line in f.readlines():
            line = line.strip('\n')
            data = line.split("\t")
            quan_0_num = len(data)
            ling_num = 0
            for xx in data:
                if xx == '0' or xx=='0.0':
                    ling_num=ling_num+1
            if ling_num == quan_0_num:
                continue  #跳过这一行数据
            myList[numm]=data    	       
            numm = numm + 1
    print numm
    filenameout = "Methylation Beta Value0.4.txt"
    
    col=myList[0][1:]
    indes=[] 
    del myList[0] 
    for x in myList:
        indes.append(x[0])
        del x[0]        
    data=df(myList,index=indes,columns=col)
    data.to_csv("Methylation Beta Value0.4.txt",sep='\t',header=True,index=True)
#    write_list_to_file(filenameout,myList)
    e_time=datetime.datetime.now()
    time=e_time-s_time
    print "程序执行完成，共用时"+str(time)
    print("程序执行完毕!")

'''
思路：1.提取癌旁和I期所在列的索引
     2.提取癌旁I期，同时删除全零：一行行检索，若为全零行，跳过该行；若不是，将该行中符合癌旁和I期的元素提取
     3.二次删除全领航：
     for i in range(1000):
         for n in range(list_hang):
             if n<len(myList):
                 if myList[n][1:]==quan_0_list:
                     del myList[n]
            else:break
        if len(myList)==list_hang:
            break
'''
