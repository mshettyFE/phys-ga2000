import numpy as np
from  scipy.optimize import brent as sp_brent

w = (3-np.sqrt(5))/2
z = 1-2*w

def golden_section_step(f,a,b,c):
    if (c<a):
        temp = a
        a = c
        c =temp
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

def parabolic_step(func=None, a=None, b=None, c=None):
    """returns the minimum of the function as approximated by a parabola"""
    fa = func(a)
    fb = func(b)
    fc = func(c)
    denom = (b - a) * (fb - fc) - (b -c) * (fb - fa)
    numerator = (b - a)**2 * (fb - fc) - (b -c)**2 * (fb - fa)
    # If singular, just return b 
    if(np.abs(denom) < 1.e-15):
        x = b
    else:
        x = b - 0.5 * numerator / denom
    return(x)

def brent(f, a, c, max_iters = 5000, tol =1E-4):
    assert(c > a)
    b = w*(c-a)+a
    assert(f(b) < f(c))
    assert(f(a) < f(c))
    for i in range(max_iters):
        x = parabolic_step(f,a,b,c)
        if x!=b:
            if (b < x):
# Shift left boundary over
                c = b
            else:
# Shift right boundary over
                a = b
            b= x
        else:
            a,b,c = golden_section_step(f,a,b,c)
    return (a+c)/2

def f(x):
    return np.power(x-0.3,2)*np.exp(x)
#    return np.power(x-0.3,2)


if __name__ == "__main__":
    print(brent(f, 0,1))
    print(sp_brent(f,brack=(0,1)))
