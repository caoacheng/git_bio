# -*- coding: utf-8 -*-
"""
@author: Administrator
"""

import pandas as pd
filename="Methylation Beta Value2.2.txt"
data1= pd.read_csv(filename,sep='\t',index_col=0)
data1=data1.T
columns=list(data1)
gene=list(columns)
filename1='Methylation Beta Value9-diff.txt'
f= open(filename1,mode='w')
for i in range(len(gene)-1):
     f.write(gene[i]+'\n')
f.close
