import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.special import roots_hermite

def workH(n,x,memo):
    if n in memo:
        return memo[n]
    memo[n] =  2*x*workH(n-1,x,memo)-2*(n-1)*workH(n-2,x,memo)
    return memo[n]

def H(n,x):
    if n == 0:
        return 1
    if n == 1:
        return 2*x
    memo = {}
    memo[0] = 1
    memo[1] = 2*x
    return workH(n,x,memo)

def waveFunction(n,x):
    prefactor = np.power(2**n*math.factorial(n)*np.pi**0.5,-0.5)
    return prefactor* np.exp(-0.5*np.power(x,2)) *H(n,x)

def plotWaveFunctions():
    x = np.linspace(-4,4,1000)
    zero = waveFunction(0,x)
    one = waveFunction(1,x)
    two = waveFunction(2,x)
    three = waveFunction(3,x)
    plt.plot(x,zero, label="n=0")
    plt.plot(x,one, label="n=1")
    plt.plot(x,two, label="n=2")
    plt.plot(x,three, label="n=3")
    plt.legend()
    plt.xlabel("x")
    plt.ylabel("H(x)")
    plt.title("Wavefunctions")
    plt.savefig("Prob3PartA.png")

def HighNWave():
    x = np.linspace(-4,4,1000)
    big = waveFunction(30,x)
    plt.clf()

    plt.plot(x,big)
    plt.xlabel("x")
    plt.ylabel("H(x)")
    plt.title("N=30 Wavefunction")
    plt.savefig("Prob3PartB.png")

def integrand(n,x):
    return x*x*waveFunction(n,x)*waveFunction(n,x)

def uncertainty_calc(n):
    points, weights = np.polynomial.legendre.leggauss(100)
    b = 10
    a = -10
    rescaled_points = 0.5*(b-a)*points+0.5*(b+a)
    rescaled_weights = 0.5*(b-a)*weights
    return np.sqrt(np.dot(integrand(n,rescaled_points), rescaled_weights))

def uncertainty_calc_Hermite(n):
    points, weights = roots_hermite(10000) 
    b = 10
    a = -10
    rescaled_points = 0.5*(b-a)*points+0.5*(b+a)
    rescaled_weights = 0.5*(b-a)*weights
    return np.sqrt(np.dot(integrand(n,rescaled_points), rescaled_weights))

if __name__ == "__main__":
    plotWaveFunctions()
    HighNWave()
    print(uncertainty_calc(5))
    print(uncertainty_calc_Hermite(5))

