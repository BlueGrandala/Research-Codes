# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 11:56:51 2024

@author: DELL
"""

import numpy as np
import matplotlib.pyplot as plt

a,b=0,1
m=1
w=1
dt=0.05
T=0.5
n=int(T/dt)

def H(p,x,a,b):
    return(p**2/(2*m)+0.5*m*w**2*((x-a)**2+(x-b)**2))

def B(t):
    return(1+(t/T)*np.sin(t/T*2.5*np.pi))
    #return(1+t/T)

def D(Z,t):
    p,q=Z[0],Z[1]
    dx=p/m
    dp=-m*w**2*(2*q-a-B(t))
    return(np.array([dp,dx]))

beta=2.5

def Ens(beta,a,b):
    u=np.random.rand()
    v=np.random.rand()
    s=np.sqrt(-2*np.log(u))*np.sin(2*np.pi*v)
    c=np.sqrt(-2*np.log(u))*np.cos(2*np.pi*v)
    p=np.sqrt(m/beta)*s
    q=np.sqrt(1/(2*m*w**2*beta))*c+0.5*(a+b)
    return(p,q)

P=[]
Q=[]
N=8000

for i in range(N):
    K,L=Ens(beta,a,b)
    P.append(K)
    Q.append(L)
    
plt.scatter(P,Q,s=5)
plt.xlim(-3,3)
plt.ylim(-3,3)
plt.show()

W=[]
G=[]

for j in range(N):
    H0=H(P[j],Q[j],a,b)
    W.append(H0)


def RK4(Z,t):
    f1=D(Z,t)
    f2=D(Z+f1*0.5*dt,t+0.5*dt)
    f3=D(Z+f2*0.5*dt,t+0.5*dt)
    f4=D(Z+f3*dt,t+dt)
    D0=Z+dt*1/6*(f1+2*f2+2*f3+f4)
    return(D0)

t=0
for i in range(n):
    for j in range(N):
        Z=[P[j],Q[j]]
        P[j]=RK4(Z,t)[0]
        Q[j]=RK4(Z,t )[1]
    t+=dt

for j in range(N):
    H0=H(P[j],Q[j],a,B(t))
    W[j]=-W[j]+H0
    G.append(np.exp(-beta*W[j]))
plt.hist(W,bins=50)
plt.show()

print('JE Free Energy',-np.log(np.mean(G))*0.4)
print('Theoretical',0.75)
print('<W>',np.mean(W))

