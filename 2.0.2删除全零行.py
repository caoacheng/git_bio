# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 17:32:22 2017

@author: Administrator
"""
import pandas as pd
print "开始查找全零行。。。。。"
all_hang = 0
quan0_Num = 0 
a=[] 
with open("biaohao_new.txt",'r') as f:
    for line in f.readlines():
        all_hang = all_hang + 1
        if(all_hang>1):   #第一行数据去掉
          line = line.strip('\n')
          data = line.split("\t")
          lin=len(data)-1
          ling_num=0
          for xx in data:
              if xx == '0' or xx=='0.0':
                  ling_num=ling_num+1
              if ling_num == lin:
                  quan0_Num = quan0_Num + 1
                  a.append(all_hang-2)				    
    print ("一共读取数据行数：%d ，其中出现全0行数：%d" %(all_hang,quan0_Num))




#value12=[]
#with open("Methylation Beta Value1.3.txt",'r') as f:
#        for line in f.readlines():
#            line = line.strip('\n')
#            data = line.split("\t")
#            value12.append(data)

print "开始查找全零行。。。。。"
            
#i=0  
#a=[]          
#for x in value12:
#    if x[0]=='0':
#        a.append(i-1)
#        i=i+1
        
data = pd.read_csv("biaohao_new.txt",sep='\t',index_col=0)
hang_index=list(data.index)

print "删除全零行。。。。。"        
hang=[]
for x in range(len(a)):
    hang.append(hang_index[a[x]])
data=data.drop(hang,axis=0)

data.to_csv('biaohao_new1.txt',sep='\t',header=True,index=True)
quan0=0
ss=0
with open("biaohao_new1.txt",'r') as f:
    for line in f.readlines():
        ss = ss + 1
        if(ss>1):   #第一行数据去掉
          line = line.strip('\n')
          data = line.split("\t")
          lin=len(data)-1
          ling=0
          for xx in data:
              if xx == '0' or xx=='0.0':
                  ling=ling+1
              if ling == lin:
                  quan0 = quan0 + 1				    
    print ("处理后。。。。一共读取数据行数：%d ，其中出现全0行数：%d" %(ss,quan0))

print "保存完成"        
    
        