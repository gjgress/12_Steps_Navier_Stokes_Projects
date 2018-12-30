import numpy
from matplotlib import pyplot

# Parameters

numx = 41 # number of dx steps
dx = 2 / (numx-1) # discretized distance
numt = 20 # number of timesteps
dt = .025 # discretized unit of time

u = numpy.ones(numx) #initializing our wave
u[int(.5/dx):int(1/dx + 1)] = 2 # our wave is now a hat; it has twice the amplitude between .5 and 1

utemp = numpy.ones(numx) # initializing placeholder solution


for n in range(numt):  #iterate through time
    utemp = u.copy() ##copy the existing values of u into un
    for i in range(1, numx):  ##now we'll iterate through the u array
    
     ###This is the line from Step 1, copied exactly.  Edit it for our new equation.
     ###then uncomment it and run the cell to evaluate Step 2   
      
           u[i] = utemp[i] - utemp[i] * dt / dx * (utemp[i] - utemp[i-1]) 

        
pyplot.plot(numpy.linspace(0, 2, numx), u) ##Plot the results
pyplot.show()
