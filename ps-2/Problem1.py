import numpy as np

starting = 100.98763
numpy_starting = np.float32(starting)

def get_bits(number):
    # Taken directly from class notes
    """For a NumPy quantity, return bit representation
    
    Inputs:
    ------
    number : NumPy value
        value to convert into list of bits
        
    Returns:
    -------
    bits : list
       list of 0 and 1 values, highest to lowest significance
    """
    btes = number.tobytes()
    bits = []
    for byte in btes:
        bits = bits + np.flip(np.unpackbits(np.uint8(byte)), np.uint8(0)).tolist()
    return list(reversed(bits))

def get_bits_pretty(number):
    out = get_bits(number);
    rev = list(reversed(out))
    # Transform [0-1] to [1,-1]
#    sign = (rev[31]-0.5)*-2
    sign = rev[31]
    exponent = list(reversed(rev[23:31]))
    mantissa = list(reversed(rev[0:23]))
    return sign, exponent, mantissa

if __name__ == "__main__":
    print("Starting", starting)
    print("Total bits", get_bits(numpy_starting))
    s,e,m = get_bits_pretty(numpy_starting)
    print("\nBits split up\n")
    print(s)
    print(e)
    print(m)
