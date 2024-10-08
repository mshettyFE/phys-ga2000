import numpy as np
import jax.numpy as jnp
from jax import grad
import matplotlib.pyplot as plt

h = 0.001

def f(x):
    return 1+0.5*np.tanh(2*x)

def jax_f(x):
    return 1+0.5*jnp.tanh(2*x)

def central_diff(func, x, h):
    left = x-0.5*h
    right = x+0.5*h 
    return (func(right)-func(left))/h

def f_prime(x):
    return np.power(np.cosh(2*x),-2)

if __name__== "__main__":
    x = np.linspace(-10,10,2000)
    numerical = central_diff(f, x, h)
    analytical = f_prime(x)
    jax_der = grad(jax_f)
    jax_val = np.array([jax_der(i) for i in x])
    resi1 = numerical -analytical
    resi2 = jax_val-  analytical
    fig, ax = plt.subplots(1,2)
    ax[0].plot(x,numerical,'b+', label="Central Difference")
    ax[0].plot(x, analytical, 'r-', label="Analytic")
    ax[0].plot(x, jax_val, 'g*', label = "Jax")
    ax[0].set_title("f'(x)")
    ax[0].set_xlabel("x")
    ax[0].set_ylabel("f'(x)")
    ax[0].legend()
    ax[1].plot(x, resi1, 'r', label = "Residual Central")
    ax[1].plot(x, resi2, 'b', label = "Residual Jax")
    ax[1].set_title("Residuals Compared to Analytic")
    ax[1].set_xlabel("x")
    ax[1].set_ylabel("Residuals")
    ax[1].legend()
    plt.tight_layout()
    plt.savefig("Derivatives.png")
