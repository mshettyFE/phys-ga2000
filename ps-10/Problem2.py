import numpy as np
from scipy.fft import dst
from scipy.fft import idst
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

def gen_initial_cond():
    x_0 = box_dim/2
    real_power = -np.power(x_span-x_0,2)/(2*sigma*sigma)
    img_power = kappa*1j*x_span
    output = np.zeros(x_span.shape, dtype=np.complex128)
    output = np.exp(real_power)*np.exp(img_power)
    return output

def gen_coefficients():
    data = gen_initial_cond()

    alpha = dst(np.real(data))
    eta = dst(np.imag(data))
    return alpha+ 1j*eta

coeffs = gen_coefficients()

def gen_wavefunc(cur_time):
    output = np.zeros(x_span.shape, dtype=np.complex128)
    for k,bk in enumerate(coeffs):
        exp_coeff = 1j*np.power(np.pi,2)*hbar*np.power(k,2)*cur_time/2/electron_mass/np.power(box_dim,2)
        sin_coeff = np.pi*k*x_span/box_dim
        output += bk*np.sin(sin_coeff)*np.exp(exp_coeff)
    return output/N_space

def init():
    global global_state
    global_state = gen_initial_cond()
    ln.set_data([], [])
    return ln,

def update(frame):
    xdata = [x_span]
    global global_state
    global_state = gen_wavefunc(frame)
    global_state[0] = 0
    global_state[-1] = 0
    ydata = [np.real(global_state)]
    ln.set_data(xdata, ydata)
    return ln,

if __name__ == "__main__":
    time_range = np.arange(0,t_max,step=time_step_size)
    ani = FuncAnimation(fig, update, init_func=init, frames=time_range,interval=50, blit=True)
    Animation.save(ani, "Problem2.mp4")
