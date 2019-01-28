import pandas as pd
import numpy as np
import clusterings

def whiten(X):
    X = X.astype(np.float)
    X = X.reshape((-1, np.prod(X.shape[1:])))
    X_centered = X - np.mean(X, axis=0)
    Sigma = np.dot(X_centered.T, X_centered) / X_centered.shape[0]
    U, Lambda, _ = np.linalg.svd(Sigma)
    W = np.dot(U, np.dot(np.diag(1.0 / np.sqrt(Lambda + 1e-5)), U.T))
    return np.dot(X_centered, W.T)

if __name__ == '__main__':
    data = pd.read_csv('../Data/final_data.csv')
    drop = [x for x in data.columns if x[-5:] == 'False']
    data = data.drop(data[drop], axis=1)
    data = data.drop(data[data.columns[-1:]], axis=1)

    Y = whiten(data.values)
    df = pd.DataFrame(data=Y, columns=data.columns)
    data = clusterings.cluster(data, 'kmodes', 4)
    clusterings.write_to_csv(data, 'whitened', 4)
