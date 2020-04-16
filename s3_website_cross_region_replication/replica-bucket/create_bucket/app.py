from crhelper import CfnResource
import boto3

helper = CfnResource()


@helper.create
def create_bucket(event, _):
    destination_bucket = event['ResourceProperties']['DestBucketName']
    destination_region = event['ResourceProperties']['DestBucketRegion']
    s3 = boto3.resource('s3', region_name=destination_region)
    helper.Data['event'] = "created"
    s3.create_bucket(Bucket=destination_bucket, CreateBucketConfiguration={
        'LocationConstraint': destination_region})
    bucket_versioning = s3.BucketVersioning(destination_bucket)
    bucket_versioning.enable()
    s3.meta.client.put_bucket_encryption(
        Bucket=destination_bucket,
        ServerSideEncryptionConfiguration={
            'Rules': [
                {
                    'ApplyServerSideEncryptionByDefault': {
                        'SSEAlgorithm': 'AES256'
                    }
                }
            ]
        }
    )


@helper.delete
def no_op(_, __):
    helper.Data['event'] = "deleted"


def handler(event, context):
    helper(event, context)
