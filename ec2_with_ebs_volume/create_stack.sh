#!/bin/bash

# crate a stack on AWS
aws --profile <YOUR PROFILE> cloudformation create-stack \
 --stack-name ec2-with-volume \
 --template-body file://ec2_ebs_volume.yaml \
 --parameters \
 ParameterKey=VPC,ParameterValue=<VPC ID> \
 ParameterKey=AZ,ParameterValue=eu-west-1a \
 ParameterKey=KeyPair,ParameterValue=Ireland
