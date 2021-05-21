# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 09:05:37 2021

@author: Ivan Zorin
"""


import numpy as np
import matplotlib.pyplot as plt


#GENERATE SOME INPUT DATA -- some spectroscopic data similar to one generated in Werle, P., Mücke, R. & Slemr, F. The limits of signal averaging in atmospheric trace-gas monitoring by tunable diode-laser absorption spectroscopy (TDLAS). Appl. Phys. B 57, 131–139 (1993). https://doi.org/10.1007/BF00425997
n=600 
a=12
data=np.zeros(n)
for i in range(0,len(data)):
    data[i]=a-5e-5*i+np.random.normal(0, 0.01)




#STANDARD Allan-Werle variance
clusters=np.unique(np.arange(0,int(np.round(n/2)))+1).astype(np.int64)


avar=[]

for clus in clusters:
    # print(clus)
    M=int(np.floor(n/clus))
    As=[]
    As_one=[]
    diff=[]
    for idx in range(1,M):
        as0=sum(data[(idx-1)*clus:(idx)*clus])/clus
        as1=sum(data[(idx)*clus:(idx+1)*clus])/clus
        As.append(as0)
        As_one.append(as1)
        
        diff.append((as1-as0))
        
    avar.append(np.mean(np.array(diff)**2)/2)
    



#OVERLAPPING Allan-Werle variance

clusters=np.unique(np.arange(0,int(np.round(n/2)))+1).astype(np.int64)
oavar=[]

for clus in clusters:
    M=n
    diff=[]

    for j in range (0,M-2*clus):
        as0=np.mean(data[j:j+clus])
        as1=np.mean(data[j+clus:j+2*clus])           
        diff.append((as1-as0))
    oavar.append(np.mean(np.array(diff)**2)/2)



#PLOT
plt.loglog(clusters,np.array(avar))    
plt.loglog(clusters,np.array(oavar))     
 



    


