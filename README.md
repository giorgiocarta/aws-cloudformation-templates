# aws-cloudformation-templates


## /static_site

Quick example on how to publish a site hosted on S3 onto a 
EC2 instance.

In this example, a website zipped into a file called tokyo.zip 
is uploaded from S3, unpacked and copied into the www folder of the instance.
A simple apache http server is also started.

Attached to the Ec2 instance, the template defines:
 - AIM role attached to the EC2 instance to allow the instance to read from S3
 - EC2 security group only allowing inbound connection only for http and https
 
SSH connection to server is forbidden.


