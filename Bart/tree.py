from sklearn import tree
import pandas as pd
import numpy as np
import graphviz
import sys
from sklearn.externals.six import StringIO
from IPython.display import Image
import pydotplus

def validation_split(data, ratio):
    slice_ind = int(len(data) * ratio)
    train = data[:slice_ind]
    val = data[slice_ind:,]
    return train, val

if __name__ == '__main__':
    clust = sys.argv[1]
    k = sys.argv[2]
    filename = '../Data/' + 'data_' + clust + k + '.csv'
    data = pd.read_csv(filename)
    train, val = validation_split(data.values, 0.7)
    X_train = train[:,:-1]
    Y_train = train[:,-1].astype(int)
    X_val = val[:,:-1]
    Y_val = val[:,-1]

    # estimator = tree.DecisionTreeClassifier(max_leaf_nodes=3, random_state=0)
    # estimator.fit(X_train, Y_train)
    #
    dot_data = StringIO()

    clf_gini = tree.DecisionTreeClassifier(criterion = "gini", random_state = 100,
                               max_depth=4, min_samples_leaf=4, min_impurity_decrease=0.01)
    clf_fit = clf_gini.fit(X_train, Y_train)
    print(sum(clf_gini.predict(X_val) == Y_val)/len(Y_val))
    tree.export_graphviz(clf_fit, out_file=dot_data,
                filled=True, rounded=True,
                special_characters=True)
    graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
    graph.write_png('tree3.png')


#     n_nodes = estimator.tree_.node_count
# children_left = estimator.tree_.children_left
# children_right = estimator.tree_.children_right
# feature = estimator.tree_.feature
# threshold = estimator.tree_.threshold
#
#
# # The tree structure can be traversed to compute various properties such
# # as the depth of each node and whether or not it is a leaf.
# node_depth = np.zeros(shape=n_nodes, dtype=np.int64)
# is_leaves = np.zeros(shape=n_nodes, dtype=bool)
# stack = [(0, -1)]  # seed is the root node id and its parent depth
# while len(stack) > 0:
#     node_id, parent_depth = stack.pop()
#     node_depth[node_id] = parent_depth + 1
#
#     # If we have a test node
#     if (children_left[node_id] != children_right[node_id]):
#         stack.append((children_left[node_id], parent_depth + 1))
#         stack.append((children_right[node_id], parent_depth + 1))
#     else:
#         is_leaves[node_id] = True
#
# print("The binary tree structure has %s nodes and has "
#       "the following tree structure:"
#       % n_nodes)
# for i in range(n_nodes):
#     if is_leaves[i]:
#         print("%snode=%s leaf node." % (node_depth[i] * "\t", i))
#     else:
#         print("%snode=%s test node: go to node %s if X[:, %s] <= %s else to "
#               "node %s."
#               % (node_depth[i] * "\t",
#                  i,
#                  children_left[i],
#                  feature[i],
#                  threshold[i],
#                  children_right[i],
#                  ))
# print()
#
# # First let's retrieve the decision path of each sample. The decision_path
# # method allows to retrieve the node indicator functions. A non zero element of
# # indicator matrix at the position (i, j) indicates that the sample i goes
# # through the node j.
#
# node_indicator = estimator.decision_path(X_val)
#
# # Similarly, we can also have the leaves ids reached by each sample.
#
# leave_id = estimator.apply(X_val)
#
# # Now, it's possible to get the tests that were used to predict a sample or
# # a group of samples. First, let's make it for the sample.
#
# sample_id = 0
# node_index = node_indicator.indices[node_indicator.indptr[sample_id]:
#                                     node_indicator.indptr[sample_id + 1]]
#
# print('Rules used to predict sample %s: ' % sample_id)
# for node_id in node_index:
#     if leave_id[sample_id] == node_id:
#         continue
#
#     if (X_val[sample_id, feature[node_id]] <= threshold[node_id]):
#         threshold_sign = "<="
#     else:
#         threshold_sign = ">"
#
#     print("decision id node %s : (X_val[%s, %s] (= %s) %s %s)"
#           % (node_id,
#              sample_id,
#              feature[node_id],
#              X_val[sample_id, feature[node_id]],
#              threshold_sign,
#              threshold[node_id]))
#
# # For a group of samples, we have the following common node.
# sample_ids = [0, 1]
# common_nodes = (node_indicator.toarray()[sample_ids].sum(axis=0) ==
#                 len(sample_ids))
#
# common_node_id = np.arange(n_nodes)[common_nodes]
#
# print("\nThe following samples %s share the node %s in the tree"
#       % (sample_ids, common_node_id))
# print("It is %s %% of all nodes." % (100 * len(common_node_id) / n_nodes,))
#
# #
# # X = [[0, 0], [1, 1]]
# # Y = [[0, 1]]
# #
# # clf = tree.DecisionTreeClassifier()
# # clf = clf.fit(X, Y)
# # clf.predict([[2., 2.]])
# # clf.predict_proba([[2., 2.]])
