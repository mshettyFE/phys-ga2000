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
        plt.xlabel("log10 lambda")
        plt.ylabel("flux")
        plt.savefig("Galaxy_"+str(counter)+".png")
        counter += 1

def Normalization(flux, logwave):
    dx = logwave[1]-logwave[0]
    normalization = flux.sum(axis=1)*dx
    return flux/normalization[:,None], normalization

def RemoveMean(flux):
    mean = np.mean(flux, axis=1, keepdims = True)
    return flux-mean, mean

def DirectEigen(residuals):
    C = np.matmul(np.transpose(residuals), residuals)*(1.0/residuals.shape[0])
    t1 = time.time()
    value, vectors =  np.linalg.eigh(C)
    t2 = time.time()
    return value, vectors, t2-t1

def plot_eigenvectors(logwave, eigen_matrix):
    counter = 0
    for galaxy in range(0,5):
        plt.clf() 
        plt.plot(logwave, flux[galaxy,:])
        plt.title(str(counter))
        plt.xlabel("log10 lambda")
        plt.ylabel("flux")
        plt.savefig("PartD_Eigen_"+str(counter)+".png")
        counter += 1

def SVD_Eigen(residuals):
    t1 = time.time()
    U,W,V = scipy.linalg.svd(residuals)
    t2 = time.time()
    return W, V.T, t2-t1

def plot_eigenvectors_SVD(logwave, eigen_matrix):
    counter = 0
    for galaxy in range(0,5):
        plt.clf() 
        plt.plot(logwave, flux[galaxy,:])
        plt.title(str(counter))
        plt.xlabel("log10 lambda")
        plt.ylabel("flux")
        plt.savefig("PartE_Eigen_"+str(counter)+".png")
        counter += 1

def reconstruct(N_c, eigenvectors,residuals, mean, normalization):
    selected_eigenvectors = eigenvectors[:,:N_c]
    coefficients = np.matmul(residuals, selected_eigenvectors)
    rotated = np.matmul(coefficients, np.transpose(selected_eigenvectors))
    shifted =  (rotated+ mean)
    normalization = normalization.reshape(normalization.shape[0],1)
    output = np.multiply(normalization, shifted)
    return output , coefficients

def plot_coeffs(coeffs):
    plt.clf()
    figs, axs = plt.subplots(2)
    axs[0].set_xlabel("c0")
    axs[1].set_xlabel("c0")
    axs[0].set_ylabel("c1")
    axs[1].set_ylabel("c2")
    axs[0].scatter(coeffs[:,0], coeffs[:,1])
    axs[1].scatter(coeffs[:,0], coeffs[:,2])
    fig.tight_layout()
    plt.savefig("EigenCoeffs.png")

def Residuals(original, fit):
    resi = original-fit
    squared  = np.power(resi,2)
    return np.sum(squared)

if __name__ == "__main__":
    logwave, flux = read_data()
# A
    plot_random(logwave, flux)
# B
    normed_flux, norm_constants = Normalization(flux, logwave)
# C
    residuals, mean = RemoveMean(normed_flux)
# D
    values, vectors, time_taken = DirectEigen(residuals)
#    plot_eigenvectors(logwave, vectors)
    print(vectors.shape)
    print("Time Taken: {t}. Condition Number: {cond}".format(t=time_taken, cond = np.max(np.abs(values))/np.min(np.abs(values))))
# E/F
    eigen_values, eigenvectors, time_taken_SVD = SVD_Eigen(residuals)
    print(eigenvectors.shape)
#    plot_eigenvectors_SVD(logwave, eigenvectors)
    print("Time Taken: {t}. Condition Number: {cond}".format(t=time_taken_SVD, cond = np.max(np.abs(eigen_values))/np.min(np.abs(eigen_values))))
# G
    approx, coeffs = reconstruct(5,eigenvectors, residuals, mean, norm_constants)
    plt.clf()
    fig, axs = plt.subplots(2)
    axs[0].plot(logwave, flux[0,:])
    axs[1].plot(logwave, approx[0,:])
    axs[0].set_title("Original")
    axs[1].set_title("Approx")
    fig.tight_layout()
    plt.savefig("Sanity.png")
# H
    plot_coeffs(coeffs)
# I
    RMS = []
    for i in range(1,21):
        approx, _ = reconstruct(i, eigenvectors, residuals, mean, norm_constants)
        RMS.append(np.sqrt(Residuals(flux, approx)))
    plt.clf()
    plt.plot([i for i in range(1,21)], RMS)
    plt.xlabel("N")
    plt.ylabel("Residuals")
    plt.savefig("Residuals.png")
