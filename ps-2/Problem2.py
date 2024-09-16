import numpy as np

def CloseToOne():
    small_eps = np.float32(5.9604645e-08)
    big_esp = np.float64(1.1102230246251565e-16)
    small_tiny = np.float32(1.1754944e-38)
    big_tiny = np.float64(2.2250738585072014e-308)
    one_small = np.float32(1)
    one_big = np.float64(1)
    print("Epsilon for 32-bit is {val1}, and for 64-bit is {val2}".format(val1 = small_eps, val2=big_esp))
    print("{Region}\t{small}\t{big}".format(Region="", small="32", big="64"))
    print("On par\t{val1}\t{val2}".format(val1=one_small+small_eps, val2=one_big+big_esp))
    print("Bigger\t{val1}\t{val2}\n".format(val1=one_small+small_eps*2, val2=one_big+big_esp*2))

if __name__ == "__main__":
    CloseToOne()
# https://numpy.org/doc/stable/reference/generated/numpy.finfo.html
    print(np.finfo(np.float32))
    print(np.finfo(np.float64))
