import numpy                 #loading our favorite library
from matplotlib import pyplot    #and the useful plotting library

nx = 41
dx = 2 / (nx - 1)
nt = 20    #the number of timesteps we want to calculate
nu = 0.3   #the value of viscosity
sigma = .2 #sigma is our CFL constant (Courant number)
dt = sigma * dx**2 / nu #dt is defined using sigma ... more later!

u = numpy.ones(nx)
u[int(.5/dx):int(1/dx+1)] = 2 # creating our hat functon again

utemp = numpy.ones(nx) # our temp array for iteration

for n in range(nt):
    utemp = u.copy() # copy the existing values of u into utemp
    for i in range(1,nx-1):
        u[i] = utemp[i] + nu * dt/dx**2 * (utemp[i+1] - 2*utemp[i] + utemp[i-1])

pyplot.plot(numpy.linspace(0,2,nx),u)
pyplot.show()