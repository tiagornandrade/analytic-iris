from analytic_iris.ops.iris import (
    etl_iris,
    array_data,
    array_labels,
    getting_label_names,
    fitting_predictions,
    splitting_train_test,
    fit_data,
    predict_data,
    save_result,
)


def test_etl_iris():
    assert etl_iris() == "Hello, Dagster!"


def test_array_data():
    assert array_data() == "Hello, Dagster!"


def test_array_labels():
    assert array_labels() == "Hello, Dagster!"


def test_getting_label_names():
    assert getting_label_names() == "Hello, Dagster!"


def test_fitting_predictions():
    assert fitting_predictions() == "Hello, Dagster!"


def test_splitting_train_test():
    assert splitting_train_test() == "Hello, Dagster!"


def test_fit_data():
    assert fit_data() == "Hello, Dagster!"


def test_predict_data():
    assert predict_data() == "Hello, Dagster!"


def test_save_result():
    assert save_result() == "Hello, Dagster!"
