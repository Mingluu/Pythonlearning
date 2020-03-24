import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

rho = 0.5
sample=[]
bias = []
for n in range (1000,50000,500):
    # Data generating process    
    y = np.random.normal(size=(n+100,))
    for i in range(1,n+100):
        y[i] += rho*y[i-1]
    #print(len(y))
    y = y[100:]
    xmat = y[:-1]
    ymat = y[1:]
    #print(len(xmat),len(ymat),len(y))
    model = linear_model.LinearRegression().fit(np.array(xmat).reshape(-1,1),np.array(ymat).reshape(-1,1))
    sample.append(n)
    bias.append([model.coef_ - rho][0][0])

plt.plot(sample, bias)
plt.ylabel('Bias Between OLS and AR(1)')
plt.xlabel('Sample Size')
