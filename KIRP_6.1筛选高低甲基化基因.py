import pandas as pd
import numpy as np
def readdata(filename):
    data= pd.read_csv(filename,sep='\t',index_col=0)
    data=data.T
    data0=data[data['cancer']==0]
    data1=data[data['cancer']==1]
    return data,data0,data1
	
def logfc(data,data0,data1):
    methyh=[]
    methyl=[]
    a=list(data.columns[:-1])
    for xx in a:
        m1=np.median(data0[xx])
        m2=np.median(data1[xx])
        p=m2-m1
        if p>0:
            methyh.append(xx)
        if p<0:
            methyl.append(xx)
    return methyh,methyl

                       
if __name__=='__main__':
    print "¿ªÊ¼Ö´ÐÐ"  
    name="Methylation Beta Value6.0"
    filename=name+".txt"
    data,data0,data1=readdata(filename)	
    methyh,methyl=logfc(data,data0,data1)	
    print "É¸Ñ¡¸ßµÍ¼×»ù»¯Î»µã"
    methyh.append('cancer')
    data_methyh=data[methyh]
    methyl.append('cancer')
    data_methyl=data[methyl]
    print "¸高甲基化:{},低甲基化:{}".format(len(methyh)-1,len(methyl)-1)
    print"¿ªÊ¼±£´æÊý¾Ý"
    name1=name+'_high.txt'
    name2=name+'_low.txt'
    data_methyh.T.to_csv(name1,sep='\t',header=True,index=True)
    data_methyl.T.to_csv(name2,sep='\t',header=True,index=True)
    print "Íê³É"
    
'''
76.74
'''
