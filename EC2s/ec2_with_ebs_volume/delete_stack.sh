#!/bin/bash

# delete a stack on AWS
aws --profile <PROFILE> cloudformation delete-stack --stack-name ec2-with-volume


