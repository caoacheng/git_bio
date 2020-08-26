
import numpy as np
#from pandas import DataFrame as df
import pandas as pd
import datetime

#value12=[]
#with open("Methylation Beta Value0.3.txt",'r') as f:
#    m=0
#    for line in f.readlines():
#        line = line.strip('\n')
#        data = line.split("\t")
#        coll=len(data)
#        m=m+1
#f.close
#print m,coll
#rows=m
#cols=coll
#myList = [([0] * cols) for i in range(rows)]   


def write_list_to_file(filename,myList):
    matrix_a = np.array(myList)
    np.savetxt(filename,matrix_a,fmt=['%s']*matrix_a.shape[1],delimiter='\t',newline='\n')
    
    
if __name__ == '__main__':
    s_time=datetime.datetime.now()
    print "��ʼ��������������̽��"
    value=[]
    with open("Methylation Beta Value0.5.txt",'r') as f:
        m=0
        for line in f.readlines():
            line = line.strip('\n')
            data = line.split("\t")
            if m==0:
                value.append(data)
#                myList[m]=data
                print "���ڴ����"+str(m)+"��......"
                m=m+1
            else:
                if data[-1]!='na':
                    if (int(data[-1])<0 and int(data[-1])>-201):
                        value.append(data)
#                    myList[m]=data
                        print "���ڴ����"+str(m)+"��......"
                        m=m+1
                else:
                    value.append(data)
                    print "���ڴ����"+str(m)+"��......"
            

    print "��ʼ�����ļ�"
    write_list_to_file("Methylation Beta Value0.6.txt",value) 
#    data=pd.read_csv("Methylation Beta Value0.4.txt",sep='\t',index_col=0)
#    data=data.T
#    del data['0']
#    data.T.to_csv("Methylation Beta Value0.4.txt",sep='\t',header=True,index=True)
#    
    print "������ɡ�������������"
    e_time=datetime.datetime.now()
    time=e_time-s_time
    print "����ִ����ɣ�����ʱ"+str(time)
'''

'''
