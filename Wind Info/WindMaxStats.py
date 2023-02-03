# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file....its actually not now...
"""

import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


a = pd.read_csv('cleanMaxesc.csv') 
x = a.to_numpy()


plt.figure(figsize=(9, 6))

plt.title('Maximum Daily Windspeed Probability Density Plot', fontsize = 12)
plt.hist(x, bins = 25, density = True, color = 'k')
plt.xlabel('Max Daily Windspeed (mph)',fontsize = 12)
plt.ylabel('Probability Density',fontsize = 12)

plt.show() 

