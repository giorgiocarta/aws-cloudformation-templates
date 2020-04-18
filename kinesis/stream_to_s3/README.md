# Kinesis Events to S3

This stack captures events using Kinesis Firehose and dumps them on S3.

To test the application, you can run the application use the python file provided.

## Test with python script

Install a virtual env:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install boto3
python send_test_events.py
```

The script will send 1,000 events directly to kinesis firehose.

To view the events:

```bash
aws s3 ls s3://<aws-account-id>-kinesis-events/events/
```

The events are stored using the following convention:

```
s3://<aws-account-id>-kinesis-events/events/YYYY/MM/DD/HH/DeliveryToS3-<date>-hash.gz
```

## Note:
The bucket has a life-cycle policy that delete the records older than 30 days.

## Note 2:
When deleting the stack, the destination bucket must be emptied of all the objects.

e.g.
```
aws s3 rm s3://bucket-name/ --recursive
```