import pandas as pd
import numpy as np
from sklearn import cluster as sc
import matplotlib.pyplot as plt

def load_csv(file, delim):
    return pd.read_csv(file, delimiter=delim)

def drop_columns(indices):
    data.drop(data[data.columns[indices]])
    return data

def cluster(data, clust, n):
    X = data.values
    if clust == 'kmeans':
        clustering = sc.KMeans(n_clusters=n).fit(X)
    if clust == 'hierarch':

    data['labels'] = clustering.labels_
    print(np.bincount(clustering.labels_))
    return clustering, data
    # clustering = sc.cluster.

def plot(data):
    d = {}
    for i in range(3):
        d['label' + i] = data.loc[data.label == 0].astype(float)
        d['sums' + i] = d['label', ]



if __name__ == '__main__':
    data = load_csv('../Data/final_data.csv', ',')
    indices = []
    data = drop_columns(indices)
    cluistering, data = cluster(data, 'kmeans', 3)
    plot(data)
    # print(data.labels)
