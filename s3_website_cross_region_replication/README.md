# replica-bucket

Deploy a encrypted and versioned bucket with a twin cross-region replica for backup.

Will create the following:

1. bucket-<AWS_ACCOUNT_ID>-encr (in eu-west-1)
2. bucket-<AWS_ACCOUNT_ID>-encr-replica (in eu-central-1)

You can change bucket names and the replica region by 
editing the template.yaml

## Project setup

Cd into this folder and install a 3.7 virtual env:

```bash
python3.7 -m venv .venv
pip install -r ./crate_bucket/requirements.txt
pip install -e .

# if everything is ok, unit tests should work fine
pytest
```

## Deploy the stack

```bash
replica-bucket$ sam build
replica-bucket$ sam deploy
```

## Cleanup

To delete the sample application that you created, use the AWS CLI. Assuming you used your project name for the stack name, you can run the following:

```bash
aws cloudformation delete-stack --stack-name replica-bucket
```

Note: you will have to remove the bucket manually - this is intended to avoid unintentional deletes.