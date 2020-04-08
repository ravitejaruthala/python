#For plotting real-time data

from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import random
from itertools import count

x = []
y = []
z=[]
index = count()

#For styling the plot
plt.style.use("fivethirtyeight")

#title() for plot title
plt.title('Continous Data plotting')

#for labelling the x,y axis
plt.xlabel('Consecutive values')
plt.ylabel('Changing values')

def animate(i):

    x.append(next(index))
    y.append(random.randint(0,5))
    z.append(random.randint(3,9))

    #For clearing previous plots on the fig and to maintain same color
    plt.cla()
    plt.plot(x,y,label='Change 1')
    plt.plot(x,z,label='Change 2')
    plt.legend(loc='upper left')

#For plotting continously in 1 sec time interval
ani = FuncAnimation(plt.gcf(),animate,interval=1000)

#To reduce padding issue
plt.tight_layout()

#show() is for displaying the plot
plt.show()
