# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file....its actually not now...
"""

import pandas as pd


n=0
co = []
while (n < 763):
    c = pd.DataFrame([1,2,3,4])
    co.append(c)
    
    n = n + 1

cou = pd.concat(co)


dftq = pd.read_csv('max daily.csv') 


#o = dftq.drop([1])
ou = dftq.T
a = ou.set_index(0)
#
o = a.drop(['1', '2', '3'])
out = o.T

o.to_csv('cleanMaxes.csv')
out.to_csv('cleanMaxesTransposed.csv')

