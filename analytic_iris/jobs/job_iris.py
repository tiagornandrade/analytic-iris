from dagster import job

from analytic_iris.ops.iris import etl_iris

@job
def etl():
    pre_load = etl_iris()
