"""GitHub Classroom autograding script."""

import pickle

import pandas as pd
from sklearn.metrics import accuracy_score


def load_data():

    import pandas as pd

    dataframe = pd.read_csv(
        "sentences.csv.zip",
        index_col=False,
        compression="zip",
    )

    data = dataframe.phrase
    target = dataframe.target

    return data, target


def load_estimator():

    import os
    import pickle

    if not os.path.exists("estimator.pickle"):
        return None
    with open("estimator.pickle", "rb") as file:
        estimator = pickle.load(file)

    return estimator


def test():

    data, target = load_data()
    estimator = load_estimator()

    accuracy = accuracy_score(
        y_true=target,
        y_pred=estimator.predict(data),
    )

    assert accuracy > 0.9545


test()
