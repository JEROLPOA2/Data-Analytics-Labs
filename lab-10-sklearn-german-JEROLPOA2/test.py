"""GitHub Classroom autograding script."""

import os
import pickle

import pandas as pd
from sklearn.calibration import LabelEncoder
from sklearn.discriminant_analysis import StandardScaler
from sklearn.metrics import accuracy_score


def load_estimator():
    """Load trained model from disk."""

    if not os.path.exists("model.pkl"):
        return None
    with open("model.pkl", "rb") as file:
        estimator = pickle.load(file)

    return estimator


def load_datasets():
    """Load train and test datasets."""

    train_dataset = pd.read_csv("train_dataset.csv")
    test_dataset = pd.read_csv("test_dataset.csv")

    categorical_columns = [col for col in train_dataset.columns if
                       train_dataset[col].dtype == 'object']


    label_encoder = LabelEncoder()

    for col in categorical_columns:
        train_dataset[col] = label_encoder.fit_transform(train_dataset[col])
        test_dataset[col] = label_encoder.fit_transform(test_dataset[col])

    scaler = StandardScaler()
    

    x_train = train_dataset.drop("default", axis=1)
    y_train = train_dataset["default"]

    x_test = test_dataset.drop("default", axis=1)
    y_test = test_dataset["default"]

    x_train = scaler.fit_transform(x_train)
    x_test = scaler.transform(x_test)

    return x_train, x_test, y_train, y_test


def eval_metrics(y_true, y_pred):
    """Evaluate model performance."""

    accuracy = accuracy_score(y_true, y_pred)

    return accuracy


def compute_metrics():
    """Compute model metrics."""

    estimator = load_estimator()
    assert estimator is not None, "Model not found"

    x_train, x_test, y_true_train, y_true_test = load_datasets()

    y_pred_train = estimator.predict(x_train)
    y_pred_test = estimator.predict(x_test)

    accuracy_train = eval_metrics(y_true_train, y_pred_train)
    accuracy_test = eval_metrics(y_true_test, y_pred_test)

    return accuracy_train, accuracy_test


def run_grading():
    """Run grading script."""

    accuracy_train, accuracy_test = compute_metrics()

    assert accuracy_train > 0.73
    assert accuracy_test > 0.73


if __name__ == "__main__":
    run_grading()
