import numpy as np
from matplotlib import pyplot as plt


def gen_gaussian(x_range, mu, sigma):
    assert sigma != 0
    prefactor  = 1.0/( sigma * np.sqrt(np.pi) )
    z_score = np.divide(np.subtract(x_range, mu), sigma)
    z_score_squared = np.square(z_score)
    inner_factor = -0.5*z_score_squared
    return prefactor*np.exp(inner_factor)


if __name__ == "__main__":
    x_range = np.linspace(-10,10,1000)
    y_range = gen_gaussian(x_range, 0, 3)
    plt.plot(x_range, y_range)
    plt.savefig("gaussian.png")
