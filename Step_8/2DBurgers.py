import numpy
from matplotlib import pyplot, cm
from mpl_toolkits.mplot3d import Axes3D


# parameters
nx = 41
ny = 41
nu = .01
nt = 120
c = 1 
dx = 2 / (nx-1)
dy = 2/(ny-1)
sigma = .25
dt = sigma*dx*dy/nu

x = numpy.linspace(0,2,nx)
y = numpy.linspace(0,2,ny)

u = numpy.ones((nx,ny))
v = numpy.ones((nx,ny)) #still trying to figure out the purpose of v
un = numpy.ones((nx,ny))
vn = numpy.ones((nx,ny))

# initial conditions
# hat function, 2 for .5<=x,y<=1, 1 elsewhere
u[int(.5/dx):int(1/dx+1),int(.5/dy):int(1/dy+1)] = 2
v[int(.5/dx):int(1/dx+1),int(.5/dy):int(1/dy+1)] = 2

fig = pyplot.figure(figsize=(11,7), dpi = 100)
ax = fig.gca(projection='3d')
X,Y = numpy.meshgrid(x,y)

ax.plot_surface(Y,X,u,cmap=cm.viridis, rstride=2, cstride=2)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
