from bokeh.core.properties import value
from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.transform import dodge
from bokeh.layouts import gridplot
from bokeh.layouts import column
import csv
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# with open('relevantQs.csv') as f:
#     data = csv.reader(f, delimiter=',')

all_data = pd.read_csv("relevantQs.csv", delimiter=',')

# print(all_data.head(5))
numberofman = 0
numberofwoman = 0
other = 0

for j in all_data['Q47']:
    if j == 'Man':
        numberofman += 1
    if j == 'Vrouw':
        numberofwoman += 1
    else:
        other += 1
total = int(numberofman + numberofwoman)
per_man = (numberofman*100)/total
per_woman = (numberofwoman*100)/total

# Pie chart, male female
# labels = 'Male', 'Female'
# sizes = [per_man, per_woman]
# explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

# fig1, ax1 = plt.subplots()
# ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
#         shadow=True, startangle=90)
# ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
# plt.show()

d_education = dict()
for key in all_data['Q51']:
    if key in d_education:
        d_education[key] += 1
    else:
        d_education[key] = 1

total_education = 0
for key in d_education:
    total_education += d_education[key]
listeducation = []
for key in d_education:
    listeducation.append((d_education[key]*100)/total_education)

# Pie chart, education
# labels = d_education
# sizes = listeducation
# explode = (0, 0.05, 0.1, 0.15, 0.2, 0.3, 0.4)  # only "explode" the 2nd slice (i.e. 'Hogs')

# fig1, ax1 = plt.subplots()
# ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
#         shadow=True, startangle=90)
# ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
# plt.show()

d_useapp = dict()
for key in all_data['Q43']:
    if key in d_useapp:
        d_useapp[key] += 1
    else:
        d_useapp[key] = 1

total_useapp = 0
for key in d_useapp:
    total_useapp += d_useapp[key]
listapp = []
for key in d_useapp:
    listapp.append((d_useapp[key]*100)/total_useapp)

# Pie chart, education
labels = d_useapp
sizes = listapp
explode = (0, 0.05, 0.1, 0.15, 0.2)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
