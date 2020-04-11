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

## /s3_website_with_logs

Quick example on how to publish a site hosted on S3 onto a EC2 instance
and log the apache server `access_log` directly to cloudwatch.

Attached to the Ec2 instance, the template defines:
 - AIM role attached to the EC2 instance to allow the instance to read from S3 and put logs to cloudwatch
 - EC2 security group only allowing inbound connection for http and https, and SSH
 
 SSH connection is allowed, but requires an SSH key.
 
 ## /ec2_with_ebs_volume
 
Example of a EC2 instance with a EBS volume attached, formatted and mounted 
in a `/data` folder of the instance.