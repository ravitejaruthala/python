# Creating and customizing plots using MATPLOTLIB

from matplotlib import pyplot as plt

#For changing the style of the plot
#print(plt.style.available)
plt.style.use('fivethirtyeight')
plt.xkcd() #For cominc look

dev_x = [25,26,27,28,29,30,31,32,33,34,35]
dev_y = [38496,42000,46000,52000,58000,61000,63000,67000,71000,76000,80000]
py_dev_y = [40000,44000,50000,55000,61000,65000,69000,71000,76000,79000,83000]
js_dev_y = [39000,40000,44000,48000,53000,57000,60000,74000,79000,81000,82000]

#plot() is for plotting the co-ordinates
plt.plot(dev_x,dev_y,color='#444444',linestyle='-',marker='.',label="All Dev's")
plt.plot(dev_x,py_dev_y,color='b',linestyle='--',marker='o',linewidth=2,label="Python Dev's")
plt.plot(dev_x,js_dev_y,color='y',linestyle='-.',marker='x',linewidth=3,label="JavaScript")

#title() for plot title
plt.title('Median salary per month based on age')

#for labelling the x,y axis
plt.xlabel('Age')
plt.ylabel('Median Salary')

#legend() for describing the lines of the plot
plt.legend()

#To reduce padding issue
plt.tight_layout()

#To enable grid view
plt.grid(True)

#show() is for displaying the plot
plt.show()

#For saving the figure
#plt.savefig('fig.png')
