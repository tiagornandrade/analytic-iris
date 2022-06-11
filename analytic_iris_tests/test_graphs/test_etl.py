from analytic_iris.jobs.job_iris import etl


def test_etl():
    result = etl.execute_in_process()

    assert result.success
    assert result.output_for_node("hello") == "Hello, Dagster!"
