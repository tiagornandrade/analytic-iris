from dagster import RunRequest, sensor

from analytic_iris.jobs.job_iris import etl


@sensor(job=etl)
def my_sensor(_context):
    should_run = True
    if should_run:
        yield RunRequest(run_key=None, run_config={})
