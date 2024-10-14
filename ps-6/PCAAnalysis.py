from astropy.io import fits
import numpy as np
import scipy
import matplotlib.pyplot as plt
import time

def read_data():
    hdu_list = fits.open("specgrid.fits")
    logwave = hdu_list["LOGWAVE"].data
    flux = hdu_list["FLUX"].data
    return logwave, flux

def plot_random(logwave, flux):
    galaxies = np.random.choice(flux.shape[0],5)
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

def DirectEigen(residuals):
    C = np.matmul(np.transpose(residuals), residuals)*(1.0/residuals.shape[0])
    t1 = time.time()
    value, vectors =  np.linalg.eig(C)
    t2 = time.time()
    return value, vectors, t2-t1

def plot_eigenvectors(logwave, eigen_matrix):
    counter = 0
    for galaxy in range(0,5):
        plt.clf() 
        plt.plot(logwave, flux[galaxy,:])
        plt.savefig("PartD_Eigen_"+str(counter)+".png")
        counter += 1

def SVD_Eigen(residuals):
    t1 = time.time()
    U,W,V = scipy.linalg.svd(residuals)
    t2 = time.time()
    return W*W, V, t2-t1

def plot_eigenvectors_SVD(logwave, eigen_matrix):
    counter = 0
    for galaxy in range(0,5):
        plt.clf() 
        plt.plot(logwave, flux[galaxy,:])
        plt.savefig("PartE_Eigen_"+str(counter)+".png")
        counter += 1

if __name__ == "__main__":
    logwave, flux = read_data()
# A
    plot_random(logwave, flux)
# B
    normed_flux, norm_constants = Normalization(flux)
# C
    residuals, mean = RemoveMean(normed_flux)
# D
#    values, vectors, time_taken = DirectEigen(residuals)
#    plot_eigenvectors(logwave, vectors)
#    print("Time Taken: {t}. Condition Number: {cond}".format(t=time_taken, cond = np.max(values)/np.min(values)))
# E
    eigen_values, eigenvectors, time_taken_SVD = SVD_Eigen(residuals)
#    print(eigenvectors.shape)
#    plot_eigenvectors_SVD(logwave, eigenvectors)
#    print("Time Taken: {t}. Condition Number: {cond}".format(t=time_taken_SVD, cond = np.max(eigen_values)/np.min(eigen_values)))
    print(eigen_values.shape)
