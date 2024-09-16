import numpy as np

a = 0.001
b = 1000
c = 0.001

def partA(a,b,c):
    discriminant = b*b-4*a*c
    left = (-b + np.sqrt(discriminant))/(2*a)
    right = (-b - np.sqrt(discriminant))/(2*a)
    return left, right

def partB(a,b ,c):
    discriminant = b*b-4*a*c
    left = (2*c)/(-b - np.sqrt(discriminant))
    right = (2*c)/(-b + np.sqrt(discriminant))
    return left, right

def quadratic(a,b,c):
    discriminant = b*b-4*a*c
    if b >=0:
        left = (2*c)/(-b - np.sqrt(discriminant))
        right = (-b - np.sqrt(discriminant))/(2*a)
    else:
        left = (-b + np.sqrt(discriminant))/(2*a)
        right = (2*c)/(-b + np.sqrt(discriminant))
    return left, right

if __name__ == "__main__":
    left, right = partA(a,b,c) 
    print("\nPart a\n")
    print("Left {l}".format(l=left))
    print("Right {r}".format(r=right))
    left, right = partB(a,b,c)
    print("\nPart b\n")
    print("Left {l}".format(l=left))
    print("Right {r}".format(r=right))

