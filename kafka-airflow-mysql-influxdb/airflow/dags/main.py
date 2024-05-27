import boto3
import logging
import json

if __name__ == '__main__':
    print("hello")

    s3_config = {
        'aws_access_key_id': 'Z8QCI7UAOC4NP9F841NP',
        'aws_secret_access_key': 'eWhtoNDgDOs5W7K80eDNhklKuo9d0GAvIzUi5myt',
        'endpoint_url': 'https://baobab.ncsoft.com',
        'region_name': 'default',
        'bucket_name': 'inspire12',
        'service_name': 's3'
    }
    s3r = boto3.resource(
        region_name=s3_config['region_name'],
        endpoint_url=s3_config['endpoint_url'],
        aws_access_key_id=s3_config.get('aws_access_key_id'),
        aws_secret_access_key=s3_config.get('aws_secret_access_key'),
        service_name=s3_config['service_name']
    )
    for raw_bucket in s3r.buckets.all():
        print(raw_bucket.name)
    bucket = s3r.Bucket(s3_config['bucket_name'])
    prefix = 'inspire12/'
    data = {
        "login_name": "inspire123",
        "created_at": "",
        "result": "success"
    }
    print(bucket.objects)

    for object in bucket.objects.filter(Prefix=prefix):
        print('{} test', object.key)

        data = object.get()['Body'].read()
        try:
            json_data = json.loads(data)
            print(json_data)
        except Exception as e:
            pass

            # hook = S3Hook(aws_conn_id='aws_default')
            # content = hook.read_key(key, bucket_name=bucket_name)
            # data = json.loads(content)
            # return data
