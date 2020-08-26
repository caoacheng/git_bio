
import os
import numpy as np
import json

curpath11 = os.getcwd()
os.chdir(curpath11+"\\450k")
manifest_lines = 0
with open("gdc_manifest.txt",'r') as fp_test:
            for content_test in fp_test.readlines():
                manifest_lines = manifest_lines + 1

os.chdir(curpath11)

rows=485578+2#60485
cols=manifest_lines #1223
myList = [([0] * cols) for i in range(rows)]     #60485�У�1223��


def read_express_file(filename,lieshu):
    gene_name_write = 0
#    global gene_name_write    
    numm=1
    i=0
    with open(filename,'r') as fp:
        for linea in fp.readlines():
            i=i+1
            if (i>1):
                linea=linea.split("\t")
                if(gene_name_write==0):
                    myList[numm][0] = linea[0]
                    myList[numm][lieshu] = linea[1].replace("\n","")
                numm = numm + 1
            else:
                a=linea.split("\t")
                myList[0][0] =a[0]
                
    gene_name_write = 1   #��ʾ��һ�еĻ���ID���Ѿ�д��



def write_list_to_file(filename):
    matrix_a = np.array(myList)
    print matrix_a.shape 
    np.savetxt(filename,matrix_a,fmt=['%s']*matrix_a.shape[1],delimiter='\t',newline='\n')

def get_stage_num(xx):
    if(xx.find("stage i")!=-1 and xx.find("stage ii")==-1 and xx.find("stage iii")==-1 and xx.find("stage iv")==-1):return 0
    elif(xx.find("stage ii")!=-1 and xx.find("stage iii")==-1):return 1
    elif(xx.find("stage iii")!=-1):return 2
    elif(xx.find("stage iv")!=-1):return 3
    else:
        print "�޷�������ת��Ϊ0-2֮������֣��Ѿ�ת��Ϊ4:   ",xx
        return 4
    
if __name__ == '__main__':
    curpath = os.getcwd()
    print curpath
    os.chdir(curpath+"\\450k")
    num_all = 0
    with open("metadata.json",'r') as fp1:
        content1=fp1.read()
        target = json.loads(content1)
        myList[-2][0] = 'cancer'
        myList[-1][0] = 'stage'
        #os.chdir(curpath+"\\Methylation Beta Value")
        with open("gdc_manifest.txt",'r') as fp:
            for content in fp.readlines():
                name = content.split("\t")
                if(len(name[0])<20):continue
                for xx in target:
                    #if(num_all==991):continue
                    if(xx["file_id"]==name[0]):
                        TCGA_ID = xx["associated_entities"][0]["entity_submitter_id"]
                        IsCancer = int(TCGA_ID[13])
                        if(IsCancer==0):
                            myList[-2][num_all+1] = 1    #��֢��λ��1��������0
                        else:
                            myList[-2][num_all+1] = 0
                        myList[0][num_all+1] = xx["associated_entities"][0]["entity_submitter_id"]
                        try:
                            stage_str = xx["cases"][0]["diagnoses"][0]["tumor_stage"]
                            myList[-1][num_all+1] = get_stage_num(stage_str)
                        except:
                            print "���ִ���û�з�����Ϣ���Ѿ�ת��Ϊ4",xx["associated_entities"][0]["entity_submitter_id"]
                            myList[-1][num_all+1] = 4
                cur= curpath+"\\450k"+"\\"+name[0]
                print cur

                os.chdir(cur) 
                filename_txt=name[1]
#                filename_txt = os.path.splitext(name[1])[0]
                read_express_file(filename_txt,num_all+1)     #��ȡ�ļ���Ļ�����ֵ��myList����
                num_all = num_all+1;
                print("���ڶ�ȡ�������ļ��������ص�����....." +str(num_all))
                #if(num_all==3):break
        print("��ȡ���!   һ����ȡ�ļ����� "+str(num_all))
    os.chdir(curpath11)
    print("����д�뵽txt�ļ������Ե�......")
    write_list_to_file("Methylation Beta Value1.txt")
    print("����ִ�����!")
    
    
       


