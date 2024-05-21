from datetime import datetime

from airflow.operators.python_operator import PythonOperator
from pymongo import MongoClient
from airflow.decorators import dag, task

def my_task():
    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.your_database
    collection = db.your_collection

    # Perform operations on the MongoDB data
    # Example: Fetch documents from the collection
    documents = collection.find({})
    for document in documents:
        print(document)
#Create a DAG object and define its parameters:
@dag(
    dag_id='run_etl_job',
    schedule='*/5 * * * *',  # Set the schedule as per your requirement
    start_date=datetime.datetime(2023, 6, 29),  # Set the start date
)
def run_etl_job():
    pass