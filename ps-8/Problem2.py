import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    piano_data = np.genfromtxt("piano.txt", delimiter='\n')
    fft_piano_data = np.abs(np.fft.fft(piano_data))
    trumpet_data = np.genfromtxt("trumpet.txt", delimiter="\n")
    fft_trumpet_data = np.abs(np.fft.fft(trumpet_data))
    t = np.arange(piano_data.shape[0])
    timestep = 1/44100
    freq = np.fft.fftfreq(piano_data.size, timestep)
    fig, axs = plt.subplots(2,1)
    time = t*timestep
    axs[0].plot(time,piano_data, color='b', label="piano")
    axs[0].plot(time, trumpet_data, color='r', label = "trumpet")
    axs[0].set_xlabel("time")
    axs[0].set_ylabel("Amp")
    axs[0].legend()

    limit = int(freq.shape[0]/2)
    axs[1].plot(freq[:limit], fft_piano_data[:limit], color='b', label="piano")
    axs[1].plot(freq[:limit], fft_trumpet_data[:limit], color='r', label="trumpet")
    axs[1].set_xscale("log")
    axs[1].set_yscale("log")
    axs[1].set_xlabel("Freq")
    axs[1].set_ylabel("Mag")
    axs[1].legend()

    plt.tight_layout()
    plt.savefig("Problem2.png")
