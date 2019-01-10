import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

# verwijder users die groot deel van de data niet hebben ingevuld
data = pd.read_csv("relevantQs.csv", delimiter=',')
data = data.replace(" ", np.nan)

# lijst van indexen voor rijen waarbij meer dan 70 vragen niet zijn ingevuld
nan = [index for index, row in data.iterrows() if row.isnull().sum() > 70]

data = data.drop(data.index[nan])

# NaN naar 0 en string naar 1 bij alle _alt vragen
alt_columns = [column for column in data.columns.values if column[-3:] == 'alt']

data[alt_columns] = data[alt_columns].replace(np.nan, 0)

for key, value in data[alt_columns].iteritems():
    for item in value:
        if item != 0:
            data[alt_columns] = data[alt_columns].replace(item, 1)  