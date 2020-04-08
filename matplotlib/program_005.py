#For plotting a pie chart

import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt

#For reading & seperating data using pandas
data = pd.read_csv('DataSheet_001.csv')
ids = data['Responder_id']
language_responses = data['LanguagesWorkedWith']

language_counter = Counter()

for item in language_responses:
    language_counter.update(item.split(';'))

#for creating list of languages and responses for 15 most commonly used
languages, languageCount = map(list, zip(*language_counter.most_common(5)))

#for exploding a slice from the pie chart
explode=[0,0,0,0.1,0]

plt.pie(languageCount,labels=languages,explode=explode,
    shadow=True,startangle=90,autopct='%1.1f%%',
    wedgeprops={'edgecolor':'black'})

plt.title('Most popular programming languages')
plt.style.use('seaborn-notebook')
plt.tight_layout()
plt.show()

