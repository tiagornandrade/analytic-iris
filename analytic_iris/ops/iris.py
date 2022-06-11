import os
import pandas as pd
from dagster import op


@op
def etl_iris(context):
    data = 'https://raw.githubusercontent.com/plotly/datasets/master/iris-data.csv'
    data_path = "c:\\Temp\\stage\\"

    iris = pd.read_csv(data)
    iris = iris[(iris["class"] == 'Iris-setosa') & (iris["sepal length"] > 5.0)]
    iris.to_csv(data_path + "iris_filtro.csv", index=False)