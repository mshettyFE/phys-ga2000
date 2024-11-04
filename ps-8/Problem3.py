import numpy as np
import matplotlib.pyplot as plt

def plot_data(data):
    plt.plot(data)
    plt.savefig("Dow.png")
    plt.clf()

def low_pass_filter(data, culling_percentage=0.1):
    coeffs = np.fft.rfft(data)
    limit = int(coeffs.size*culling_percentage)
    coeffs[limit:] = 0
    return coeffs
    
def plot_filtered_data(data, filtered, title):
    plt.plot(data, color='r' , label="Original")
    plt.plot(filtered, color='b', label="Filtered")
    plt.legend()
    plt.savefig(title+".png")
    plt.clf()

if __name__ == "__main__":
    data = np.genfromtxt("dow.txt", delimiter="\n")
    plot_data(data)

    coeffs = low_pass_filter(data)
    filtered_data = np.fft.irfft(coeffs)
    plot_filtered_data(data, filtered_data, "TenPercent")
    
    coeffs = low_pass_filter(data, 0.02)
    filtered_data = np.fft.irfft(coeffs)
    plot_filtered_data(data, filtered_data, "TwoPercent")

