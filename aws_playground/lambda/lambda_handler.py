import json
import boto3

BUCKET = 'awsplaygroundstack-testingbucket7061cae3-hdvce056y7xq'

def get_bucket():
    s3 = boto3.resource('s3')

    bucket = s3.Bucket(BUCKET)

    return bucket

def main(event, context):

    print(event)

    bucket = get_bucket()

    if bucket:
        print('bucket found!')
        # list all objects in the bucket
        for obj in bucket.objects.all():
            metadata = obj.get()
            print(metadata)

    return {
        'statusCode': 200,
        'body': event
    }