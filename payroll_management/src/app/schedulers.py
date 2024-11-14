#!/usr/bin/python3
"""Module to set scheduler variables"""

import pytz
from app.database import DATABASE_URL
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ProcessPoolExecutor, ThreadPoolExecutor

jobstores = {'default': SQLAlchemyJobStore(
    url=DATABASE_URL or 'sqlite:///./asset_store.db')}

executors = {'default': ThreadPoolExecutor(
    20), 'processpool': ProcessPoolExecutor(5)}

job_defaults = {'coalesce': False, 'max_instances': 3}

scheduler = BackgroundScheduler(jobstores=jobstores,
                                executors=executors,
                                job_defaults=job_defaults,
                                timezone=pytz.utc,
                                misfire_grace_time=60)
