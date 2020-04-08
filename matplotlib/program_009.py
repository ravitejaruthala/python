#For plotting a scatter plot

import pandas as pd
from matplotlib import pyplot as plt

#For styling the plot
plt.style.use("seaborn")

#For reading and classifying the data
data = pd.read_csv('DataSheet_004.csv')
view_count = data['view_count']
likes = data['likes']
ratio = data['ratio']

#To plot a scatter plot
plt.scatter(view_count,likes,c=ratio,cmap='summer',
            edgecolor='black',linewidth=1,alpha=0.75)

#For color scale
cbar = plt.colorbar()
cbar.set_label('Like/Dislike Ratio')

#For using log scale
plt.xscale('log')
plt.yscale('log')

#title() for plot title
plt.title('Trending youtube videos')

#for labelling the x,y axis
plt.xlabel('Total views')
plt.ylabel('Total likes')

#To reduce padding issue
plt.tight_layout()

#show() is for displaying the plot
plt.show()
