import numpy as np
import struct

starting = 100.98763


def binaryPrint(number):
# Adapted from here. Comments for better clarity
# https://stackoverflow.com/questions/16444726/binary-representation-of-float-in-python-bits-not-hex
#   Does the actual conversion of floating point number to string. Outputs in hex
    bits = struct.pack('!f', number)
# Formats the hex string into a binary string
    output = ''.join('{:0>8b}'.format(c) for c in bits)
    return output

def BackAndForth():
    print("Starting {num}".format(num=starting))
    bits = struct.pack('!f', starting)
    reversed = struct.unpack("!f", bits)
    print("Ended with {num}".format(num=reversed))

if __name__ == "__main__":
# https://numpy.org/doc/stable/reference/arrays.scalars.html
    val = np.float32(starting)
    print(binaryPrint(starting))
    BackAndForth()

