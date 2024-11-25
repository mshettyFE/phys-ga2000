import numpy as np
import matplotlib.pyplot as plt

# r = [x0,x1, y0, y1]

R = 8/100 # Radius of Ball (m)
rho = 1.22 # kg/m^{3}
g = 9.8 # m/s^2

# C is drag coefficient
# m is mass in kg
args = {"C": .47, "m":1}

def dx0_dt(r,t,args):
    return r[1]
def dx1_dt(r,t,args):
    vel_squared = np.power(r[1],2)+np.power(r[3],2)
    return -r[1]*np.sqrt(vel_squared)
def dy0_dt(r,t,args):
    return r[3]
def dy1_dt(r,t,args):
    gamma = R*R*rho*args["C"]*g/args["m"]
    vel_squared = np.power(r[1],2)+np.power(r[3],2)
    return -gamma-(np.pi/2)*r[3]*np.sqrt(vel_squared)

def RK2(derivatives, r,t, dt,args):
    update = []
    for derivative in derivatives:
        k1 =  derivative(r,t,args)
        k2 = derivative(r+k1*dt, t+dt,args)
        update.append(dt*(0.5*k1+0.5*k2))
    return t+dt , r+np.array(update)

def integrate(ders, initial, args, dt, nsteps):
    cur  = initial
    output  = np.zeros((len(ders),nsteps))
    cur_time = 0
    for i in range(nsteps):
        output[:,i] = cur
        cur_time, cur = RK2(ders, cur, cur_time, dt, args)
    return output

def plot_traj(x,y, title, fig_name, clear=True, label = None, save=False):
    if (clear):
        plt.clf()
    plt.title(title)
    plt.xlabel("x'")
    plt.ylabel("y'")
    if label:
        plt.scatter(x,y, label=label)
    else:
        plt.scatter(x,y)
    if (save):
        plt.savefig(fig_name+".png")

def conversion(args):
    return  np.sqrt((args["m"]*g)/(R*R*rho*args["C"]))

if __name__=="__main__":
# Part b
    initial_vel_y = 100*np.sin(np.deg2rad(30))/conversion(args)    
    initial_vel_x = 100*np.cos(np.deg2rad(30))/conversion(args)

    r0 = np.array([0,initial_vel_x,1, initial_vel_y])
    ders = [dx0_dt, dx1_dt, dy0_dt, dy1_dt]
    mesh  = integrate(ders, r0, args, 0.001,10000)
    plot_traj(mesh[0,:], mesh[2,:], "Air Resistance Part B", "Prob2_Part_B", save=True)

# Part c
    plt.clf()
    mass_points = [.1, .5,1,3,5]
    mass_labels = [".1", ".5","1","3","5"]
    for i in range(len(mass_points)):
        args["m"] = mass_points[i]
        mesh  = integrate(ders, r0, args, 0.001,10000)
        plot_traj(mesh[0,:], mesh[2,:], "Air Resistance Part B", "Prob2_Part_B", False, mass_labels[i], save=False)
    plt.legend()
    plt.savefig("Prob2PartC.png")        