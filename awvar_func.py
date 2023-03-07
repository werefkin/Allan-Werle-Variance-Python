# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 09:05:37 2021

@author: Ivan Zorin
"""


import numpy as np
import matplotlib.pyplot as plt



def awvar(data,dt=1):
    """
    standard Allan-Werle VARiance (AWVAR)
    (the same notation as in the paper of Werle is used)
    can be inefficient computationally (although it is not crucial here), 
    but transparent and straight forward implementation
    data - input spectroscopic data
    dt - sampling rate
    """
    n=len(data)
    clusters=np.unique(np.arange(0,int(np.round(n/2)))+1).astype(np.int64)
    awvar=[]
    for clus in clusters:
        M=int(np.floor(n/clus))
        As=[]
        As1=[]
        diff=[]
        for idx in range(1,M):
            as0=sum(data[(idx-1)*clus:(idx)*clus])/clus
            as1=sum(data[(idx)*clus:(idx+1)*clus])/clus
            As.append(as0)
            As1.append(as1)
    
            diff.append((as1-as0))
            
        awvar.append(np.mean(np.array(diff)**2)/2)
    taus=clusters*dt
    return awvar,taus





def oawvar(data,dt=1):
    """
    Overlapping Allan-Werle Variance 
    (the same notation as in the paper of Werle is used)
    can be inefficient computationally (although it is not crucial here), 
    but transparent and straight forward implementation
    data - input spectroscopic data
    dt - sampling rate
    """
    #OVERLAPPING Allan-Werle variance
    n=len(data)
    clusters=np.unique(np.arange(0,int(np.round(n/2)))+1).astype(np.int64)
    oawvar=[]
    
    for clus in clusters:
        M=n
        diff=[]
        for j in range (0,M-2*clus):
            as0=np.mean(data[j:j+clus])
            as1=np.mean(data[j+clus:j+2*clus])           
            diff.append((as1-as0))
        oawvar.append(np.mean(np.array(diff)**2)/2)
    taus=clusters*dt
    return oawvar, taus







#DEMO 
#GENERATE SOME INPUT DATA -- some spectroscopic data similar to one generated in Werle, P., Mücke, R. & Slemr, F. The limits of signal averaging in atmospheric trace-gas monitoring by tunable diode-laser absorption spectroscopy (TDLAS). Appl. Phys. B 57, 131–139 (1993). https://doi.org/10.1007/BF00425997
N=600 
a=12
data=np.zeros(N)
for i in range(0,len(data)):
    data[i]=a-5e-5*i+np.random.normal(0, 0.01)



av, taus1 =awvar(data)   
oa, taus2 = oawvar(data)   


#PLOT
plt.loglog(taus1,np.array(av,dtype=np.float64))    
plt.loglog(taus2,np.array(oa,dtype=np.float64))     
plt.show()



    


