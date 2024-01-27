# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 21:28:09 2024

@author: DELL
"""

import numpy as np
import matplotlib.pyplot as plt

def heatmap2d(arr: np.ndarray):
    plt.imshow(arr, cmap='hot',vmin=0.0,vmax=1)
    x_unit=0.1
    plt.colorbar()
    plt.show()

n=15
Z=np.ones((n,n))
J=1
beta=0.1

def Metro(Z,m):
    i=int(np.random.rand()*n)
    j=int(np.random.rand()*n)
    E=2*J*Z[i][j]*( Z[i-1][j] + Z[(i+1)%n][j] + Z[i][j-1] + Z[i][(j+1)%n] )
    q=np.exp(-E*beta)
    w=np.random.rand()
    if w<=q:
        Z[i][j]=-Z[i][j]
        return(m+2*Z[i][j])
    else:
        return(m)


M=[]
T=[]
m=n**2

for t in range(200):
    #heatmap2d(Z)
    M.append(m/n**2)
    T.append(t)
    m=Metro(Z,m)
    
plt.plot(T,M)
plt.ylim([-1.1,1.1])
plt.show()

#heatmap2d(Z)