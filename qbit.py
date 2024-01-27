# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 10:35:05 2024

@author: DELL
"""

import numpy as np
import matplotlib.pyplot as plt

H=np.array([[1,0.5],[0.5,0]],dtype=float)

R=np.array([[0.3,0.2],[0.2,0.7]],dtype=float)

def C(A,B):
    AB=np.dot(A,B)
    BA=np.dot(B,A)
    return(AB-BA)

def Tr(A):
    n=len(A)
    z=0
    for i in range(n):
       z+=A[i][i] 
    return(z)

def d(A):
    return(-1j*C(H,A))

def S(A):
    eig=np.linalg.eigvals(A)
    z=0
    for x in eig:
        z+=x*np.log(x)
    return(-z)

dt=0.001

X=[]
Y=[]

for i in range(10000):
    R=dt*d(R)+R
    X.append(i*dt)
    Y.append(R[0][0].real)

plt.plot(X,Y)
plt.show()