#!/usr/bin/python3
import boto3
from botocore.client import Config

# 토큰 획득을 위해 LDAP 인증 문자열 access_key 제공
access_key = 'Z8QCI7UAOC4NP9F841NP'
secret_key = 'eWhtoNDgDOs5W7K80eDNhklKuo9d0GAvIzUi5myt'

# LDAP 인증 문자열로 'sts' 클라이언트 인스턴스 생성
sts_client = boto3.client('sts',
                          aws_access_key_id=access_key,
                          aws_secret_access_key=secret_key,
                          endpoint_url='https://baobab.ncsoft.com',
                          region_name='default',
                          verify=True,
                          config=Config(signature_version='s3v4'),
                          )

# 임시 자격 증명 세션 토큰 발급
# 세션 토큰은 6시간(43200초) 동안 유효함
response = sts_client.get_session_token(DurationSeconds=43200)

s3client = boto3.client('s3',
                        aws_access_key_id=response['Credentials']['AccessKeyId'],
                        aws_secret_access_key=response['Credentials']['SecretAccessKey'],
                        aws_session_token=response['Credentials']['SessionToken'],
                        endpoint_url='https://baobab.ncsoft.com',
                        region_name='default'
                        )

response = s3client.list_buckets()

for bucket in response["Buckets"]:
    print("{name}\t{created}".format(
        name=bucket['Name'],
        created=bucket['CreationDate'], ))