# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 15:13:03 2017

@author: luowen
"""
import numpy as np
import copy
import GeneticOperator as GO
#Update

def updatePopulation(population,data,children,Bestchild):
    row,column=np.shape(population)
    P_new=np.zeros([row,column])
    All_P=np.zeros([row+len(children)+1,column])
    All_P[0:row]=copy.deepcopy(population)
    All_P[row:row+len(children)]=copy.deepcopy(children)
    All_P[-1]=copy.deepcopy(Bestchild)
    fit=np.zeros([1,len(All_P)])
    for i in xrange(len(All_P)):
        fit[0][i]=GO.fitness(data,All_P[i])
    S=np.argsort(fit[0])
    t=-1
    for i in xrange(len(P_new)):
        P_new[i]=copy.deepcopy(All_P[S[t]])
        t-=1
    return P_new