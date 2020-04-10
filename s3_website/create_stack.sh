#!/bin/bash

# crate a stack on AWS
aws --profile <YOUR PROFILE> cloudformation create-stack \
 --capabilities CAPABILITY_IAM \
 --stack-name static-website \
 --template-body file://static_site_template.yaml \
 --parameters \
 ParameterKey=VPC,ParameterValue=<ENTER HERE A VPC ID> \
 ParameterKey=Subnet,ParameterValue=<ENTER HERE A SUBNSET ID> \
 ParameterKey=Environment,ParameterValue=Staging
