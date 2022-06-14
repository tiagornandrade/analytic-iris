from dagster import repository

from analytic_iris.jobs.job_iris import etl
from analytic_iris.schedules.my_hourly_schedule import my_hourly_schedule
from analytic_iris.sensors.my_sensor import my_sensor


@repository
def iris():
    jobs = [etl]
    schedules = [my_hourly_schedule]
    sensors = [my_sensor]

    return jobs + schedules + sensors
