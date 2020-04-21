import json
import boto3
import time
import decimal
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Movies')


# This is a workaround for: http://bugs.python.org/issue16535
class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return int(obj)
        return super(DecimalEncoder, self).default(obj)


def lambda_handler(event, context):
    """
    Entry point
    :param event:
    :param context:
    :return:
    """
    return Router(event=event, context=context).route()


def list_items(event, _):
    """
    list items
    :param event:
    :param _:
    :return:
    """

    result = table.scan()

    return {
        "statusCode": 200,
        "body": json.dumps(result['Items'], cls=DecimalEncoder),
    }


def create_item(event, _):
    """
    Create an item
    :param event:
    :param _:
    :return:
    """
    data = json.loads(event['body'])
    timestamp = str(time.time())

    item = {
        'id': str(uuid.uuid1()),
        'title': data['title'],
        'publication_year': data['publication_year'],
        'updatedAt': timestamp,
        'createdAt': timestamp

    }
    table.put_item(Item=item)
    return {
        "statusCode": 200
    }


def delete_item(event, _):
    """
    Delete an item
    :param event:
    :param _:
    :return:
    """

    table.delete_item(
        Key={
            'id': event['pathParameters']['id']
        }
    )
    return {
        "statusCode": 200
    }


def get_item(event, _):
    """
    Returns an item
    :param event:
    :param _:
    :return:
    """

    result = table.get_item(
        Key={
            'id': event['pathParameters']['id']
        }
    )
    return {
        "statusCode": 200,
        "body": json.dumps(result['Item'], cls=DecimalEncoder),
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

    result = table.update_item(
        Key={
            'id': event['pathParameters']['id']
        },
        ExpressionAttributeValues={
            ':title': data['title'],
            ':publication_year': data['publication_year'],
            ':updatedAt': timestamp,
        },
        UpdateExpression='SET title = :title, '
                         'publication_year = :publication_year, '
                         'updatedAt = :updatedAt',
        ReturnValues='ALL_NEW',
    )

    return {
        "statusCode": 200,
        "body": json.dumps(result['Attributes'], cls=DecimalEncoder),
    }


collectionHandlers = {
    "GET": list_items,
    "POST": create_item,
}

# this methods need an item id
itemHandlers = {
    "DELETE": delete_item,
    "GET": get_item,
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
