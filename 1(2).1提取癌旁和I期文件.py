# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 10:31:24 2017
从临床文件提取癌旁和I期样本
@author: Administrator
"""
import json
import pandas as pd

def get_filename():
    filenames=[]
    with open("metadata.json",'r') as fp1:
        content1=fp1.read()
        target = json.loads(content1)
    for xx in target:
        TCGA_ID = xx["associated_entities"][0]["entity_submitter_id"]
        Iscancer = int(TCGA_ID[13:14])
        stage_str = xx["cases"][0]["diagnoses"][0]["tumor_stage"]
        filename=xx["file_id"]
        if (Iscancer==1 or (stage_str.find("stage i")!=-1 and stage_str.find("stage ii")==-1 and \
                            stage_str.find("stage iii")==-1 and stage_str.find("stage iv")==-1)):
            filenames.append(filename)
    filenames1=list(set(filenames))
    return target,filenames1
            
if __name__ == '__main__':
    print "kaishi ..."
    data=pd.read_csv("gdc_manifest.txt",sep='\t',index_col=0)
    data=data.T
    file1=list(data)
    target,filenames=get_filename()
    file2=[]
    for x in file1:
        for xx in filenames:
            if x==xx:
                file2.append(xx)
#    print filenames
    print len(file2)
    print len(file1)
    print len(filenames)
    print "tiqu 文件名...."
    file3=list(set(file2))
    print len(file3)
    data1=data[file3]
    tcga=[]
    for x in file3:
        for xx in target:
            TCGA_ID = xx["associated_entities"][0]["entity_submitter_id"]
            Iscancer = int(TCGA_ID[13:14])
            stage_str = xx["cases"][0]["diagnoses"][0]["tumor_stage"]
            filename=xx["file_id"]
            if x==xx["file_id"]:
                TCGA_ID = xx["associated_entities"][0]["entity_submitter_id"]
                Iscancer = int(TCGA_ID[13:14])
                if Iscancer==1:
                    print TCGA_ID
                    tcga.append(TCGA_ID)
    print len(tcga)
           
    data1.T.to_csv("gdc_manifest_change.txt",sep='\t',header=True,index=True)
    
            
        
