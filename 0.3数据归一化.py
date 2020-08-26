#-*-coding: utf-8 -*-
import pandas as pd
        
def pdtoNorm(data):      #pandas形式归一化
    max_val = list(data.max(axis=0))  
    min_val = list(data.min(axis=0))   
    nan_values = data.isnull().values  
    row_num = len(list(data.values))  
    col_num = len(list(data.values)[1])
    
    for rn in range(row_num):   
        nan_values_r = list(nan_values[rn])  #返回改行的值true和false，是否全0
        for cn in range(col_num-1):    #最后一列为分期信息，不进行归一化
            if nan_values_r[cn] == False: #如果不等于0 
                data.values[rn][cn] =(data.values[rn][cn] - min_val[cn])/(max_val[cn] - min_val[cn])  
            else:  
                print 'Wrong'

    return data

if __name__ == '__main__':
    print "正在读取数据..."
    data_old = pd.read_csv("KIRP-gene express file1.txt",sep='\t',index_col=0)
    data_t = data_old.T
    if 'stage' in list(data_t):
        print "正在删除stage行数据..."
        del data_t['stage']
    print "正在进行数据归一化...."
    data_norm = pdtoNorm(data_t)
    print "正在存储数据....."
    data_norm.T.to_csv('KIRP-gene express file2.txt',sep='\t',header=True,index=True)    
    print("程序执行完毕!")

'''

'''
