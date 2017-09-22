# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 11:40:36 2017

Simulate a random sum of Bernoulli random variables, each having a different parameter p.
The parameter p is drawn from a uniform distribution on [0,1].

Note: The Bernoulli random variables are independent, but not identically distributed.
The uniform random variables are i.i.d.

@author: Henning Thomsen
"""

# Imports
import numpy as np

# Parameters
numIterBern = 100 # Number of iterations for the Bernoulli random variables
numIterUnif = 250 # Number of iterations for the uniform random variables
lengthBern = 50 # Length of Bernoulli sequence
numTerms = 5.0 # Mean number of terms, parameter in the Poisson random variable

numBernRand = 10 # Iterations of the number of terms
meanTotalBernUnifAveVec = np.zeros([numBernRand])
meanVarTotalBernUnifAveVec = np.zeros([numBernRand])

for termIdx in np.arange(numBernRand):
    numBern = np.random.poisson(lam=numTerms) # Number of Bernoulli random variables
    
    # Draw uniform random numbers, which are the probabilities of the Bernoulli processes
    unifProbs = np.random.uniform(low=0.0, high=1.0, size=(numIterUnif, numBern))
    
    # Draw Bernoulli random numbers
    bernMat = np.random.binomial(1, unifProbs, size=(lengthBern, numIterBern, numIterUnif, numBern))
    
    # Now bernMat is a 3D array. First dim. is the iteration for the Bernoulli r.v., 
    # second dim. is over the uniform r.v., third dim
    
    # Adding the Bernoulli processes
    totalBernMat = np.sum(bernMat, axis=3)
    
    # Average of the total number of successes (i.e. 1's)
    meanTotalBernMat = np.mean(totalBernMat, axis=1)
    varTotalBernMat = np.var(totalBernMat, axis=1)
    
    # Averagning over the iterations
    meanTotalBernIterAveMat = np.mean(meanTotalBernMat, axis=0)
    meanVarTotalBernIterAveMat = np.mean(varTotalBernMat,axis=0)
    
    # Finally, averaging over the realizations of the uniform distribution
    meanTotalBernUnifAveVec[termIdx] = np.mean(meanTotalBernIterAveMat)
    meanVarTotalBernUnifAveVec[termIdx] = np.mean(meanVarTotalBernIterAveMat)
    
# Compute average mean and variance
finalMean = np.mean(meanTotalBernUnifAveVec)
finalVar = np.mean(meanVarTotalBernUnifAveVec)

# Theoretical approximation (assumes the Bernoulli r.v.'s are iid.)
finalMeanApprox = numTerms/2.0 # Uses E[S] = E[N]E[X]
finalVarApprox = numTerms/3.0 # Uses E[S] = E[X]Var(X)+E[X]^2*Var(N)