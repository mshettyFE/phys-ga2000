import numpy as np
import matplotlib.pyplot as plt

def integrand(x,a):
    return np.power(x,a-1)*np.exp(-x)

def trans1_integrand(x,a):
    return np.exp(-x+(a-1)*np.log(x))

def transformed_integrand(z,a):
# z = x/(c+x)
# x = zc+zx
# x(1-z) = zc
# x = zc/(1-z)
# x = 0.5 c (0/5)
# x = c
# c = a-1
    c = a-1
    x = c*z*np.power(1-z,-1)
    return c*np.power(1-z,-2)*trans1_integrand(x,a)

def PartA():
    x = np.linspace(0,5,1000)
    two = integrand(x,2)
    three = integrand(x,3)
    four = integrand(x,4)
    plt.plot(x, two, label="a=2")
    plt.plot(x, three, label="a=3")
    plt.plot(x, four, label="a=4")
    plt.legend()
    plt.savefig("Prob2PartA.png")

def Gamma(a):
    points, weights = np.polynomial.legendre.leggauss(20)
    upper = 1
    lower = 0
    rescaled_points = 0.5*(upper-lower)*points+0.5*(upper+lower)
    rescaled_weights = 0.5*(upper-lower)*weights
    return np.dot(transformed_integrand(rescaled_points, a), rescaled_weights)


if __name__ == "__main__":
    PartA()
    print("Gamma(1.5)", Gamma(1.5))
    print("Gamma(3)", Gamma(3))
    print("Gamma(6)", Gamma(6))
    print("Gamma(10)", Gamma(10))

