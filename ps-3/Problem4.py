import numpy as np
import matplotlib.pyplot as plt

N = 400
samples = 10000

def gen_y(N):
    assert(N >=1)
    return np.sum(np.random.exponential(scale=1.0,size=N))/N

def plot_gaussian(N,samples):
    sampling = np.array([gen_y(N) for index in range(samples)])
    plt.hist(sampling, bins = 100)
    plt.savefig("CLTVisual.png")

def moment_calculations(N_max, samples):
    mean = []
    var = []
    skew = []
    kurt = []
    N_range = np.arange(1, N_max)
    for n in N_range:
        sampling = np.array([gen_y(n) for index in range(samples)])
        new_mean = np.sum(sampling)/samples
        new_var = np.sum(np.square(sampling-new_mean))/samples
        new_skew = (np.sum(np.power(sampling-new_mean,3))/samples)/new_var**1.5
        new_kurt = (np.sum(np.power(sampling-new_mean,4))/samples)/new_var**2-3
        mean.append(new_mean)
        var.append(new_var)
        skew.append(new_skew)
        kurt.append(new_kurt)
    return N_range, np.array(mean), np.array(var), np.array(skew), np.array(kurt)

if __name__ == "__main__":
    plot_gaussian(N, samples)
    n, mu, sigma, skew, kurt = moment_calculations(N, samples)
    fig, axs  = plt.subplots(2,2)
    axs[0,0].plot(n, mu)
    axs[0,0].set_title("Mean")
    axs[0,0].set_xlabel("N")

    axs[0,1].plot(n, sigma)
    axs[0,1].set_title("Sigma")
    axs[0,1].set_xlabel("N")
    
    axs[1,0].plot(n, skew)
    axs[1,0].set_title("Skew")
    axs[1,0].axhline(y = skew[0]*0.01, color = 'r')
    axs[1,0].set_xlabel("N")
    
    axs[1,1].plot(n, kurt)
    axs[1,1].set_title("Kurt")
    axs[1,1].set_xlabel("N")
    axs[1,1].axhline(y = kurt[0]*0.01, color = 'r')
    
    fig.tight_layout()
    plt.show()
