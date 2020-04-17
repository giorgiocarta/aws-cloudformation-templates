#!/bin/bash

# update the stack on AWS
aws cloudformation update-stack --stack-name custom-vpc \
 --template-body file://template.yaml \
 --parameters \
 ParameterKey=VPCName,ParameterValue=CUSTOM-VPC \
 ParameterKey=Environment,ParameterValue=PRODUCTION \
 ParameterKey=BastionKeyPair,ParameterValue=Ireland

