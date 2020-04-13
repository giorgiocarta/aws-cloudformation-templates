#!/bin/bash

# crate a stack on AWS
aws --profile giorgio2 cloudformation create-stack \
 --stack-name s3-static-site \
 --template-body file://s3_static_website.yaml
