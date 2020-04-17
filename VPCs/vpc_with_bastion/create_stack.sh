#!/bin/bash

# crate a Staging VCP network
aws cloudformation create-stack --stack-name custom-vpc \
 --template-body file://template.yaml \
 --parameters \
 ParameterKey=VPCName,ParameterValue=CUSTOM-VPC \
 ParameterKey=Environment,ParameterValue=PRODUCTION \
 ParameterKey=BastionKeyPair,ParameterValue=Ireland