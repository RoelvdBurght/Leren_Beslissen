import pandas as pd
import numpy as np
import sys
from sklearn import cluster as sc
from kmodes.kmodes import KModes
import matplotlib.pyplot as plt

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
    if clust == 'spect':
        clustering = sc.SpectralClustering(n_clusters=n, assign_labels="discretize", random_state=0).fit(X)
        labels = clustering.labels_
    if clust == 'kmodes':
        labels = KModes(n_clusters=n, init='Huang', n_init=10, verbose=1).fit_predict(X)

    data['label'] = labels
    #print(np.bincount(labels))
    return data

def plot(data, n):
    d = {}
    indices = []
    y = []
    for i in range(n):
        d['label' + str(i)] = data.loc[data.label == i].astype(float)
        d['sums' + str(i)]  = d['label'+str(i)].sum()
        for j in range(len(d['sums'+str(i)])):
            if d['sums'+str(i)][j]/len(d['label' + str(i)]) > .1 and j not in indices:
                indices.append(j)

    indices.sort()
    indices = indices[:-1]
    for i in range(n):
        sums = d['sums'+str(i)]
        df = d['label'+str(i)]
        y.append(sums[df.columns[indices]])
        #print(len(df))

    y = np.array(y)
    for i in range(len(y)):
        y[i] = y[i]/len(d['label'+str(i)])

    y = y.T
    #print(y)

    # y[0] = y[0] / len()
    x = data.columns[indices]
    df = pd.DataFrame(y,
                 index=x)
    plot = df.plot(kind='bar',figsize=(10,3))
    plt.show()

if __name__ == '__main__':
    clust_alg = sys.argv[1]
    n = int(sys.argv[2])
    data = load_csv('../Data/final_data.csv', ',')
    indices = [i for i in range(57,167)] + [i for i in range(35,47)]
    indices.sort()
    data = drop_columns(data, indices)
    data = cluster(data, clust_alg, n)
    plot(data, n)
