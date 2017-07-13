# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 15:12:49 2017

@author: luowen
"""
import numpy as np
import math
import matplotlib.pyplot as plt
#Initialize

#definr sigmod function
def sigmof(x):
    return 1/(1+math.exp(-x))


def generate_data(N,Ns,dt):
    length=300
    data=np.zeros([Ns*N,length])
    if N==4:
        beta=[0,-0.5,0,0]
        tao=[10,5,5,5]
        data[:,0]=[0.95,0.2,0.6,0.8]
        w=[[20.0,-20.0,0,0],[15.0,-10.0,0,0],[0,-8.0,12.0,0],[0,0,8.0,-12.0]]
        w=np.array(w)
    else:
        beta=np.random.uniform(-1,1,size=N)
        tao=np.random.uniform(1,15,size=N)

    for i in xrange(length-1):
        for j in xrange(Ns):
            for k in xrange(N):
                temp=beta[k]+sum(np.multiply(data[j*N:(j+1)*N,i],w[k,:]))
                data[j*N+k,i+1]=(dt/tao[k])*sigmof(temp)+(1-(dt/tao[k]))*data[j*N+k,i]
    #display the dataset
    for i in xrange(N):
        plt.subplot(221+i)
        plt.plot(data[i])
    plt.show()
    return data[:,0:50]

def initial_pop(N,Sp):
    pop=np.random.uniform(-1,1,size=[Sp,N*(N+2)])
    taopop=np.random.uniform(1,15,size=[Sp,N])
    pop[:,N*(N+1):N*(N+2)]=pop[:,N*(N+1):N*(N+2)]+taopop
    return pop