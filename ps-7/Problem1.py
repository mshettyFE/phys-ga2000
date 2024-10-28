import numpy as np

# kg
EARTH_MASS = 5.974E24
MOON_MASS = 7.348E22
SUN_MASS = 1.989E30
JUPITER_MASS = 1.898E27

# m
EARTH_MOON_DIST = 3.844E8
SUN_EARTH_DIST = 1.5E11


def f(r_prime, m_prime):
    a = np.power(1-r_prime,2)
    return -np.power(r_prime,3)*a+a-m_prime*np.power(r_prime,2)
# r^3(1-r)^2+(1-r)^2-m r^2

def f_prime(r_prime, m_prime):
    return -5*np.power(r_prime,4)+8*np.power(r_prime,3)-3*np.power(r_prime,2)+(2-2*m_prime)*r_prime-2

def Newton(initial, func, func_prime, m_prime, iters = 100):
    r_prime = np.array([initial])
    print("M_PRIME: ", m_prime)
    for i in range(iters):
        r_prime = r_prime - func(r_prime, m_prime)/ func_prime(r_prime, m_prime)
    return r_prime[0]

if __name__ == "__main__":
    print("Distances in meters")
    print("EARTH_MOON",EARTH_MOON_DIST*Newton(10,f, f_prime, MOON_MASS/EARTH_MASS))
    print("SUN_EARTH",SUN_EARTH_DIST*Newton(10,f, f_prime, EARTH_MASS/SUN_MASS))
    print("SUN_JUPITERLIKE",SUN_EARTH_DIST*Newton(10,f, f_prime, JUPITER_MASS/SUN_MASS))

