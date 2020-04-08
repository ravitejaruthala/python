#For plotting data from csv file using csv package

import csv
from matplotlib import pyplot as plt
from collections import Counter

with open('DataSheet_001.csv','r') as csvFile:
#For reading a csv file
#    csv_reader = csv.reader(csvFile)
#For reading a csv file in form of a Dictionary
#csv_reader = csv.reader(csvFile)
#For going to next line
    #next(csv_reader)

    csv_reader = csv.DictReader(csvFile)

    #using a counter for counting
    languageCounter = Counter()

    for row in csv_reader:
        languageCounter.update(row['LanguagesWorkedWith'].split(';'))

languages = []
languageCount = []

#for creating list of languages and responses for 15 most commonly used
for item in languageCounter.most_common(15):
    languages.append(item[0])
    languageCount.append(item[1])

#For sorting
languages.reverse()
languageCount.reverse()

#For horizontal view use barh(y-axis,x-axis)
plt.barh(languages,languageCount)
plt.title('Most popular programming languages')
plt.xlabel('No of people opting')
plt.tight_layout()
plt.show()
