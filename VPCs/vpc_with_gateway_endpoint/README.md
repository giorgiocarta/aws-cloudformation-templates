# A practical example of AWS Gateway endpoints.

To follow this tutorial you will need an AWS cloud account, and some familiarity with cloudformation template.

A VPC endpoint enables you to privately connect your VPC to supported AWS services and VPC endpoint services powered by 
AWS PrivateLink without requiring an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection.
Instances in your VPC do not require public IP addresses to communicate with resources in the service. 
Traffic between your VPC and the other service does not leave the Amazon network. 

In this example we will extending the default VPC that comes when you setup a new VPC account. 

I'm working within the Ireland region (eu-west-1), which has 3 AZs. You may need to adjust
this for your setup. 


Below is a general overview of the setup:

```
                 ┌────────────┐                                                         
                 │Local Shell │                                                         
                 └───────┬────┘                                                         
                         │                                                              
  ┌─────────────┐    SSH │                                                              
┌─┤172.31.0.0/16├────────┼─────────────────────────────────────────────────────────────┐
│ └─────────────┘        │                                                             │
│                        │                                                             │
│                        │                                                             │
│  ┌─────────────────────┼──┐   ┌───────────────────────┐   ┌───────────────────────┐  │
│  │          AZ1        │  │   │          AZ2          │   │          AZ3          │  │
│  └─────────────────────┼──┘   └───────────────────────┘   └───────────────────────┘  │
│                        │                                                             │
│    ┌─────────────┐     │      ┌──────────────┐            ┌───────────────┐          │
│  ┌─┤172.31.0.0/20├─────┼──┐  ┌┤172.31.16.0/20├────────┐  ┌┤172.31.32.0/20 ├───────┐  │
│  │ └─────────────┘     ▼  │  │└──────────────┘        │  │└───────────────┘       │  │
│  │              ┌───────┐ │  │                        │  │                        │  │
│  │   public     │EC2 (A)│ │  │   public               │  │   public               │  │
│  │              └──────┬┘ │  │                        │  │                        │  │
│  └─────────────────────┼──┘  └────────────────────────┘  └────────────────────────┘  │
│                        │                                                             │
│                        │                                                             │
│                    SSH │                                                             │
│      ┌──────────────┐  │                                                             │
│   ┌──|172.31.48.0/20|──┼───┐       ┌─────────────────┐                               │
│   │  └──────────────┘  ▼   │       │                 │                               │
│   │  private     ┌───────┐ │       │  VPC Endpoint   │                               │
│   │              │EC2 (B)│─┼──────▶│                 │                               │
│   │              └───────┘ │       │                 │                               │
│   └───────▲────────────────┘       └────────────▲────┘                               │
│           │                                     │                                    │
└───────────X─────────────────────────────────────┼────────────────────────────────────┘
            │                                     │                                     
     ┌──────▼───────┐                  ┌──────────▼───┐                                 
     │              │                  │              │                                 
     │     WEB      │                  │      S3      │                                 
     │              │                  │              │                                 
     └──────────────┘                  └──────────────┘                                 
```

With this stack we create:

1. One Subnet. EC2 instances in this Subnet won't get a public facing IP address, only a private one
2. One VPC endpoint for S3 access
3. One route table for the private Subnet, with rule to direct local VPC traffic and another rule for the S3 VPC endpoint
4. One SG for SSH access from everywhere
5. One SH for SSH access restricted to VPC IPs. 
6. One EC2 instance in the public subnet (i.e. accessible from the web) and with SG no. 4
7. One EC2 instance in the private subnet (without access to the web) and with SG no. 5


Run the stack using the following command.
```bash
aws cloudformation create-stack --stack-name private-subnet \
--capabilities CAPABILITY_IAM \
 --template-body file://template.yaml
 ParameterKey=VPC,ParameterValue=<DEFAULT_VPC_ID> \
 ParameterKey=PublicSubnetId,ParameterValue=<DEFAULT_SUBNET_ID> \
 ParameterKey=KeyPair,ParameterValue=Ireland
```

Replace `DEFAULT_VPC_ID` with the VPC id provided with the aws account
Replace `DEFAULT_SUBNET_ID` with one of the Subnet ids provided with the aws account

This template assumes you have a PEM key stored and named `Ireland`.

To test the solution, once the stack is complete, grap the public ip address 
of the public EC2 instance. e.g. `249.217.161` and the private IP of the instance
in the private subnet (e.g. `172-31-54-148`).

Execute the following commands:
```
scp <path_to_pem>/Ireland.pem ec2-user@249.217.161:~/
ssh -i <path_to_pem>/Ireland.pem ec2-user@249.217.161
scp -i Ireland.pem ec20user@172-31-54-148
aws s3 ls --region eu-west-1
```



