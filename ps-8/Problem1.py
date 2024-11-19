import numpy as np
from  scipy.optimize import minimize
import matplotlib.pyplot as plt

data = np.genfromtxt("survey.csv", delimiter=',')
data = data[1:,:]

def p(x, beta_0, beta_1):
    return np.power(1+np.exp(-(beta_0+beta_1*x)),-1)

def neg_log_likelihood(b):
    xdata = data[:,0]
    ydata = data[:,1]
    beta_0 = b[0]
    beta_1 = b[1]
    prob = p(xdata,beta_0, beta_1)
    yes = ydata*np.log(prob)
    no = (1-ydata)*np.log(1-prob) 
    return -np.sum(yes + no )

def plot(data, mlvs):
    beta_0 = mlvs[0]
    beta_1 = mlvs[1]
    x = data[:,0]
    y = p(x, beta_0, beta_1)
    plt.scatter(x,y, color='r', label="model")
    plt.scatter(x, data[:,1], color='b', label="data")
    plt.xlabel("Age")
    plt.ylabel("Probability")
    plt.title("Be Kind, Rewind")
    plt.legend()
    plt.savefig("Logistic.png")

if __name__ == "__main__":
    result = minimize(neg_log_likelihood,[-50,1])
    mlvs = result.x
    cov = result.hess_inv
    errors = np.sqrt(np.diag(cov))
    print("Maximum Likelihood Values ", mlvs)
    print("Covariance ", cov)
    print("Errors", errors)
    plot(data, mlvs)
