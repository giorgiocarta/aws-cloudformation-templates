import json
import boto3
import time
import os

# Create SQS client
sqs = boto3.client('sqs')
# Get queue url from env
queue_url = os.getenv('SQS_QUEUE')

"""
Message attributes are supposed to be used as message metadata 
(like timestamp or possibly some category) and not the message itself. 
"""


def lambda_handler(event, context):
    """
    Entry point
    :param event:
    :param context:
    :return:
    """
    return Router(event=event, context=context).route()


def create_item(event, _):
    """
    Create an item
    :param event:
    :param _:
    :return:
    """
    data = json.loads(event['body'])
    timestamp = str(time.time())

    # here the code to push the event to the queue

    response = sqs.send_message(
        QueueUrl=queue_url,
        DelaySeconds=10,
        MessageAttributes={
            'Event': {
                'DataType': 'String',
                'StringValue': 'INSERT'
            },
            'ArrivedAt': {
                'DataType': 'Number',
                'StringValue': timestamp
            }
        },
        MessageBody=json.dumps(
            {
                'title': data['title'],
                'publication_year': data['publication_year']
            }
        )
    )

    # send event to queue

    return {
        "statusCode": 200,
        "body": json.dumps({"messageId": response['MessageId']})
    }


def delete_item(event, _):
    """
    Delete an item
    :param event:
    :param _:
    :return:
    """

    timestamp = str(time.time())

    response = sqs.send_message(
        QueueUrl=queue_url,
        DelaySeconds=10,
        MessageAttributes={
            'Event': {
                'DataType': 'String',
                'StringValue': 'INSERT'
            },
            'ArrivedAt': {
                'DataType': 'Number',
                'StringValue': timestamp
            }
        },
        MessageBody=json.dumps(
            {
                "id": event['pathParameters']['id']
            }
        )
    )

    # send event to queue

    return {
        "statusCode": 200,
        "body": json.dumps({"messageId": response['MessageId']})
    }


def post_item(event, _):
    """
    Update an item
    :param event:
    :param _:
    :return:
    """

    data = json.loads(event['body'])

    timestamp = int(time.time() * 1000)

    response = sqs.send_message(
        QueueUrl=queue_url,
        DelaySeconds=10,
        MessageAttributes={
            'Event': {
                'DataType': 'String',
                'StringValue': 'INSERT'
            },
            'ArrivedAt': {
                'DataType': 'Number',
                'StringValue': timestamp
            }
        },
        MessageBody=json.dumps(
            {
                'id': event['pathParameters']['id'],
                'title': data['title'],
                'publication_year': data['publication_year']
            }
        )
    )

    # send event to queue

    return {
        "statusCode": 200,
        "body": json.dumps({"messageId": response['MessageId']})
    }


collectionHandlers = {
    "POST": create_item,
}

# this methods need an item id
itemHandlers = {
    "DELETE": delete_item,
    "POST": post_item,
}


class Router:

    def __init__(self, event, context):
        self._httpMethod = event["httpMethod"]
        self._path_parameter = event.get('pathParameters', None)
        self._context = context
        self._event = event

    def route(self, *args, **kwargs):
        routes = itemHandlers if self._path_parameter else collectionHandlers
        if self._httpMethod in routes:
            method_to_call = routes[self._httpMethod]
            return method_to_call(self._event, self._context)
