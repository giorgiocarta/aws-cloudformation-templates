#!/bin/bash

# crate a stack on AWS
aws cloudformation create-stack \
 --stack-name s3-static-site \
 --template-body file://s3_static_website.yaml
