#!/bin/bash

# crate a Staging VCP network
aws cloudformation update-stack --stack-name private-subnet \
--capabilities CAPABILITY_IAM \
 --template-body file://template.yaml \
ParameterKey=VPC,ParameterValue=<YOUR DEFAULT VPC ID> \
ParameterKey=PublicSubnetId,ParameterValue=<A DEFAULT VPC ID> \
ParameterKey=KeyPair,ParameterValue=Ireland