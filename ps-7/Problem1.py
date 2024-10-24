import numpy as np

EARTH_MASS = 5.974E24
MOON_MASS = 7.348E22
EARTH_RAD = 3.844E8

def f(r_prime, m_prime):
    a = np.power(1-r_prime,2)
    return np.power(r_prime,3)*a+a-m_prime*np.power(r_prime,2)

def f_prime(r_prime, m_prime):
    return 5*np.power(r_prime,5)-8*np.power(r_prime,4)+3*np.power(r_prime,3)+(2-2*m_prime)*r_prime-2

def Newton(initial, func, func_prime, m_prime, iters = 100):
    r_prime = np.array([initial])
    print("M_PRIME: ", m_prime)
    for i in range(iters):
        r_prime = r_prime - func(r_prime, m_prime)/ func_prime(r_prime, m_prime)
        print(i, r_prime)


if __name__ == "__main__":
    Newton(0,f, f_prime, MOON_MASS/EARTH_MASS) 

