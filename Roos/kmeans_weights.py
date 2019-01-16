import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn import metrics
from scipy.spatial.distance import cdist
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("../Data/final_data.csv", delimiter=',')
full_data = data
cols = data.columns[:57]
data = data[cols]
drop = [i for i in range(35,47)]
data = data.drop(data.columns[drop], axis=1)

weights = []
for name in full_data.columns.values:
    if any(name in s for s in data.columns.values):
    #if name is in data.columns.values:
        weights.append(2)
    else:
        weights.append(-2)
print(weights)

X = full_data.values

km = KMeans(n_clusters=3).fit(X, sample_weight=weights)
