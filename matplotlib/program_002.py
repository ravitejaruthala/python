# Creating and customizing bar charts using MATPLOTLIB

import numpy as np
from matplotlib import pyplot as plt

#For changing the style of the plot
plt.style.use('fivethirtyeight')

dev_x = [25,26,27,28,29,30,31,32,33,34,35]
dev_y = [38496,42000,46000,52000,58000,61000,63000,67000,71000,76000,80000]
py_dev_y = [40000,44000,50000,55000,61000,65000,69000,71000,76000,79000,83000]
js_dev_y = [39000,40000,44000,48000,53000,57000,60000,74000,79000,81000,82000]

x_indexes = np.arange(len(dev_x))
width = 0.25

#bar() is for plotting the co-ordinates in form of bar chart
plt.bar(x_indexes-width,dev_y,color='#444444',label="All Dev's",width=width)
plt.bar(x_indexes,py_dev_y,color='b',label="Python Dev's",width=width)
plt.bar(x_indexes+width,js_dev_y,color='y',label="JavaScript",width=width)

#title() for plot title
plt.title('Median salary per month based on age')

#for labelling the x,y axis
plt.xlabel('Age')
plt.ylabel('Median Salary')

#legend() for describing the lines of the plot
plt.legend()

#To reset x-axis to labels instead of indexes
plt.xticks(ticks=x_indexes,labels=dev_x)

#To reduce padding issue
plt.tight_layout()

#To enable grid view
plt.grid(True)

#show() is for displaying the plot
plt.show()

