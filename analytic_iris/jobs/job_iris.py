from dagster import job

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


@job
def etl():
    pre_load = etl_iris()
    array_x = array_data(pre_load)
    array_y = array_labels(pre_load)
    getting_label_names(pre_load)
    fit_pred = fitting_predictions(array_x)
    splitting_train_test(array_x, array_y, fit_pred)
    fit = fit_data(array_x, array_y, fit_pred)
    predict = predict_data(fit, array_x)
    save_result(predict)
