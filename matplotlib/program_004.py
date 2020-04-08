#For plotting data from csv file using pandas

import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt

#For styling the plot
plt.style.use("fivethirtyeight")

#For reading & seperating data using pandas
data = pd.read_csv('DataSheet_001.csv')
ids = data['Responder_id']
language_responses = data['LanguagesWorkedWith']

language_counter = Counter()

for item in language_responses:
    language_counter.update(item.split(';'))

languages = []
languageCount = []

#for creating list of languages and responses for 15 most commonly used
for item in language_counter.most_common(15):
    languages.append(item[0])
    languageCount.append(item[1])

#Sorting the data
languages.reverse()
languageCount.reverse()

#For horizontal view use barh(y-axis,x-axis)
plt.barh(languages,languageCount)
plt.title('Most popular programming languages')
plt.xlabel('No of people opting')
plt.tight_layout()
plt.show()
