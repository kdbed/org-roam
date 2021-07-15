#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt


def slab_transmission(Sig_t,thickness,N):
    """ Compute the fraction of neutrons that leak through a slab
    Inputs:
    Sig_t:      The total macroscopic x-section
    thickness:  Width of the slab
    N:          Number of neutrons to simulate

    Returns:
    transmission: The fraction of neutrons that made it through
    """
    thetas = np.random.random(N)
    x = -np.log(1 - thetas)/Sig_t
    transmission = np.sum(x>thickness)/N

    #for a small number of neutrons we'll output a little more
    if (N <= 1000):
        plt.scatter(x,np.arange(N))
        plt.xlabel("Distance to collision")
        plt.ylabel("Neutron Number")
        plt.show()
    return transmission


#test the function with a small number of neutrons
Sigma_t = 2.0
thickness = 3.0
N = 1000000
transmission = slab_transmission(Sigma_t, thickness, N)
print("out of ", N, "neutrons only", int(transmission*N),
        "made it through.\n The fraction that made it through was",
        transmission)
