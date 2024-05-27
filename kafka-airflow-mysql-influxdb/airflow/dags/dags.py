from datetime import timedelta, datetime
from airflow import DAG
from airflow.providers.mysql.hooks.mysql import MySqlHook
from airflow.operators.python import PythonOperator
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from airflow.providers.mysql.operators.mysql import MySqlOperator
import pandas as pd
from airflow.decorators import task
import json
import boto3
import logging
import pprint
import pendulum
import datetime
from airflow.decorators import dag, task
from airflow.models.param import Param
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from airflow.providers.amazon.aws.operators.s3 import (
    S3CopyObjectOperator,
    S3CreateBucketOperator,
    S3CreateObjectOperator,
    S3DeleteBucketOperator,
    S3DeleteBucketTaggingOperator,
    S3DeleteObjectsOperator,
    S3FileTransformOperator,
    S3GetBucketTaggingOperator,
    S3ListOperator,
    S3ListPrefixesOperator,
    S3PutBucketTaggingOperator,
)

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

s3_config = {
    'aws_access_key_id': 'Z8QCI7UAOC4NP9F841NP',
    'aws_secret_access_key': 'eWhtoNDgDOs5W7K80eDNhklKuo9d0GAvIzUi5myt',
    'endpoint_url': 'https://baobab.ncsoft.com',
    'region_name': 'default',
    'bucket_name': 'inspire12',
    'service_name':'s3'
}

with DAG(
        'kafka_to_s3_to_mysql',
        default_args=default_args,
        description='Load data from S3 and store it into MySQL',
        schedule_interval=timedelta(days=1),
        start_date=datetime(2021, 1, 1),
        catchup=False,
) as dag:

    @task(task_id="fetch_from_s3")
    def fetch_from_s3(**kwargs):
        s3r = boto3.resource(
            region_name=s3_config['region_name'],
            endpoint_url=s3_config['endpoint_url'],
            aws_access_key_id=s3_config.get('aws_access_key_id'),
            aws_secret_access_key=s3_config.get('aws_secret_access_key'),
            service_name=s3_config['service_name']
        )
        logging.info('1')
        for raw_bucket in s3r.buckets.all():
            logging.info(raw_bucket.name)
        logging.info('2')
        bucket = s3r.Bucket(s3_config['bucket_name'])
        prefix = 'test'
        data = {
            "login_name": "inspire123",
            "created_at": "",
            "result": "success"
        }
        logging.info('3')
        logging.info(bucket.objects)
        logging.info('4')
        for object in bucket.objects.all():
            logging.info('{} test', object.key)

            data = object.get()['Body'].read()

        # hook = S3Hook(aws_conn_id='aws_default')
        # content = hook.read_key(key, bucket_name=bucket_name)
        # data = json.loads(content)
        # return data
    run_fetch_from_s3 = fetch_from_s3()

    @task(task_id="process_data")
    def process_data(**kwargs):
        logging.info(kwargs)
        ti = kwargs['ti']
        raw_data = ti.xcom_pull(task_ids='fetch_data')
        df = pd.DataFrame(raw_data)
        # 데이터를 필요에 따라 변환
        processed_data = df.to_json(orient='records')
        ti.xcom_push('processed_data', processed_data)

    run_process_data = process_data()
    @task(task_id="save_to_mysql")
    def save_to_mysql(**kwargs):
        sql = "show databases;"
        ti = kwargs['ti']
        data = json.loads(ti.xcom_pull(key='processed_data'))
        hook = MySqlHook(mysql_conn_id='mysql_default')
        for record in data:
            hook.run(sql, parameters=record)


    run_save_to_mysql = save_to_mysql()


@dag(
    description='주기적 삭제 대상 게스트 계정에게 push 사전 고지 완료 키 값 변경',
    start_date=pendulum.datetime(2022, 6, 30),
    catchup=False,
    schedule=None,
    tags=['account_purge_regular'],
    params={
        "object_key": Param(default="notify_read_complete_live/guest_purge_notify_1681782470.3132_150.csv",
                            type="string"),
    }
)
def account_guest_purge_push_notify_retry():
    """
    ### push 실패 처리용 DAG \n
    #### read complete object key 를 파라미터로 전달 받아, 다시 push 전송되도록 key 값을 변경한다.
    """

    @task
    def copy_and_delete(**kwargs):
        AWS_CONN_ID = 'account-shield'
        GUEST_PURGE_BUCKET_NAME = 'account-shield'

        s3_hook = S3Hook(aws_conn_id=AWS_CONN_ID)
        object_key = kwargs['params']['object_key']

        key_list = object_key.split(',')
        for key in key_list:
            dest = 'notify_upload_live/{}'.format(key.replace('notify_read_complete_live/', ''))
            print(dest)
            # s3_hook.copy_object(source_bucket_key=key, source_bucket_name=GUEST_PURGE_BUCKET_NAME,
            #                     dest_bucket_key=dest, dest_bucket_name=GUEST_PURGE_BUCKET_NAME)
            # s3_hook.delete_objects(bucket=GUEST_PURGE_BUCKET_NAME, keys=key)

        return key_list

    copy_and_delete_task = copy_and_delete()

    # account_guest_purge_push_notify_retry_dag = account_guest_purge_push_notify_retry()
# fetch_from_s3 >> run_process_data >> run_save_to_mysql()