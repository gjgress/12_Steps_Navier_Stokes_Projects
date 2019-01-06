import numpy
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot, cm

# parameters
nx = 101
ny = 101
nt = 80
c = 1 #? What? Why is c here?
dx = 2 / (nx-1)
dy = 2/(ny-1)
sigma = .2
dt = sigma*dx

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

for n in range(nt+1): 
    un = u.copy()
    vn = v.copy()
    u[1:,1:] = (un[1:,1:] - dt*c*(un[1:,1:]/dx*(un[1:,1:] - un[:-1,1:]) + vn[1:,1:]/dy*(un[1:,1:]-un[1:,:-1])))
    v[1:,1:] = (vn[1:,1:] - dt*c*(un[1:,1:]/dx*(vn[1:,1:] - vn[:-1,1:]) + vn[1:,1:]/dy*(vn[1:,1:]-vn[1:,:-1])))

    # BC

    u[0,:] = 1
    u[-1,:] = 1
    u[:,0] = 1
    u[:,-1] = 1

    v[0,:] = 1
    v[-1,:] = 1
    v[:,0] = 1
    v[:,-1] = 1

fig = pyplot.figure(figsize=(11,7), dpi = 100)
ax = fig.gca(projection='3d')
X,Y = numpy.meshgrid(x,y)

ax.plot_surface(Y,X,u,cmap=cm.viridis, rstride=2, cstride=2)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')

fig = pyplot.figure(figsize=(11,7), dpi = 100)
ax = fig.gca(projection='3d')
X,Y = numpy.meshgrid(x,y)

ax.plot_surface(Y,X,v,cmap=cm.viridis, rstride=2, cstride=2)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')

pyplot.show()
