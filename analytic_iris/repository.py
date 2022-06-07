from dagster import repository

from analytic_iris.jobs.say_hello import say_hello_job
from analytic_iris.schedules.my_hourly_schedule import my_hourly_schedule
from analytic_iris.sensors.my_sensor import my_sensor


@repository
def analytic_dados_enem():
    """
    The repository definition for this analytic_dados_enem Dagster repository.

    For hints on building your Dagster repository, see our documentation overview on Repositories:
    https://docs.dagster.io/overview/repositories-workspaces/repositories
    """
    jobs = [say_hello_job]
    schedules = [my_hourly_schedule]
    sensors = [my_sensor]

    return jobs + schedules + sensors
