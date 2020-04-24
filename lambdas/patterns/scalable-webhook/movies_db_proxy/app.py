import json
import boto3
import os


def lambda_handler(event, context):
    """
    This Lambda connect to a DB instance and run CRUD operations
    on a DB. NOT IMPLEMENTED.
    :param event:
    :param context:
    :return:
    """
    print(event)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": event
            # "location": ip.text.replace("\n", "")
        }),
    }
