# VPC with Bastion

This cloudformation template provision for the following:

- VPC (10.0.0.0/16)
- Public Subnet (10.0.10.0/24)
- Private Subnet (10.0.10.0/24)
- EC2 Bastion Instance running on Public Subnet
- Elastic IP address associated to EC2 bastion instance
- EC2 Isolated instance running on the Private Subnet
- Nat Gateway attached to the public subnet, to allow outgoing TCP traffic from the isolated EC2 instance
- Internet Gateway, attached to public TCP traffic, e.g. for a server running on the http public subnet (not included)
- Some utility security groups:
    1. SSH only
    2. Web only
    3. No connection at all
- Routes table to force network isolation:
    a. public subnet can connect to the internet and to private subnet
    b. private subnet can connect to public subnet, but only ongoing traffic to the internet is allowed.
    c. external clients can only reach instances in the public subnet (if they have a public IP)
- Both Ec2 instance can be accessed using a pem key - this is for testing only. Tipically, the instance
   in the private subnet would be e.g. a database, with different connection protocols.