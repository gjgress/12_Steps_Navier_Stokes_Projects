import numpy
from matplotlib import pyplot, cm
from mpl_toolkits.mplot3d import Axes3D


# parameters
nx = 31
ny = 31
nu = .05
nt = 80
c = 1 
dx = 2 / (nx-1)
dy = 2/(ny-1)
sigma = .25
dt = sigma*dx*dy/nu

x = numpy.linspace(0,2,nx)
y = numpy.linspace(0,2,ny)

u = numpy.ones((nx,ny))
un = numpy.ones((nx,ny))

# initial conditions
# hat function, 2 for .5<=x,y<=1, 1 elsewhere
u[int(.5/dx):int(1/dx+1),int(.5/dy):int(1/dy+1)] = 2

fig = pyplot.figure(figsize=(11,7), dpi = 100)
ax = fig.gca(projection='3d')
X,Y = numpy.meshgrid(x,y)

surf = ax.plot_surface(Y,X,u,cmap=cm.viridis, rstride=1, cstride=1, linewidth=0, antialiased=False)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')

def diffuse(nt):

    u[int(.5/dx):int(1/dx+1),int(.5/dy):int(1/dy+1)] = 2

    for n in range(nt+1): 
        un = u.copy()
        u[1:-1,1:-1] = (un[1:-1,1:-1] + nu*dt/dx/dx*(un[2:,1:-1] - 2*un[1:-1,1:-1] + un[:-2,1:-1]) + nu*dt/dy/dy*(un[1:-1,2:] - 2*un[1:-1,1:-1] + un[1:-1,:-2]))


        # BC

        u[0,:] = 1
        u[-1,:] = 1
        u[:,0] = 1
        u[:,-1] = 1

    fig = pyplot.figure()
    ax = fig.gca(projection='3d')

    ax.plot_surface(Y,X,u[:],cmap=cm.viridis, rstride=1, cstride=1, linewidth=0, antialiased=True)
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_zlim(1,2.5)
diffuse(10)
diffuse(14)
diffuse(50)
pyplot.show()