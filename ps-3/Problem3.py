import numpy as np
import matplotlib.pyplot as plt

lifetime = 3.053*60
atoms = 1000
total_time_steps = 1000

def gen_decay_times(size, decay_time):
    beta =  decay_time/np.log(2)
    return np.random.exponential(beta, size)

if __name__ == "__main__":
    when_it_will_decay = gen_decay_times(atoms, lifetime)
    b = np.sort(when_it_will_decay)
    time = np.arange(total_time_steps)
    remaining = np.array([np.sum(b>= t) for t in time])
    plt.plot(time, remaining)
    plt.show()
