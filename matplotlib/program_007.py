#For plotting a line chart and filling areas with logics

from matplotlib import pyplot as plt
import pandas as pd

#extracting the data
data = pd.read_csv('DataSheet_002.csv')

#classifying the data
ages = data['Age']
dev_sal = data['All_Devs']
py_sal = data['Python']
js_sal = data['JavaScript']
overall_median = 57287

plt.plot(ages,dev_sal,label="All Dev's")
plt.plot(ages,py_sal,label='Python')
#plt.plot(ages,js_sal,label='JavaScript')

#title() for plot title
plt.title('Median salary per month based on age')

#for labelling the x,y axis
plt.xlabel('Age')
plt.ylabel('Median Salary in USD')

#To fill the area between line graphs
plt.fill_between(ages,py_sal,overall_median,interpolate=True,
                 where=(py_sal>overall_median),alpha=0.25,label='Above Median')
plt.fill_between(ages,py_sal,overall_median,interpolate=True,
                 where=(py_sal<=overall_median),color='red',alpha=0.25,label='Below Median')

#legend() for describing the lines of the plot
plt.legend()

#To reduce padding issue
plt.tight_layout()

#To enable grid view
plt.grid(True)

#show() is for displaying the plot
plt.show()

