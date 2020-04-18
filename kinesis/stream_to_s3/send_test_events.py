import boto3
import datetime

client = boto3.client('firehose')

import json

for n in range(1, 1000):
    response = client.put_record(
        DeliveryStreamName='DeliveryToS3',
        Record={
            'Data': json.dumps({
                'example': 'payload' + str(n),
                'emitted_date': str(datetime.datetime.now()),
                'hello': 'world'})
        }
    )

    print(response)
