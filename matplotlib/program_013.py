#For plotting a 3D-plot

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d

#For styling the plot
plt.style.use("fivethirtyeight")

fig = plt.figure()
#111 means 1x1 grid 1 subplot
ax = fig.add_subplot(111,projection='3d')

#arange(start,len)
x = np.arange(1,11)
y = [5,6,7,8,2,5,6,3,7,2]
#For list of all zeros
z = np.zeros(10)
#width
dx = np.ones(10)
#depth
dy = np.ones(10)
#height
dz = [1,2,3,4,5,6,7,8,9,10]

#For a 3D plot
ax.bar3d(x,y,z,dx,dy,dz)

plt.title('3D Plot')
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_zlabel('z-axis')

plt.show()
