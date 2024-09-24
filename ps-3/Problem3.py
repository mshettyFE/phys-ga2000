import numpy as np
import matplotlib.pyplot as plt

# in seconds
lifetime = 3.053*60

# Initial array of atoms
atoms = 1000

# Total simulation steps
total_time_steps = 1000

def gen_decay_times(size, decay_time):
# Need to scale the beta parameter by log(2) to draw from 2**(-x) distribution
    beta =  decay_time/np.log(2)
    return np.random.exponential(beta, size)

if __name__ == "__main__":
    when_it_will_decay = gen_decay_times(atoms, lifetime)
    time = np.arange(total_time_steps)
    # At each time step, count how many atoms have decay times greater than the current time step
    remaining = np.array([np.sum(when_it_will_decay>= t) for t in time])
    plt.plot(time, remaining)
    plt.xlabel("Time  (s)")
    plt.ylabel("Remaining Tl atoms")
    plt.title("Tl Decay")
    plt.show()
