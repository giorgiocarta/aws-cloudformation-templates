#!/bin/bash

# crate a stack on AWS
aws cloudformation create-stack \
 --capabilities CAPABILITY_IAM \
 --stack-name asg-lb \
 --template-body file://template.yaml
