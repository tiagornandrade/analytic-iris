from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.metrics import accuracy_score
import numpy as np
import csv
from dagster import op


@op
def etl_iris(context):
    iris = load_iris()
    return iris


@op
def array_data(context, iris):
    x = iris.data  # array of the data
    return x


@op
def array_labels(context, iris):
    y = iris.target  # array of labels (i.e answers) of each data entry
    return y


@op
def getting_label_names(context, iris):
    y_names = iris.target_names
    return y_names


@op
def fitting_predictions(context, x):
    test_ids = np.random.permutation(len(x))
    return test_ids


@op
def splitting_train_test(context, x, y, test_ids):
    x_train = x[test_ids[:-10]]
    y_train = y[test_ids[:-10]]
    x_test = x[test_ids[-10:]]
    y_test = y[test_ids[-10:]]
    return (
        x_train,
        y_train,
        x_test,
        y_test,
    )


@op
def fit_data(context, x, y, test_ids):
    clf = tree.DecisionTreeClassifier()
    clf.fit(x[test_ids[:-10]], y[test_ids[:-10]])
    return clf


@op
def predict_data(context, clf, x_test):
    pred = clf.predict(x_test)
    return pred


@op
def save_result(context, pred):
    with open("prediciton.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=" ")
        writer.writerow(pred)
