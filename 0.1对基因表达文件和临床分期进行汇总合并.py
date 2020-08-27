#-*-coding: utf-8 -*-
import os
import numpy as np
import json


curpath11 = os.getcwd()
os.chdir(curpath11+"\\LUSC METHY")
manifest_lines = 0
with open(curpath11+"\\gdc_manifest.txt",'r') as fp_test:
            for content_test in fp_test.readlines():
                manifest_lines = manifest_lines + 1

os.chdir(curpath11)

rows=60486 #60485
cols=manifest_lines #1223
myList = [([0] * cols) for i in range(rows)]     #60485行，1223列
gene_name_write = 0

def read_express_file(filename,lieshu):
    global gene_name_write    
    numm=1
    with open(filename,'r') as fp:
        for linea in fp.readlines():
            linea=linea.split("\t")
            if(gene_name_write==0):
                myList[numm][0] = linea[0]
            myList[numm][lieshu] = linea[1].replace("\n","")
            numm = numm + 1
    gene_name_write = 1   #表示第一列的基因ID号已经写完



def write_list_to_file(filename):
    matrix_a = np.array(myList)
    np.savetxt(filename,matrix_a,fmt=['%s']*matrix_a.shape[1],delimiter='\t',newline='\n')

def get_stage_num(xx):
    if(xx.find("stage i")!=-1 and xx.find("stage ii")==-1 and xx.find("stage iii")==-1 and xx.find("stage iv")==-1):return 0
    elif(xx.find("stage ii")!=-1 and xx.find("stage iii")==-1):return 1
    elif(xx.find("stage iii")!=-1):return 2
    elif(xx.find("stage iv")!=-1):return 3
    else:
        print ("无法将分期转换为0-2之间的数字，已经转换为4:   ",xx)
        return 4
    
if __name__ == '__main__':
    curpath = os.getcwd() #获取当前工作目录
    num_all = 0
    with open(curpath11+"\\metadata.json",'r') as fp1:
        content1=fp1.read()
        target = json.loads(content1) #还原本身格式，文件中是字符串，还原成字典或者其他
        myList[-2][0] = 'cancer'  #获取信息癌症、分期
        myList[-1][0] = 'stage'
        os.chdir(curpath+"\\LUSC METHY") #修改当前工作目录
        with open(curpath+"\\gdc_manifest.txt",'r') as fp:
            for content in fp.readlines():
                name = content.split("\t")  #删除回车
                if(len(name[0])<20):continue
                for xx in target:
                    # target = json.loads(content1)包含分期癌症信息
                    # if(num_all==991):continue
                    if(xx["file_id"]==name[0]):
                        TCGA_ID = xx["associated_entities"][0]["entity_submitter_id"] #associated 关联 entities 实体 提交
                        IsCancer = int(TCGA_ID[13:15])
                        if(IsCancer<11):
                            myList[-2][num_all+1] = 1    #癌症部位用1，癌旁用0
                        else:
                            myList[-2][num_all+1] = 0
                        myList[0][num_all+1] = xx["associated_entities"][0]["entity_submitter_id"]
                        try:
                            stage_str = xx["cases"][0]["diagnoses"][0]["tumor_stage"]
                            myList[-1][num_all+1] = get_stage_num(stage_str)
                        except:
                            print ("出现错误，没有分期信息，已经转换为4",xx["associated_entities"][0]["entity_submitter_id"])
                            myList[-1][num_all+1] = 4

                os.chdir(curpath+"\\LUSC METHY\\"+name[0])
                filename_txt = os.path.splitext(name[1])[0]
                read_express_file(filename_txt,num_all+1)     #读取文件里的基因表达值到myList里面
                num_all = num_all+1;
                print("正在读取基因表达文件，并加载到数组....." +str(num_all))
                #if(num_all==3):break
        print("读取完毕!   一共读取文件数： "+str(num_all))
    os.chdir(curpath)
    print("正在写入到txt文件，请稍等......")
    write_list_to_file("KIRP-gene express file.txt")
    print("程序执行完毕!")
    
    
       


