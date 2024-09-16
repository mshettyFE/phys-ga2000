from matplotlib import pyplot as plt
import numpy as np

resolution = 10000
iterations = 10
diverging_criterion = 2
re_min = -2
re_max = 2
im_min = -2
im_max = 2
 
def man_plot():
    # Set up Grid of points to probe
    x = np.linspace(re_min, re_max, resolution, dtype = np.float32)
    y = np.linspace(im_min, im_max, resolution, dtype = np.float32)
    re, im = np.meshgrid(x,y)
    start = re+ im*1j
    # Set up initial state and output array keeping track of diverging points
    state = np.zeros(start.shape)
    output = np.ones(state.shape)
    # Do the thing
    for iteration in range(0,iterations):
        state = state*state+start
        # Clamp values above diverging_criterion to be 0
        output[np.absolute(state) > diverging_criterion ] = 0
    return re, im, output

if __name__=="__main__":
    x,y, state = man_plot()
    plt.imshow(state)
    plt.show()
