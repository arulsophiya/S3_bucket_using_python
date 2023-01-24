import boto3

def create_bucket(bucket_name, region):
    s3_client = boto3.client('s3', region_name=region)
    location = {'LocationConstraint': region}
    s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)

create_bucket("test-bucket-09764", "ap-south-1")



