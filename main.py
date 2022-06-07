import os
import pandas as pd
from dagster import job, op


data_path = "c:\\Temp\\stage\\"
arquivo = data_path + "iris.csv"


@op
def extract_iris_dataset(context):
    data = os.system(
        "curl https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv -o c:\Temp\stage\iris.csv"
    )
    return data


@op
def aplica_filtros(context, data):
    iris = pd.read_csv(arquivo, sep=",", decimal=".")
    iris = iris.loc[(iris.species == "setosa") & (iris.sepal_length > 5.0)]
    iris.to_csv(data_path + "iris_filtro.csv", index=False)


@job
def etl():
    pre_load = extract_iris_dataset()
    aplica_filtros(pre_load)
