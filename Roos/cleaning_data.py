import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

# verwijder users die groot deel van de data niet hebben ingevuld
data = pd.read_csv("relevantQs.csv", delimiter=',')
data = data.replace(" ", np.nan)

# lijst van indexen voor rijen waarbij meer dan 70 vragen niet zijn ingevuld
nan = [index for index, row in data.iterrows() if row.isnull().sum() > 70]

data = data.drop(data.index[nan])

####################

# drop _alt columns
alt_columns = [column for column in data.columns.values if column[-3:] == 'alt']
data = data.drop(alt_columns, axis=1)