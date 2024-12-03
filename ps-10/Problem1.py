import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.animation import Animation

time_step_size = 1E-17
N_time = 1000
t_max = time_step_size*N_time
box_dim = 1E-8
N_space = 100
space_step_size = box_dim/N_space
hbar = 1.05E-34
electron_mass = 9.109E-31
kappa = 5E10
sigma = 1E-10

global_state = 0


fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], animated=True)
ax.set_xlim(-box_dim/2, 1.5*box_dim)
ax.set_ylim(-1, 1)
ax.set_xlabel('x')
ax.set_ylabel('Re($\\Psi$)')
ax.set_title("Gaussian In Box")

x_span  = np.linspace(0,box_dim,num=N_space)+np.ones(N_space)*space_step_size

def gen_A(dimensionality, space_step_size, time_step_size, mass):
    factor = time_step_size*1j*hbar/(mass*np.power(space_step_size,2))
    a1 = 1+factor/2
    a2 = -factor/4
    output = np.zeros((dimensionality,dimensionality), dtype=np.complex128)
    for i in range(dimensionality):
        output[i,i] = a1
        if(i==0):
            output[i,i+1] = a2
        elif(i==dimensionality-1):
            output[i,i-1] = a2
        else:
            output[i,i+1] = a2
            output[i,i-1] = a2
    return output

def gen_B(dimensionality, space_step_size, time_step_size, mass):
    factor = time_step_size*1j*hbar/(mass*np.power(space_step_size,2))
    b1 = 1-factor/2
    b2 = factor/4
    output = np.zeros((dimensionality,dimensionality), dtype=np.complex128)
    for i in range(dimensionality):
        output[i,i] = b1
        if(i==0):
            output[i,i+1] = b2
        elif(i==dimensionality-1):
            output[i,i-1] = b2
        else:
            output[i,i+1] = b2
            output[i,i-1] = b2
    return output

def gen_initial_cond():
    x_0 = box_dim/2
    real_power = -np.power(x_span-x_0,2)/(2*sigma*sigma)
    img_power = kappa*1j*x_span
    output = np.exp(real_power)*np.exp(img_power)
    return output

def step_Crank(A_inv,B, state):
    v = np.matmul(B,state)
    output=  np.matmul(A_inv,v)
    return output

def init():
    global global_state
    global_state = gen_initial_cond()
    ln.set_data([], [])
    return ln,

def update(frame):
    xdata = [x_span]
#    xdata.append(x_span)
    global global_state
    global_state = step_Crank(A_inv,B,global_state)
    global_state[0] = 0
    global_state[-1] = 0
    ydata = [np.real(global_state)]
#    ydata.append(np.real(global_state))
    ln.set_data(xdata, ydata)
    return ln,

# Define the A and B matrices globally
A = gen_A(N_space, space_step_size, time_step_size, electron_mass)
A_inv = np.linalg.inv(A)
B = gen_B(N_space,space_step_size, time_step_size, electron_mass)

if __name__ == "__main__":
    time_range = np.arange(0,t_max,step=time_step_size)
    ani = FuncAnimation(fig, update, init_func=init, frames=time_range,interval=50, blit=True)
    Animation.save(ani, "Problem1.mp4")