# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 15:11:42 2017

@author: luowen
"""
import numpy as np
import copy
import math
#GeneticOperator


#definr sigmod function
def sigmof(x):
    return 1/(1+math.exp(-x))

def selection(population,data,pool,tour):
    row,column=np.shape(population)
    parents=np.zeros([pool,column])
    for i in range(pool):
        a=np.random.randint(0,row-1)
        for j in xrange(tour):
            b=np.random.randint(0,row-1)
            if fitness(data,population[a])<fitness(data,population[b]):
                best=b
            else:
                best=a
        parents[i]=copy.deepcopy(population[best])
    return parents
    
    
def fitness(data,individual):
    dt=0.1
    row,column=np.shape(data)
    N=int(math.sqrt(len(individual)))
    Ns=row/N
    cdata=np.zeros([row,column])
    cdata[:,0]=data[:,0]
    for i in xrange(column-1):
        for j in xrange(Ns):
            for k in xrange(N):
                temp=individual[N*N+k]+np.sum(np.multiply(cdata[j*N:(j+1)*N,i],individual[k*N:(k+1)*N]))
                cdata[j*N+k,i+1]=(dt/individual[N*(N+1)+k])*sigmof(temp)+(1-(dt/individual[N*(N+1)+k]))*cdata[j*N+k,i]
    cha=data-cdata
    er=np.multiply(cha,cha)
    dataerror=-np.sum(er)/(N*Ns*column)
    return dataerror
    
def Cross_Mutate(parents,pc,pm):
    row,column=np.shape(parents)
    N=int(math.sqrt(len(parents[0])))
    for i in xrange(row):
        if np.random.rand()<pc: #cross
            cpos=np.random.randint(0,column)
            neighbor=np.random.randint(0,row)
            tempind=copy.deepcopy(parents[i])
            parents[i,cpos:column]=copy.deepcopy(tempind[cpos:column])
            parents[neighbor,cpos:column]=copy.deepcopy(tempind[cpos:column])

    for i in xrange(row):
        ps=int(column*0.2)
        for j in xrange(ps):
            if np.random.rand()<pm:
                mpoint=np.random.randint(0,column)
                if mpoint<N*(N+1):
                    parents[i,mpoint]=parents[i,mpoint]+np.random.uniform(-0.4,0.4)
                    if np.fabs(parents[i,mpoint])>=1:                    
                        parents[i,mpoint]=np.random.uniform(-1,1)
                else:
                    parents[i,mpoint]=parents[i,mpoint]+np.random.uniform(-1,4)
                    if parents[i,mpoint]>=15 or parents[i,mpoint]<=1:                    
                        parents[i,mpoint]=np.random.uniform(1,15)
    return parents
    
                    
            
    
    