import pandas as pd
import numpy as np
import sys

from sklearn import cluster as sc
from kmodes.kmodes import KModes

def load_csv(file, delim):
    return pd.read_csv(file, delimiter=delim)

def drop_columns(data, indices):
    data = data.drop(data[data.columns[indices]], axis=1)
    return data

def cluster(data, clust, n):
    X = data.values
    if clust == 'kmeans':
        clustering = sc.KMeans(n_clusters=n).fit(X)
        labels = clustering.labels_
    if clust == 'spectral':
        clustering = sc.SpectralClustering(n_clusters=n, assign_labels="discretize", random_state=0).fit(X)
        labels = clustering.labels_
    if clust == 'kmodes':
        labels = KModes(n_clusters=n, init='Huang', n_init=20, verbose=0).fit_predict(X)

    data['label'] = labels
    print(np.bincount(labels))
    return data

def write_to_csv(data, clust, k):
    filename = '../Data/' + 'data_' + clust + str(k) + '.csv'
    data.to_csv(filename, index=False)

if __name__ == '__main__':
    clust_alg = sys.argv[1]
    k = int(sys.argv[2])
    data = load_csv('../Data/final_data.csv', ',')
    indices = [i for i in range(57,167)] + [i for i in range(35,47)]
    indices.sort()
    data = drop_columns(data, indices)
    data = cluster(data, clust_alg, k)
    write_to_csv(data, clust_alg, k)
