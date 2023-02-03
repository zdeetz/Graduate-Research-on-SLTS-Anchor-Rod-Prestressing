# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 12:23:15 2019

@author: zacd
"""

# get current file directory
from __future__ import division
import os.path
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#from mpl_toolkits import mplot3d
from scipy import signal

# Code to combine all the data file from multiple directories at once
#%% Get current parent working directory
working_dir = os.getcwd()

# initialize analysis
if not os.path.exists("output"):
    os.makedirs("output") # make a output directory if does not exist
data_total = []
file_list = []
df = []
fo = []


# walking to the directory top-down
for root, dirs, files in os.walk(working_dir):
# preallocate file list


    for filename in files:
         # match files that match this name

        if filename.startswith("CR9000_MNDOT_"):
            try:
                dft = pd.read_csv(root+'/'+filename, index_col=0, header=1, engine = 'c')
                dft = dft.drop(dft.index[[0,1]])
                dft=dft.astype(float)
                df.append(dft)
            except:
                print(filename)
                continue

frame = pd.concat(df, axis = 0)
#            fr.astype(float)
    
#            frame = pd.concat(fr)
        
print('Frame Compile Done')
#frame = pd.concat(fr, axis = 0)

            
    #splitting out stuff we want into a format that the plotter won't cry about 
ws = frame.iloc[:,1:2]
c = frame.iloc[:,0:1]
b2 = frame.iloc[:,3:4]
b3 = frame.iloc[:,4:5]
b4 = frame.iloc[:,15:16]
b6 = frame.iloc[:,6:7]

p1 = frame.iloc[:,7:8]
p2 = frame.iloc[:,8:9]
p3 = frame.iloc[:,9:10]
p4 = frame.iloc[:,10:11]
p5 = frame.iloc[:,11:12]
p6 = frame.iloc[:,12:13]
p7 = frame.iloc[:,13:14]
p8 = frame.iloc[:,14:15]


x = np.ravel(ws.to_numpy())
c = np.ravel(c.to_numpy())
z2 = np.ravel(b2.to_numpy())
z3 = np.ravel(b3.to_numpy())
z4 = np.ravel(b4.to_numpy())
z6 = np.ravel(b6.to_numpy())
zp1 = np.ravel(p1.to_numpy())
zp2 = np.ravel(p2.to_numpy())
zp3 = np.ravel(p3.to_numpy())
zp4 = np.ravel(p4.to_numpy())

print('Frames Split')


#%%2D Contour plotter for stresses in rods

n = 0

for j in x, z2, z3, z4, z6, zp1, zp2, zp3, zp4: #b2, b3, b4, b6, p1, p2, p3, p4:

    n += 1
    print(n)
    
#    j = j-j.mean()
#    ffd = np.array([c,i])
#    b, a = signal.butter(6, 0.2, btype='lowpass', analog=False)
#    c = signal.filtfilt(b, a, j)

    fot = np.abs(np.fft.fft(j))
    
#    plt.plot(fot)
#    plt.show()
            
#    time_step = 1/100
#    freqs = np.fft.fftfreq(j.size, d = time_step)
#    idx = np.argsort(freqs)
#
#    plt.plot(freqs[idx], fot[idx])
#    plt.xlabel('Frequency (Hz)')
#    plt.yscale('log')
#    plt.xscale('log')
#    plt.axis([0.01, 100, 1, 10000000000])
#    print(fou)

#    plt.show()
##
    plt.psd(j, Fs = 100)
    plt.xscale('log')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Strain (ue/Hz)')
    plt.show()

