#For plotting Time series data

import pandas as pd
from matplotlib import pyplot as plt

#For styling the plot
plt.style.use("seaborn")

#For reading and classifying the data
data = pd.read_csv('DataSheet_005.csv')
price_date = data['Date']
price_close = data['Close']

#To convert csv strings into dates and sortting by Date
data['Date'] = pd.to_datetime(data['Date'])
data.sort_values('Date',inplace=True)

#For plotting date plot
plt.plot_date(price_date,price_close,linestyle='solid')

#For auto-formatting dates on x-axis
plt.gcf().autofmt_xdate()

#title() for plot title
plt.title('BitCoin prices')

#for labelling the x,y axis
plt.xlabel('Dates')
plt.ylabel('Changing Prices')

#To reduce padding issue
plt.tight_layout()

#show() is for displaying the plot
plt.show()
