#For plotting subplots

import pandas as pd
from matplotlib import pyplot as plt

#extracting the data
data = pd.read_csv('DataSheet_002.csv')

#classifying the data
ages = data['Age']
dev_sal = data['All_Devs']
py_sal = data['Python']
js_sal = data['JavaScript']

#For styling the plot
plt.style.use("seaborn")

#For two different plots in same script
#fig1,ax1 = plt.subplots()
#fig2,ax2 = plt.subplots()

#For two different plots in same figure
fig,(ax1,ax2) = plt.subplots(nrows=2, ncols=1,sharex=True)

ax1.plot(ages,dev_sal,label="All Dev's",linestyle='--',color='#444444')
ax1.set_title('Median salary per month based on age')
ax1.set_ylabel('Median Salary in USD')
ax1.legend()

ax2.plot(ages,py_sal,label='Python')
ax2.plot(ages,js_sal,label='JavaScript')
ax2.set_xlabel('Age')
ax2.set_ylabel('Median Salary in USD')
ax2.legend()

#To reduce padding issue
plt.tight_layout()

#show() is for displaying the plot
plt.show()
