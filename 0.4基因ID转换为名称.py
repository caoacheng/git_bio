#-*- coding: utf-8 -*-
import os
import numpy as np
import pandas as pd
from scipy import stats
import datetime
'''
将基因的ID号转换为名称，并统计各个类型的数量
'''
def get_file_info(filename):
    all_hang = 0
    stage_1qi=0
    stage_2qi =0
    stage_3qi = 0
    stage_4qi =0
    stage_no =0
    lie_all = 0
    quan0_Num = 0 
    with open(filename ,'r') as f:
        for line in f.readlines():
            all_hang = all_hang + 1
            if(all_hang>1):   #第一行数据去掉
                line = line.strip('\n')
                data = line.split("\t")
                if(data[1]=='0.0' and data[100]=='0.0'):
                    quan0 = True
                    for xx in data[1:]:
                        if xx != '0':quan0 = False
                        if quan0 == False:break
                    if quan0 == True:
                        quan0_Num = quan0_Num + 1
                        #print ("出现一次全0基因行：%s\n" %str(all_hang))
    print ("一共读取数据行数：%d ，其中出现全0行数：%d" %(all_hang,quan0_Num))
    last_line = 0
    num_ai_pang = 0
    num_ai = 0
    with open(filename ,'r') as f1:
        for line1 in f1.readlines():
            last_line = last_line + 1
            if last_line == all_hang-1:
                   line1 = line1.strip('\n')
                   data = line1.split("\t")
                   for xx in data:
                        if xx=='cancer':  #第一列的stage不算
                           lie_all = lie_all + 1
                           continue
                        if(xx=='0'):num_ai_pang = num_ai_pang + 1
                        elif(xx=='1'):num_ai = num_ai + 1
                        else:
                            print "出现未知的样本： ",xx
                        lie_all = lie_all + 1
                
        print ("一共有%s列，其中癌症有%s列，癌旁有%s列" %(str(lie_all),str(num_ai),str(num_ai_pang)))
    return all_hang,lie_all

def write_list_to_file(filename,myList):
    matrix_a = np.array(myList)
    np.savetxt(filename,matrix_a,fmt=['%s']*matrix_a.shape[1],delimiter='\t',newline='\n')

if __name__ == '__main__':
    start_time = datetime.datetime.now()
#返回当前目录的上级目录
    
    fileName = "KIRP-gene express file.txt"
    
    rows,cols = get_file_info(fileName)
    myList = [([0] * cols) for i in range(rows)]

    with open("geneGTF_file.txt",'r') as fp_test:
            list_content = [content_test for content_test in fp_test.readlines()]      #将基因gtf文件存到内存，就不用每次都打开文件读取，节省时间
    

    num_all = 0
    with open(fileName,'r') as fp:
        for content in fp.readlines():
            content = content.strip('\n')
            name = content.split("\t")
            lieshu = 0
            for yy in name:
                myList[num_all][lieshu] = yy
                lieshu = lieshu + 1
            num_all = num_all + 1
            if num_all%500==0:
                print "正在将基因数据加载到矩阵...%d"%(num_all)
    gene_dic = dict()

    def get_gene_name(ID):
        for linea in list_content:
            GTF_info = linea.split("\t")
            if ID==GTF_info[0]:
             gene_name = GTF_info[1]
             gene_type = GTF_info[2]
             break
        return gene_name,gene_type



    for xx in range(len(myList)):
        if xx %500 ==0:print "正在将基因ID转换为名称，并统计各类数目......%d"%(xx)
        first_lie = myList[xx][0]
        if first_lie.find('EN')!=-1:
            gene_name,gene_type = get_gene_name(first_lie)
            myList[xx][0] = gene_name
            try:
                gene_dic[gene_type] = gene_dic[gene_type] + 1
            except:
                gene_dic[gene_type] = 1

    print "正在存储数据......"

    fileName_out = fileName
    
    write_list_to_file(fileName_out,myList)
    print gene_dic
    get_file_info(fileName_out)          
    
    end_time = datetime.datetime.now()
    meal_time = (end_time - start_time)
    print("程序执行完毕! 一共耗时 %s " %(str(meal_time)))


'''
结果
一共读取数据行数：5323 ，其中出现全0行数：0
一共有296列，其中癌症有182列，癌旁有113列
正在将基因数据加载到矩阵...500
正在将基因数据加载到矩阵...1000
正在将基因数据加载到矩阵...1500
正在将基因数据加载到矩阵...2000
正在将基因数据加载到矩阵...2500
正在将基因数据加载到矩阵...3000
正在将基因数据加载到矩阵...3500
正在将基因数据加载到矩阵...4000
正在将基因数据加载到矩阵...4500
正在将基因数据加载到矩阵...5000
正在将基因ID转换为名称，并统计各类数目......0
正在将基因ID转换为名称，并统计各类数目......500
正在将基因ID转换为名称，并统计各类数目......1000
正在将基因ID转换为名称，并统计各类数目......1500
正在将基因ID转换为名称，并统计各类数目......2000
正在将基因ID转换为名称，并统计各类数目......2500
正在将基因ID转换为名称，并统计各类数目......3000
正在将基因ID转换为名称，并统计各类数目......3500
正在将基因ID转换为名称，并统计各类数目......4000
正在将基因ID转换为名称，并统计各类数目......4500
正在将基因ID转换为名称，并统计各类数目......5000
姝ｅ湪瀛樺偍鏁版嵁......
{'unitary_pseudogene': 10, 'antisense': 413, 'snRNA': 8, 'lincRNA': 515, 'TEC': 60, 'sense_intronic': 37, 'protein_coding': 3985, 'transcribed_unprocessed_pseudogene': 46, 'processed_transcript': 44, 'TR_V_pseudogene': 1, 'sense_overlapping': 26, 'transcribed_processed_pseudogene': 18, 'miRNA': 18, 'unprocessed_pseudogene': 32, 'polymorphic_pseudogene': 2, 'snoRNA': 1, 'misc_RNA': 1, 'rRNA': 1, 'non_coding': 1, 'processed_pseudogene': 102}
一共读取数据行数：5323 ，其中出现全0行数：0
一共有296列，其中癌症有182列，癌旁有113列
程序执行完毕! 一共耗时 0:03:48.946000


一共读取数据行数：964 ，其中出现全0行数：0
一共有296列，其中癌症有182列，癌旁有113列
正在将基因数据加载到矩阵...500
正在将基因ID转换为名称，并统计各类数目......0
正在将基因ID转换为名称，并统计各类数目......500
姝ｅ湪瀛樺偍鏁版嵁......
{'antisense': 109, 'unitary_pseudogene': 1, 'TEC': 25, 'lincRNA': 97, 'unprocessed_pseudogene': 4, 'sense_intronic': 11, 'protein_coding': 667, 'transcribed_unprocessed_pseudogene': 15, 'processed_transcript': 9, 'sense_overlapping': 8, 'transcribed_processed_pseudogene': 2, 'miRNA': 1, 'non_coding': 1, 'processed_pseudogene': 12}
一共读取数据行数：964 ，其中出现全0行数：0
一共有296列，其中癌症有182列，癌旁有113列
程序执行完毕! 一共耗时 0:00:44.104000





一共读取数据行数：44 ，其中出现全0行数：0
一共有296列，其中癌症有182列，癌旁有113列
正在将基因ID转换为名称，并统计各类数目......0
姝ｅ湪瀛樺偍鏁版嵁......
{'protein_coding': 38, 'miRNA': 1, 'lincRNA': 3}
一共读取数据行数：44 ，其中出现全0行数：0
一共有296列，其中癌症有182列，癌旁有113列
程序执行完毕! 一共耗时 0:00:02.043000


一共读取数据行数：18 ，其中出现全0行数：0
一共有296列，其中癌症有182列，癌旁有113列
正在将基因ID转换为名称，并统计各类数目......0
姝ｅ湪瀛樺偍鏁版嵁......
{'antisense': 2, 'protein_coding': 13, 'lincRNA': 1}
程序执行完毕! 一共耗时 0:00:00.899000







'''
