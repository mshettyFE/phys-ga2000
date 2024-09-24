import numpy as np
import matplotlib.pyplot as plt

# Kelvin
AlDebyeTemp = 428

# m^3
Volume  = (1000) / (1E6)

# number density (atoms/m^3)
Rho  = 6.022E28

# J/K
kb = 1.380649E-23

# m^3 * (1/m^3) * J/K = J/K
ConstPrefactor = 9 * Volume*Rho * kb

def integrand(x):

    top = np.power(x, 4)*np.exp(x)
    bot = np.power(np.expm1(x), 2)
    return top/bot


def cv(T, N=50):

    assert(T != 0)
    a = 0
    b = AlDebyeTemp/T
    Prefactor = ConstPrefactor* np.power(T/AlDebyeTemp,3)

    #https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.leggauss.html
    points, weights = np.polynomial.legendre.leggauss(N)
    rescaled_points = 0.5*(b-a)*points+0.5*(b+a)
    rescaled_weights = 0.5*(b-a)*weights
    return Prefactor*np.dot(integrand(rescaled_points), rescaled_weights)

def genCvPlot(N):
    temps = np.linspace(5,500,100)
    values = np.array([cv(t, N) for t in temps])
    plt.plot(temps, values)
    plt.savefig("SpecificHeatPlot.png")

def convergence():
    N  = [10,20,30,40,50,60,70]
    target_temps = [5]
    plt.clf()
    for t in target_temps:
        values = [cv(t,n) for n in N]
        plt.plot(N, values)
    plt.yscale("log")
    plt.savefig("ConvergenceProb1.png")

if __name__ == "__main__":
    genCvPlot(50)
    convergence()

