import numpy as np
import timeit
# https://en.wikipedia.org/wiki/Madelung_constant

L = 50
debug = False


def SolutionWithFor():
    Running_tally = 0.0
    for x in range(-L,L+1):
        for y in range(-L,L+1):
            for z in range(-L,L+1):
                if (x==0 and y==0 and z==0):
                    continue
                Running_tally += np.power(-1.0, x+y+z+1)/np.sqrt(np.square(x)+np.square(y)+np.square(z))                
    return Running_tally


def SolutionPureNumpy():
    side = np.arange(-L,L+1, dtype = np.float32)
    x,y,z = np.meshgrid(side, side,side)
    v = np.sqrt(np.square(x)+np.square(y)+np.square(z))/np.power(-1, x+y+z+1)
    v = 1.0/v[v!= 0]
    return np.sum(v)


if __name__ == "__main__":    
    print("Solving with For loop")
    print("Solution: {}".format(SolutionWithFor()))
    print("Solving without For loop")
    print("Solution: {}".format(SolutionPureNumpy()))
    print(timeit.timeit(lambda: SolutionWithFor(), number = 5))
    print(timeit.timeit(lambda: SolutionPureNumpy(), number = 5))

