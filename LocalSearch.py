# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 15:12:16 2017

@author: luowen
"""
import GeneticOperator as GO
#LocalSearch

def Findbest(children,data):
    best=0
    for i in xrange(len(children)):
        if GO.fitness(data,children[i])>GO.fitness(data,children[best]):
            best=i
    return children[best]