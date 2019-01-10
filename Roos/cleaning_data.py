import pandas as pd
import numpy as np

# verwijder users die groot deel van de data niet hebben ingevuld
data = pd.read_csv("relevantQs.csv", delimiter=',')
data = data.replace(" ", np.nan)

# lijst van indexen voor rijen waarbij meer dan 70 vragen niet zijn ingevuld
nan = [index for index, row in data.iterrows() if row.isnull().sum() > 70]

data = data.drop(data.index[nan])
#data.to_csv('cleaned_data.csv')