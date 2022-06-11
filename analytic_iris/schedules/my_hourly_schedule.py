from dagster import schedule

from analytic_iris.jobs.job_iris import etl


@schedule(cron_schedule="0 * * * *", job=etl, execution_timezone="US/Central")
def my_hourly_schedule(_context):
    run_config = {}
    return run_config
