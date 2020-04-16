from unittest.mock import patch
from unittest import TestCase
import pytest
from create_bucket import app


class MockContext(object):
    function_name = "test-function"
    ms_remaining = 9000

    @staticmethod
    def get_remaining_time_in_millis():
        return MockContext.ms_remaining


@pytest.fixture()
def apigw_create_event():
    """ Generates API GW Event"""

    return {
        "StackId": "somestack/testme",
        "RequestId": "1234",
        "LogicalResourceId": "1234",
        "RequestType": "create",
        "ResponseURL": "http://someaddress.com",
        "ResourceProperties": {
            "DestBucketName": "aaa",
            "DestBucketRegion": "bbb"
        }
    }


@pytest.fixture()
def apigw_delete_event():
    """ Generates API GW Event"""

    return {
        "StackId": "somestack/testme",
        "RequestId": "1234",
        "LogicalResourceId": "1234",
        "RequestType": "delete",
        "ResponseURL": "http://someaddress.com",
        "ResourceProperties": {
            "DestBucketName": "aaa",
            "DestBucketRegion": "bbb"
        }
    }


@patch("create_bucket.app.boto3")
def test_lambda_handler__create_event(boto3, apigw_create_event):
    c = MockContext()
    app.handler(apigw_create_event, c)
    assert app.helper.Data == {'event': 'created'}
    assert app.helper.Status == 'SUCCESS'


@patch("create_bucket.app.boto3")
def test_lambda_handler__delete_event(boto3, apigw_delete_event):
    c = MockContext()
    app.handler(apigw_delete_event, c)
    assert app.helper.Data == {'event': 'deleted'}
    assert app.helper.Status == 'SUCCESS'
