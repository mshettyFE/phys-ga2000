from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt

def read_data():
    hdu_list = fits.open("specgrid.fits")
    logwave = hdu_list["LOGWAVE"].data
    flux = hdu_list["FLUX"].data
    return logwave, flux

def plot_random(logwave, flux):
    galaxies = np.random.choice(flux.shape[1],5)
    counter = 0
    for galaxy in galaxies:
        plt.clf() 
        plt.plot(logwave, flux[galaxy,:])
        plt.savefig("Galaxy_"+str(counter)+".png")
        counter += 1

def Normalization(flux):
    normalization = flux.sum(axis=1)
    return flux/normalization[:,None], normalization

def RemoveMean(flux):
    mean = np.mean(flux, axis=1, keepdims = True)
    return flux-mean, mean

if __name__ == "__main__":
    logwave, flux = read_data()
    plot_random(logwave, flux)
    normed_flux, norm_constants = Normalization(flux)
    centered_normed_flux, mean = RemoveMean(normed_flux)
