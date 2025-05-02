import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier

data = {'age': [23, 25, 27, 29, 29],
        'likes english': [0, 1, 1, 0, 0],
        'likes ai': [0, 1, 0, 1, 0],
        'raise salary': [0, 0, 1, 1, 0]}

# load data
df = pd.DataFrame(data)

# get value and convert to numpy
X = df[['age', 'likes english', 'likes ai']].values
y = df[['raise salary']].values.reshape(-1,)

# define classifier
clf = DecisionTreeClassifier()

# train
clf = clf.fit(X, y)
# predict

x_test = np.array([[27, 0, 1]])
predicted_label = clf.predict(x_test)
predicted_label

from sklearn.tree import plot_tree

# visualization
plot_tree(clf, feature_names=['age', 'likes english', 'likes ai'], fontsize=10)