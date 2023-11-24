import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

path = os.getcwd() + '\API\ex1data1.txt'
data = pd.read_csv(path, header=None, names=['Population', 'Profit'])
print(data.head())
print(data.describe())
data.plot(kind="scatter", x="Population",y="Profit",figsize= (12,8),c = 1)
plt.show()

def computeCost(x,y,theta):
    inner = np.power(((x* theta.T)-y), 2)
    return np.sum(inner)/(2*len(x))



def gradientDescent(X, y, theta, alpha, iters):
    temp = np.matrix(np.zeros(theta.shape))
    parameters = int(theta.ravel().shape[1])
    cost = np.zeros(iters)
   
    for i in range(iters):
        error = (X * theta.T) - y
       
        for j in range(parameters):
            term = np.multiply(error, X[:,j])
            temp[0,j] = theta[0,j] - ((alpha / len(X)) * np.sum(term))
           
        theta = temp
        cost[i] = computeCost(X, y, theta)
       
    return theta, cost

alpha = 0.01
iters = 1000

g, cost = gradientDescent(x,y,theta,alpha,iters)
print(g)

print(computeCost(x,y,g))

x = np.linspace(data.Population.win(),data.Population.max(), 100)

f = g[0,0] + (g[0,1] * x)

