import numpy as np
import matplotlib.pyplot as plt

def crappy_read_csv(fname):
    left = []
    right = []
    with open(fname, 'r') as f:
        line = f.readline()
        while len(line) != 0:
            split_up = line.split(",")
            left.append(float(split_up[0]))
            right.append(float(split_up[1]))
            line = f.readline()
    return np.array(left), np.array(right)

def graph_with_fit(x,y, clear = False):
    if clear:
        plt.clear()
    p = np.polyfit(x,y,3)
    cubic_fit = p[0]*np.power(x,3)
# https://stackoverflow.com/questions/893657/how-do-i-calculate-r-squared-using-python-and-numpy
    plt.plot(x,y, color = 'blue')
    plt.plot(x, cubic_fit, color = 'red')


if __name__ == "__main__":
    l,r = crappy_read_csv("Explicit.csv")
    graph_with_fit(l,r)
    plt.show()


