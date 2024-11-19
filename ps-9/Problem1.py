import numpy as np
import matplotlib.pyplot as plt

OMEGA = 1
DELTA_T = 0.001

# r = [x,y]

def dx_dt(r,t,args):
    return r[1]

def dy_dt_parta(r,t,args):
    return -OMEGA*OMEGA*r[0]

def dy_dt_partc(r,t,args):
    return -OMEGA*OMEGA*(r[0]*r[0]*r[0])

def dy_dt_parte(r,t,args):
    x = r[0]
    y = r[1]
    return args["mu"]*(1-x*x)*y-OMEGA*OMEGA*x


def RK2(derivative_dx, derivative_dy,r,t, dt,args):
    dx_start = derivative_dx(r,t,args)
    dy_start = derivative_dy(r,t,args)
    k1 = np.array([dx_start,dy_start])

    dx_end = derivative_dx(r+k1*dt, t+dt,args)
    dy_end = derivative_dy(r+k1*dt, t+dt,args)
    k2 = np.array([dx_end,dy_end])
    
    return t+dt , r+dt*(0.5*k1+0.5*k2)

def integrate(delta_y, initial_conds,args={},t_max=50):
    r = initial_conds
    t = 0
    t_min = 0
    dt = DELTA_T
    N_steps = int((t_max-t_min)/dt)
    n_out = np.zeros((N_steps+1,3))
    n_out[0,0] = t
    n_out[0,1] = r[0]
    n_out[0,2] = r[1]
    for i in range(N_steps):
        t, r = RK2(dx_dt,delta_y,r,t,dt,args)
        n_out[i+1,0] = t
        n_out[i+1,1] = r[0]
        n_out[i+1,2] = r[1]
    return n_out

def plot(mesh, title, fname, clear= True):
    t = mesh[:,0]
    x = mesh[:,1]
    if (clear):
        plt.clf()
    plt.plot(t,x)
    plt.title(title)
    plt.xlabel("time")
    plt.ylabel("position")
    plt.savefig(fname+".png")

def plot_phase(mesh, title, fname, clear= True):
    x = mesh[:,1]
    p = mesh[:,2]
    if (clear):
        plt.clf()
    plt.scatter(x,p)
    plt.title(title)
    plt.xlabel("position")
    plt.ylabel("velocity")
    plt.savefig(fname+".png")

if __name__ == "__main__":
    mesh = integrate(dy_dt_parta,np.array([1,0]))
    plot(mesh, "Part A", "PartA")
    mesh = integrate(dy_dt_parta,np.array([2,0]))
    plot(mesh, "Part B", "PartB", False)
    mesh = integrate(dy_dt_partc,np.array([1,0]))
    plot(mesh, "Part Ci", "PartCi")
    mesh = integrate(dy_dt_partc,np.array([2,0]))
    plot(mesh, "Part Ci", "PartCii", False)
    mesh = integrate(dy_dt_parta,np.array([1,0]))
    plot_phase(mesh, "Part D", "PartD")
    mesh = integrate(dy_dt_parte,np.array([1,0]), args={"mu": 1}, t_max=20)
    plot_phase(mesh, "Part Ei", "PartEi")
    mesh = integrate(dy_dt_parte,np.array([1,0]), args={"mu": 2}, t_max=20)
    plot_phase(mesh, "Part Eii", "PartEii")
    mesh = integrate(dy_dt_parte,np.array([1,0]), args={"mu": 4}, t_max=20)
    plot_phase(mesh, "Part Eiii", "PartEiii")