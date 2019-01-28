import pandas as pd
import numpy as np
import sys
import matplotlib.pyplot as plt

def plot(data, k, clust):
    d = {}
    indices = []
    y = []
    for i in range(k):
        d['label' + str(i)] = data.loc[data.label == i].astype(float)
        d['sums' + str(i)]  = d['label'+str(i)].sum()
        for j in range(len(d['sums'+str(i)])):
            if d['sums'+str(i)][j]/len(d['label' + str(i)]) > .6 and j not in indices:
                indices.append(j)

    indices.sort()
    indices = indices[:-1]
    for i in range(k):
        sums = d['sums'+str(i)]
        df = d['label'+str(i)]
        y.append(sums[df.columns[indices]])

    y = np.array(y)
    for i in range(len(y)):
        y[i] = y[i]/len(d['label'+str(i)]) *100

    y = y.T
    data = rename_cols(data, clust)
    x = data.columns[indices]
    titl = clust + ' clustering'
    df = pd.DataFrame(y,
                 index=x)
    plot = df.plot(kind='bar',figsize=(10,3),
        title='Percentage per cluster that belongs to specific category (' + titl + ')',
        sort_columns=True, rot=20)
    plt.xlabel('Categories')
    plt.ylabel('Percentage')
    plt.show()

def rename_cols(df, clust):
    df = df.rename(columns={'Q13A':'No fixed day',
                      'Q13F':'fixed week+weekend day',
                      'Q16A':'Runs in a group',
                      'Q16F': 'Trains individual',
                      'Q8_Geen aparte trainingsperiode (ik train gedurende het hele jaar)':'Trains whole year',
                      'Q10_Langer dan een jaar':'Trains for over a year',
                      'Q14_Ik begin meestal met hardlopen vanuit mijn huis.':'Starts running from home',
                      'Q15_Niet, ik loop thuis de deur uit':'Dont travel for training'})
    if clust == 'kmodes':
        df = df.rename(columns={'Q9_2 keer per week':'Trains twice a week',
                            'Q9_3 keer per week':'Trains three times a week',
                            'Q11_Ik wil niet vaker en/of meer kilomerters hardlopen dan ik nu doe':'Doenot wanna train more'})
    elif clust == 'spectral':
        df = df.rename(columns={'Q8_Niet of nauwelijks getraind':'Did not train beforehand'})
    return df


if __name__ == "__main__":
    clust = sys.argv[1]
    k = sys.argv[2]
    filename = '../Data/' + 'data_' + clust + k + '.csv'
    data = pd.read_csv(filename)
    plot(data, int(k), clust)
