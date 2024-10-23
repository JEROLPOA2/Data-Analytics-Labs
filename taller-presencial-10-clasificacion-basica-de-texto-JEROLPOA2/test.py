"""GitHub Classroom autograding script."""

import pickle
import pandas as pd

from sklearn.metrics import accuracy_score

dataframe = pd.read_csv(
    "sentences.csv.zip",
    index_col=False,
    compression="zip",
)

with open("clf.pickle", "rb") as file:
    clf = pickle.load(file)

with open("vectorizer.pickle", "rb") as file:
    vectorizer = pickle.load(file)

accuracy = accuracy_score(
    y_true=dataframe.target,
    y_pred=clf.predict(vectorizer.transform(dataframe.phrase)),
)

assert accuracy > 0.854
