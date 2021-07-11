from scipy import integrate
from scipy.interpolate import interp1d
from numpy import *
from scipy.optimize import basinhopping
import pso

x0 = linspace(0,1,5)



def fmin(z):
    f1 = interp1d(x0,z)
    sum1 = 0.0
    for i in range(5):
        f2 = lambda x: f1(x)*0.5
        y, err = integrate.quad(f2, 0, 1)
        sum1 += abs(z[i] - y - 1)
    return sum1



z0 = array([0,0.5,2,0.0,0.3])



def print_fun(x, f, accepted):
    print("at minimum %.4f accepted %d" % (f, int(accepted)))

minimizer_kwargs = {"method": "BFGS"}
ret = basinhopping(fmin, z0, minimizer_kwargs=minimizer_kwargs,niter=3,callback=print_fun)
print(ret)

'''
bounds = list()
for i in range(len(z0)):
    bounds.append((-100,100))

pso.PSO(fmin,z0,bounds,num_particles=15,maxiter=50)
'''
