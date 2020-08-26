#-*-coding: utf-8 -*-
import numpy as np
import os
'''
删去表达值全为0的基因
提取癌旁样本、第I分期样本
二次删去表达值全为0的基因
'''
def get_file_info(filename,new=0):
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
                lin =len(data)-1
                ling_number=0
                for xx in data:
                    if xx == '0':
                        ling_number=ling_number + 1
                    if ling_number == lin:
                        quan0_Num = quan0_Num + 1
#                if(data[1]=='0' and data[69]=='0'):
#                    quan0 = True
#                    for xx in data[1:]:
#                        if xx != '0':quan0 = False
#                        if quan0 == False:break
#                    if quan0 == True:
#                        quan0_Num = quan0_Num + 1
                        #print ("出现一次全0基因行：%s\n" %str(all_hang))
    print ("一共读取数据行数：%d ，其中出现全0行数：%d" %(all_hang,quan0_Num))

    num_ai_pang = 0
    num_ai = 0
    last_line=0
    list_no_last_lie=[]
    with open(filename ,'r') as f1:
        for line1 in f1.readlines():
            last_line = last_line + 1
            if(new == 0):
                lie_123 = 0
                if last_line == (all_hang-1):
                    line1 = line1.strip('\n')
                    data = line1.split("\t")
                    for xx in data:
                         if(xx=='0'):
                             num_ai_pang = num_ai_pang + 1
                             list_no_last_lie = list_no_last_lie + [lie_123]     #癌旁的列数，需要放到保留列表里
                         if(xx=='1'):
                             num_ai = num_ai + 1
                         lie_123 = lie_123 + 1
                if last_line == all_hang:
                   line1 = line1.strip('\n')
                   data = line1.split("\t")
                   for xx in data:
                        if xx=='stage':  #第一列的stage不算
                           lie_all = lie_all + 1
                           continue
                        if(xx=='0'):
                            stage_1qi = stage_1qi + 1
                            list_no_last_lie = list_no_last_lie + [lie_all]   #list_no_last_lie表示需要删去的列，把i分期的样本放到保留列表里
                        elif(xx=='1'):stage_2qi = stage_2qi + 1
                        elif(xx=='2'):stage_3qi = stage_3qi + 1
                        elif(xx=='3'):
                            stage_4qi = stage_4qi + 1
                            #list_no_last_lie = list_no_last_lie + [lie_all]   #list_no_last_lie表示需要删去的列，即废弃列的列表
                        else:
                            stage_no = stage_no + 1
                            #list_no_last_lie = list_no_last_lie + [lie_all]
                            print "出现无分期的样本： ",xx
                        lie_all = lie_all + 1
                
            if(new == 1):
                if last_line == (all_hang-1):
                    line1 = line1.strip('\n')
                    data = line1.split("\t")
                    if data[0]=='cancer':
                        for xx in data:
                             if(xx=='0'):
                                 num_ai_pang = num_ai_pang + 1
                             if(xx=='1'):
                                 num_ai = num_ai + 1
                if last_line == all_hang:
                   line1 = line1.strip('\n')
                   data = line1.split("\t")
                   for xx in data:
                        if xx=='stage':  #第一列的stage不算
                           lie_all = lie_all + 1
                           continue
                        if(xx=='0'):stage_1qi = stage_1qi + 1
                        elif(xx=='1'):stage_2qi = stage_2qi + 1
                        elif(xx=='2'):stage_3qi = stage_3qi + 1
                        elif(xx=='3'):
                            stage_4qi = stage_4qi + 1
                        else:
                            stage_no = stage_no + 1
                            print "出现无分期的样本： ",xx
                        lie_all = lie_all + 1
    if new == 0:
        print ("处理之前一共有%s列，其中癌症有%s列，癌旁部位有%s列\n其中stage i有%s列\n stage ii有%s列\n stage iii有%s列\n stage iv有%s列\n 无分期有%s列" %(str(lie_all),str(num_ai),str(num_ai_pang),str(stage_1qi),str(stage_2qi),str(stage_3qi),str(stage_4qi),str(stage_no)))
        last_hang = all_hang - quan0_Num

        b = [0]
        for x in list_no_last_lie:
            if x in b:continue
            b.append(x)
        last_lie = len(b)
        return last_hang,last_lie,b
    if new == 1:
        print ("处理之前一共有%s列，其中癌症有%s列，癌旁部位有%s列\n其中stage i有%s列\n stage ii有%s列\n stage iii有%s列\n stage iv有%s列\n 无分期有%s列" %(str(lie_all),str(num_ai),str(num_ai_pang),str(stage_1qi),str(stage_2qi),str(stage_3qi),str(stage_4qi),str(stage_no)))
        

def write_list_to_file(filename,myList):
    matrix_a = np.array(myList)
    np.savetxt(filename,matrix_a,fmt=['%s']*matrix_a.shape[1],delimiter='\t',newline='\n')



if __name__ == '__main__':
    print "读取中gene express file..."
    filename = "Methylation Beta Value0.0.txt"
    rows,cols,list_no_last_lie = get_file_info(filename)
    myList = [([0] * cols) for i in range(rows)]
    print rows,cols,len(list_no_last_lie),list_no_last_lie

    numm = 0
    print "正在提取癌旁样本、第I分期样本..."
    with open(filename ,'r') as f:
        for line in f.readlines():
            line = line.strip('\n')
            data = line.split("\t")
            quan_0_num = len(data) - 1
            ling_num = 0
            for xx in data:
                if xx == '0':
                    ling_num=ling_num+1
            if ling_num == quan_0_num:
                continue
#            if(data[1]=='0' and data[100]=='0'):
#                    quan0 = True
#                    for xx in data[1:]:
#                        if xx != '0':quan0 = False
#                        if quan0 == False:break
#                    if quan0 == True:continue            #跳过这一行数据

            last_lieshu = 0
            lie_all = 0
            for xy in data:
                if lie_all in list_no_last_lie:       #如果当前列在保留列的列表里
                    myList[numm][last_lieshu] =xy.replace("\n","")   #给一行数据赋值
                    last_lieshu = last_lieshu + 1
                lie_all = lie_all + 1
            numm = numm + 1
    print ("整合完毕，过滤后一共有%s行，%s列数据" %(str(numm),str(last_lieshu)))
    #在list中删除还存在全0的行
    print "二次删除全0的行中。。。"
    list_hang = len(myList)   
    list_lie = len(myList[0])  
    quan_0_list = ['0']*(list_lie-1)
    for i in range(1000):
         for n in range(list_hang):
             if n<len(myList): #删除一行之后，myList会变小，可能会使nu大于myList行数
                 if myList[n][1:]==quan_0_list:
                     del myList[n]
             else:break
         if len(myList)==list_hang:
             break
#    for nu in range(list_hang):
#        for i in range(1000):
#            if nu < len(myList):      #删除一行之后，myList会变小，可能会使nu大于myList行数
#                if myList[nu][1:]==quan_0_list:
#                    del myList[nu]
#                else:break
#            else:break
    
    print ("二次删除完毕，过滤后一共有%s行，%s列数据" %(str(len(myList)),str(len(myList[0]))))

    print("正在写入到txt文件，请稍等......")
    filenameout = "Methylation Beta Value0.111.txt"
    write_list_to_file(filenameout,myList)
    get_file_info(filenameout,1)

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
