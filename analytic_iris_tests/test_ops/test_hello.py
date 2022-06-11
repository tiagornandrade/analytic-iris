from analytic_iris.ops.iris import extract_iris_dataset, aplica_filtros


def test_extract_iris_dataset():
    assert extract_iris_dataset() == "Hello, Dagster!"


def test_aplica_filtros():
    assert aplica_filtros() == "Hello, Dagster!"
