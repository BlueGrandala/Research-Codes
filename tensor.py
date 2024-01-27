# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 21:09:03 2024

@author: DELL
"""

import numpy as np
import matplotlib.pyplot as plt

def Tensor_dot(A,B):
    m,n=len(A),len(B)
    Z=np.zeros((m*n,m*n))
    for i in range(m):
        for j in range(m):
            z=A[i][j]
            for p in range(n):
                for q in range(n):
                    Z[n*i+p][n*j+q]=z*B[p][q]
    return(Z)

H=np.array([[1,0],[0,-1]])
I=np.array([[1,0],[0,1]])

print(Tensor_dot(H,H))

