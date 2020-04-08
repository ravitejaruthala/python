#For plotting a Histogram

from matplotlib import pyplot as plt
import pandas as pd

plt.style.use('fivethirtyeight')

#extracting the data
data = pd.read_csv('DataSheet_003.csv')

#classifying the data
ages = data['Age']
median_age = 29

#For grouping the x-axis
#bins = 5
bins = [10,20,30,40,50,60,70,80,90,100]

#For plotting histogram
plt.hist(ages,bins=bins,edgecolor='black',log=True,label='Responses')

#For drawing a verticle line
plt.axvline(median_age,color='#fc4f30',label='Median Age',linewidth=2)

#title() for plot title
plt.title('Histogram plot for responses')

#for labelling the x,y axis
plt.xlabel('Age')
plt.ylabel('Responses')


#legend() for describing the lines of the plot
plt.legend()

#To reduce padding issue
plt.tight_layout()

#show() is for displaying the plot
plt.show()

