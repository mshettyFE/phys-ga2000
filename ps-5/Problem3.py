import numpy as np
import matplotlib.pyplot as plt

def parse_data(filename):
    time = []
    sig = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines[1:]:
            split = line.split("|")
            time.append(float(split[1].strip()))
            sig.append(float(split[-2].strip()))
    return np.array(time), np.array(sig)

def plot_data(time, signal):
    plt.clf()
    plt.scatter(time, signal)
    plt.xlabel("Time")
    plt.ylabel("Signal")
    plt.title("Signal Vs. Time")
    plt.savefig("Signal.png")
    plt.clf()

def scale_time(t):
    return (t-np.mean(t))/np.std(t)

def FourierDesignMatrix(dim , t):
    A = np.zeros((len(time), dim))
    Period = (np.max(t)-np.min(t))/2
    for n in range(0,A.shape[1],2):
        A[:,n] = np.cos(t* 2*n*np.pi/Period)
        A[:,n+1] = np.sin(t* 2*n*np.pi/Period)
    return A

def polyDesignMatrix(dim , t):
    A = np.zeros((len(time), dim))
    for n in range(0,A.shape[1]):
        A[:,n] = np.power(t,n)
    return A

def SVDPoly(time, signal, dim):
    t = scale_time(time)
    A = polyDesignMatrix(dim, t)
    (u,w,vt) = np.linalg.svd(A, full_matrices=False)
    condition_number = np.max(w)/np.min(w)
    ainv = vt.transpose().dot(np.diag(1. / w)).dot(u.transpose())
    x = ainv.dot(signal)
    fit = A.dot(x)

    plt.clf()
    fig, axs = plt.subplots(2,1)
    axs[0].scatter(t, signal)
    axs[0].scatter(t,fit)
    cur_title = str("Condition Number {num}".format(num=condition_number))
    axs[0].set_title(cur_title)
    axs[1].scatter(t,signal-fit)
    cur_title = "PolySVD_{num}.png".format(num=dim)
    plt.savefig(cur_title)

def SVDFourier(time, signal, dim):
    t = scale_time(time)
    A = FourierDesignMatrix(dim, t)
    (u,w,vt) = np.linalg.svd(A, full_matrices=False)
    ainv = vt.transpose().dot(np.diag(1. / w)).dot(u.transpose())
    x = ainv.dot(signal)
    fit = A.dot(x)

    plt.clf()
    fig, axs = plt.subplots(2,1)
    axs[0].scatter(t, signal)
    axs[0].scatter(t,fit)
    axs[0].set_title("Fourier Decomposition")
    axs[1].scatter(t,signal-fit)
    cur_title = "FourierSVD_{num}.png".format(num=dim)
    plt.savefig(cur_title)


if __name__ == "__main__":
    time, signal = parse_data("signal.dat")
    plot_data(time, signal)
    SVDPoly(time, signal, 3)
    SVDPoly(time, signal, 20)
    SVDFourier(time, signal, 10)
