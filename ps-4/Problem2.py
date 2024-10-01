import numpy as np
import matplotlib.pyplot as plt

def integrand(value, a):
    return np.power(np.sqrt(np.power(a,4) - np.power(value,4)), -1)


def period(amp, N = 20):
    points, weights = np.polynomial.legendre.leggauss(N)
    upper = amp
    lower = 0
    rescaled_points = 0.5*(upper-lower)*points+0.5*(upper+lower)
    rescaled_weights = 0.5*(upper-lower)*weights
    return np.sqrt(8)*  np.dot(integrand(rescaled_points, upper), rescaled_weights)

def ampPlot(N=20):
    amps = np.linspace(0,2,100)
    periods = [period(a,N) for a in amps]
    plt.plot(amps, periods)
    plt.title("Amp vs. Period. N=20")
    plt.xlabel("Amplitude")
    plt.ylabel("Period (s)")
    plt.savefig("Amplitudes.png")

if __name__ == "__main__":
    ampPlot(20)
