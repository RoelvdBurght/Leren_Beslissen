import clusterings
import plotly.plotly as py
import plotly.graph_objs as go
from sklearn.manifold import TSNE
import plotly
plotly.tools.set_credentials_file(username='hbpvanLaatum', api_key='gIm1W4VzUfg1V8LYtQHe')


def tsne(data):
    X = data.values
    tsne = TSNE(n_components=3, verbose=1)
    return tsne.fit_transform(X)

def create_df(data, tsne_result):
    df_tsne = data.copy()
    df_tsne['x-tsne'] = tsne_result[:,0]
    df_tsne['y-tsne'] = tsne_result[:,1]
    df_tsne['z-tsne'] = tsne_result[:,2]
    return df_tsne

def 

if __name__ == '__main__':
    data = clusterings.load_csv('../Data/final_data.csv', ',')
    indices = [i for i in range(57,167)] + [i for i in range(35,47)]
    data = clusterings.drop_columns(data, indices)
    data = clusterings.cluster(data, 'kmodes', 5)
    tsne_result = tsne(data)
    df_tsne = create_df(data, tsne_result)

    label0 = df_tsne.loc[df_tsne['label'] == 0]
    label1 = df_tsne.loc[df_tsne['label'] == 1]
    label2 = df_tsne.loc[df_tsne['label'] == 2]
    label3 = df_tsne.loc[df_tsne['label'] == 3]
    trace1 = go.Scatter3d(
        x=label0['x-tsne'],
        y=label0['y-tsne'],
        z=label0['z-tsne'],
        mode='markers',
        marker=dict(
            size=12,
            line=dict(
                color='rgba(217, 217, 217, 0.14)',
                width=0.5
            ),
            opacity=1
        )
    )
    trace2 = go.Scatter3d(
        x=label1['x-tsne'],
        y=label1['y-tsne'],
        z=label1['z-tsne'],
        mode='markers',
        marker=dict(
            size=12,
            line=dict(
                color='rgba(217, 217, 217, 0.14)',
                width=0.5
            ),
            opacity=1
        )
    )
    trace3 = go.Scatter3d(
        x=label2['x-tsne'],
        y=label2['y-tsne'],
        z=label2['z-tsne'],
        mode='markers',
        marker=dict(
            size=12,
            line=dict(
                color='rgba(217, 217, 217, 0.14)',
                width=0.5
            ),
            opacity=1
        )
    )
    trace4 = go.Scatter3d(
        x=label3['x-tsne'],
        y=label3['y-tsne'],
        z=label3['z-tsne'],
        mode='markers',
        marker=dict(
            size=12,
            line=dict(
                color='rgba(217, 217, 217, 0.14)',
                width=0.5
            ),
            opacity=1
        )
    )
    data = [trace1, trace2, trace3, trace4]
    layout = go.Layout(
        margin=dict(
            l=0,
            r=0,
            b=0,
            t=0
        )
    )
    fig = go.Figure(data=data, layout=layout)
    py.plot(fig, filename='simple-3d-scatter')
