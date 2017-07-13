# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 15:08:51 2017

@author: luowen
"""
import numpy as np
import GeneticOperator as GO
import LocalSearch as LS
import Initialize as Initial
import Update as Update
import matplotlib.pyplot as plt
N=4
Ns=1
dt=0.1
data=Initial.generate_data(N,Ns,dt)

Gm=100
Sp=200
Spool=Sp/2
Stour=2
Pc=0.8
Pm=0.2
population=Initial.initial_pop(N,Sp)
dimension=N*(N+2)
Bestpop=np.zeros([Gm,dimension])
t=0
maxfitness=[]
while t<Gm:
    parents=GO.selection(population,data,Spool,Stour)
    children=GO.Cross_Mutate(parents,Pc,Pm)
    Bestchild=LS.Findbest(children,data)
    Islocal=False
    #localsearch operator
#    while not Islocal:
#        L=neighbor
#        if
#        
#        else:
#            Islocal=True
    population=Update.updatePopulation(population,data,children,Bestchild)
    print 'generation %d'%t
    maxfitness.append(GO.fitness(data,population[0]))
    Bestpop[t]=population[0]
    t+=1
plt.figure()
plt.plot(maxfitness)
plt.show()
finalbest=LS.Findbest(Bestpop,data)
print 'the minist energy is :',GO.fitness(data,finalbest)
    
    