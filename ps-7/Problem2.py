import numpy as np
from  scipy.optimize import brent as sp_brent

def golden_section_step(a,b,c):
    w = (3-np.sqrt(5))/2
    z = 1-2*w
    b = w*(c-a)+a
    x = z*(c-a)+b
    if (f(x) < f(b)):
# Shift left boundary over
        a = b
    else:
# Shift right boundary over
        c = b
    b = w*(c-a)+a
    return (a,b,c)

def brent(f, a, c, max_iters = 500, tol =1E-4):
    assert(c > a)
    w = (3-np.sqrt(5))/2
    z = 1-2*w
    b = w*(c-a)+a
    assert(f(b) < f(c))
    assert(f(a) < f(c))
    for i in range(max_iters):
        a,b,c = golden_section_step(a,b,c)
    return b

def f(x):
#    return np.power(x-0.3,2)*np.exp(x)
    return np.power(x-0.3,2)


if __name__ == "__main__":
    print(brent(f, 0,1))
    print(sp_brent(f,brack=(0,1)))
