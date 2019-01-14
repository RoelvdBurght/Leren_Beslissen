import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn import metrics
from scipy.spatial.distance import cdist
import numpy as np
import matplotlib.pyplot as plt

# find optimal value of k for k-means
data = pd.read_csv("../Data/final_data.csv", delimiter=',')
#data = data.drop(['Q47_Man', 'Q47_Vrouw', 'Q48', 'Q49', 'Q50'], axis=1)

X = data.values

Sum_of_squared_distances = []
K = range(1,15)
for k in K:
    km = KMeans(n_clusters=k)
    km = km.fit(X)
    #Sum of squared distances of samples to their closest cluster center.
    Sum_of_squared_distances.append(km.inertia_) 

plt.plot(K, Sum_of_squared_distances, 'bx-')
plt.xlabel('k')
plt.ylabel('Sum of squared distances')
plt.title('The Elbow Method showing the optimal k')
plt.show()