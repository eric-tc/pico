from celery import Celery

import logging
logging.basicConfig(level=logging.INFO)

#SQL ALCHEMY CONNECTION

from sqlalchemy import create_engine, Column, Integer, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import BaseConfig
from app.models import User
import time

# Create the database engine and tables
engine = create_engine(BaseConfig.SQLALCHEMY_DATABASE_URI)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

print("App Data")

print(session.query(User).all())


#db inside postgres used to save result of task executed
celery_database_uri= f'db+postgresql://{BaseConfig.DB_USER}:{BaseConfig.DB_PASS}@postgres:{BaseConfig.DB_PORT}/{BaseConfig.DB_NAME}'

print(f"CELERY URL{celery_database_uri} ")
celery = Celery(
    'tasks',
    broker='redis://redis:6379/0',  # Redis as the message broker
    #backend='postgresql://username:password@localhost:5432/dbname',  # PostgreSQL as the backend
    backend=celery_database_uri
)

@celery.task
def add_numbers(x, y):
    result = x + y
    # Save the result to the database
    #result = session.query(User).all()
    #print(result)
    
    logging.info(f"Result: {result}")
    print("Inside task")
    return result

@celery.task
def check():
    
    print("Repeating task is running.")
    # Add your task logic here
    time.sleep(1)
    print("Repeating task completed.")


#scheduler task 
celery.conf.beat_schedule = {
    "run-me-every-ten-seconds": {
    "task": "tasks.check",
    "schedule": 10.0
    }
 }