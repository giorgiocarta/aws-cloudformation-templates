#!/bin/bash

aws cloudformation create-stack --capabilities CAPABILITY_NAMED_IAM --stack-name events-to-s3 \
 --template-body file://template.yaml