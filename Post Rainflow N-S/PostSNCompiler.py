# -*- coding: utf-8 -*-
"""
Created on Mon Aug  26

@author: zacd
"""

# get current file directory
import os.path
import os
import pandas as pd

#%% Get current parent working directory
working_dir = os.getcwd()
df = []
frame = []
dfa = []
dffinal = []
P2o = []
P4o = []
P6o = []
P8o = []

dfout2=[]
dfout4 = []
dfout6 = []
dfout8 = []
appdat = []

for root, dirs, files in os.walk(working_dir):

    for filename in files:
             # match files that match this name
        if filename.endswith("outputPost1SN.xlsx"):
            dft2 = pd.read_excel(root+'/'+filename, index_col=0, header=1, names=["in","count","uerange"])
            df2 = pd.DataFrame(dft2)
            dfout2.append(df2)
            appd2 = pd.concat(dfout2)
            
        if filename.endswith("outputPost3SN.xlsx"):
            dft4 = pd.read_excel(root+'/'+filename, index_col=0, header=1, names=["in","count","uerange"])
            df4 = pd.DataFrame(dft4)
            dfout4.append(df4)
            appd4 = pd.concat(dfout4)
            
#        if filename.endswith("outputPost6SN.xlsx"):
#            dft6 = pd.read_excel(root+'/'+filename, index_col=0, header=1, names=["in","count","uerange"])
#            df6 = pd.DataFrame(dft6)
#            dfout6.append(df6)
#            appd6 = pd.concat(dfout6)
            
        if filename.endswith("outputPost7SN.xlsx"):
            dft8 = pd.read_excel(root+'/'+filename, index_col=0, header=1, names=["in","count","uerange"])
            df8 = pd.DataFrame(dft8)
            dfout8.append(df8)
            appd8 = pd.concat(dfout8)
           
BB2 = appd2.sort_values('count')
BB4 = appd4.sort_values('count')
#BB6 = appd6.sort_values('count')
BB8 = appd8.sort_values('count')

BB2.to_excel(working_dir+'Post1SN.xlsx') 
BB4.to_excel(working_dir+'Post3SN.xlsx')              
#BB6.to_excel(working_dir+'Post6SN.xlsx')       
BB8.to_excel(working_dir+'Post7SN.xlsx')        

 
