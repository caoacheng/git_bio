# -*- coding: utf-8 -*-
"""
Created on Wed Jan 03 17:05:08 2018
保存表格
@author: Administrator
"""

import pandas as pd
data=pd.read_csv('12genes.txt',sep='\t',index_col=0)
data=data.T
data0=data[data['cancer']==0.0]
data1=data[data['cancer']==1.0]
filename='12genes_normal.xlsx'
filename1='12genes_cancer.xlsx'
data0.to_excel(filename)
data1.to_excel(filename1)