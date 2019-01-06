import numpy
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot, cm

# parameters

nx = 81
ny = 81 # 2D! Gotta iterate for both variables now
nt = 100
c = 1 # wavespeed
dx = 2 / (nx-1)
dy = 2 / (ny-1)
sigma = .2
dt = sigma*dx

x = numpy.arange(0,2+dx,dx)
y = numpy.arange(0,2+dy,dy)

# solutions vector
u = numpy.ones((nx,ny))
un = numpy.ones((nx, ny)) #for iteration?


# initial conditions
u[int(.5/dx):int(1/dx+1),int(.5/dy):int(1/dy+1)] = 2

# plot initial conditions-- practicing 3D plotting capabilities
fig = pyplot.figure(figsize=(11,7),dpi=100)
ax = fig.gca(projection='3d')
X,Y = numpy.meshgrid(x,y)
surf = ax.plot_surface(Y,X,u[:],cmap= cm.viridis) #for some reason, using mesh grid means switching the position of x and y in u. I just switched X and Y here. Not sure why meshgrid works that way? or 3D plot?

for n in range(nt+1): #loop across numbe of timesteps
    un = u.copy()
    u[1:,1:] = (un[1:,1:] - c*dt/dx*(un[1:,1:] - un[:-1,1:]) - c*dt/dy*(un[1:,1:] - un[1:,:-1]))
    
    # These were the BC included in the original lesson. In this case, they are not necessary. But if our wave were to start near a boundary, then BC become important-- I bet you could simulate forced oscillations with this idea, using a sinusoidal boundary condition

    # u[0,:] = 1  
    # u[-1,:] = 1
    # u[:,0] = 1
    # u[:,-1] = 1

fig = pyplot.figure(figsize=(11,7),dpi=100)
ax = fig.gca(projection='3d')
pyplot.xlabel('x')
pyplot.ylabel('y')
surf2 = ax.plot_surface(Y,X,u[:],cmap= cm.viridis)
pyplot.show()
