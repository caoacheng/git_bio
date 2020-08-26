# -*- coding: utf-8 -*-
"""""""""""""""

"""""""""""""""
import pandas as pd
def del_quan0(filename,):
    data1,hang_index1,lie_columns1=read_data(filename1)
    all_hang = 0
    quan0_Num = 0 
    a=[] #放置全零行所在的索引位置：第二行索引为0，第一行为非数据行
    with open(filename ,'r') as f:
        for line in f.readlines():
            all_hang = all_hang + 1
            if(all_hang>1):   #第一行数据去掉
                line = line.strip('\n')
                data = line.split("\t")
                lin=len(data)-1
                ling_num=0
                for xx in data[1:]:
                    if xx == '0.0':
                        ling_num=ling_num+1
                if ling_num == lin:
                    quan0_Num = quan0_Num + 1
                    a.append(all_hang-2)				    
        print ("二次删除全零行前一共读取数据行数：%d ，其中出现全0行数：%d" %(all_hang,quan0_Num))
    hang=[]
    for x in range(len(a)):
        hang.append(hang_index1[a[x]])
    data=data1.drop(hang,axis=0)
    print "二次处理后处理后数据大小为："+str(data.shape[0])+","+str(data.shape[1])
    data.to_csv(filename,sep='\t',header=True,index=True)
    

def feiqineirong(filename):
    all_hang = 0
    quan0_Num = 0 
    stage_1qi=0
    stage_2qi =0
    stage_3qi = 0
    stage_4qi =0
    stage_no =0
    last_line=0
    num_ai_pang=0
    num_ai=0
    n=0  #癌旁所在的位置索引
    m=0  #I期所在位置索引
    a=[] #放置全零行所在的索引位置：第二行索引为0，第一行为非数据行
    b=[] #放置要保留列所在索引位置
    with open(filename ,'r') as f:
        for line in f.readlines():
            all_hang = all_hang + 1
            if(all_hang>1):   #第一行数据去掉
                line = line.strip('\n')
                data = line.split("\t")
                lin=len(data)-1
                ling_num=0
                for xx in data[1:]:
                    if xx == '0.0':
                        ling_num=ling_num+1
                if ling_num == lin:
                    quan0_Num = quan0_Num + 1
                    a.append(all_hang-2)				    
        print ("处理前一共读取数据行数：%d ，其中出现全0行数：%d" %(all_hang,quan0_Num))
    with open(filename,'r') as f1:
        for line1 in f1.readlines():
            last_line = last_line + 1  
            if last_line==(all_hang-1):
                line1 = line1.strip('\n')
                data = line1.split("\t") 
                for x in data:
                    n=n+1
                    if(x=='0'):
                        num_ai_pang = num_ai_pang + 1
                        b.append(n-2)
                    if (x=='1'):
                        num_ai = num_ai + 1
            if last_line==all_hang:
                line1 = line1.strip('\n')
                data = line1.split("\t")
                for x in data:
                    m=m+1
                    if (x=='0'):
                        stage_1qi=stage_1qi + 1
                        b.append(m-2)
                    if (x=='1'):stage_2qi =stage_2qi + 1
                    if (x=='2'):stage_3qi=stage_3qi + 1
                    if (x=='3'):
                        stage_4qi=stage_4qi + 1  
                        
                    if(x=='4'):
                        stage_no=stage_no + 1
                        
        print ("一共有%s列，其中癌症有%s列，癌旁部位有%s列\n其中stage i有%s列\n stage ii有%s列\n stage iii有%s列\n stage iv有%s列\n 无分期有%s列" %(str(m-1),str(num_ai),str(num_ai_pang),str(stage_1qi),str(stage_2qi),str(stage_3qi),str(stage_4qi),str(stage_no)))
    c=[]
    for x in b: #除去重复列
        if x in c:continue
        c.append(x)
    return a,c


def read_data(filename):
    data = pd.read_csv(filename,sep='\t',index_col=0)
    hang_index=list(data.index)
    lie_columns=list(data.columns)
    return data,hang_index,lie_columns

if __name__ == '__main__':
    print "开始数据处理"
    filename="KIRP-gene express file.txt"
    a,c=feiqineirong(filename)
    data,hang_index,lie_columns=read_data(filename)
    print "处理前数据大小为："+str(data.shape[0])+","+str(data.shape[1])
    hang=[]
    lie=[]
    for x in range(len(a)):
        hang.append(hang_index[a[x]])
    for x in range(len(c)):
        lie.append(lie_columns[c[x]])
    data=data[lie]
    data=data.drop(hang,axis=0)
    filename1='KIRP-gene express file1.txt'
    print "处理后数据大小为："+str(data.shape[0])+","+str(data.shape[1])
    data.to_csv(filename1,sep='\t',header=True,index=True)    
    del_quan0(filename1)
    print "保存完成"
    
        
        
        
    
    

                
                        
                        
                        
                    
    
     
   
                