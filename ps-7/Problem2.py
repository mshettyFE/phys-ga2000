import numpy as np
from  scipy.optimize import brent as sp_brent

def brent(f, a, b, c, max_iters = 500, tol =1E-4):
    assert(f(b) < f(a))
    assert(f(b) < f(c))
    for i in range(max_iters):
        print(a,b,c)
        w = (b-a)/(c-a)
        x_new = (1-2*w)*(c-a)+b
        print(w, x_new)
        if(abs(x_new-b) < 1E-4):
            break
        if x_new > b:
            a = b
        else:
            c = b
        b = (c+a)/2
    return b

def f(x):
#    return np.power(x-0.3,2)*np.exp(x)
    return np.power(x-0.3,2)


if __name__ == "__main__":
    print(brent(f, 0,0.5,1))
    print(sp_brent(f,brack=(0,1)))
