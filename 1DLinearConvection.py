import numpy
from matplotlib import pyplot
import time, sys

#Number of 
numx = 41
dx = 2/(numx-1)

numt = 25
dt = .025
c = 1

u = numpy.ones(numx)
u[int(.5/dx):int(1/dx+1)] = 2

# pyplot.plot(numpy.linspace(0,2,numx), u)
# pyplot.show()

utemp = numpy.ones(numx)

# Why do we backpropogate for x? Figure this out
for n in range(numt):
    utemp = u.copy()
    for i in range(1,numx):
        u[i] = utemp[i] - c * dt / dx * (utemp[i] - utemp[i-1])
pyplot.plot(numpy.linspace(0,2,numx),u)
pyplot.show()
