#!/bin/bash

# crate a stack on AWS
aws --profile <YOUR PROFILE> cloudformation create-stack \
 --capabilities CAPABILITY_IAM \
 --stack-name s3-website-logs \
 --template-body file://static_site_template.yaml \
 --parameters \
 ParameterKey=VPC,ParameterValue=<VPC ID> \
 ParameterKey=Subnet,ParameterValue=<SUBNET ID> \
 ParameterKey=Environment,ParameterValue=Staging \
 ParameterKey=KeyPair,ParameterValue=Ireland
