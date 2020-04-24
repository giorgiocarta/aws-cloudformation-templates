# Application Elastic Load balancer with EC2 Target groups

Target groups are just a group of Ec2 instances and are closely associated with ELB:

This is a simple diagram of the template created by the stack:
```
 ┌────────────────┐                                                            
┌┤EC2 Target Group├───────────────────────────────────────────────────────────┐
│└────────────────┘                                                           │
│    ┌────────────┐                               ┌────────────┐              │
│  ┌─┤  Subnet A  ├──────────┐                 ┌──┤  Subnet A  ├─────────┐    │
│  │ └────────────┘          │                 │  └────────────┘         │    │
│  │                         │                 │                         │    │
│  │                         │                 │                         │    │
│  │                         │                 │                         │    │
│  │       ┌────────────┐    │                 │      ┌────────────┐     │    │
│  │       │    EC2     │    │                 │      │    EC2     │     │    │
│  │       │ Instance A │◀─ ─│─ ─ ─ ─ ─ ─ ─ ─ ─│─ ─ ─▶│ Instance B │     │    │
│  │       │            │    │       │         │      │            │     │    │
│  │       └────────────┘    │     Round       │      └────────────┘     │    │
│  │                         │     Robin       │                         │    │
│  │                         │                 │                         │    │
│  └─────────────────────────┘       │         └─────────────────────────┘    │
│                                                                             │
│                                    │                                        │
└────────────────────────────────────▲────────────────────────────────────────┘
                                     │                                         
                        ┌─────────────────────────┐                            
                        │                         │                            
                        │           ALB           │                            
                        │  (EC2 Application Load  │                            
                        │        Balancer)        │                            
                        │                         │                            
                        │                         │                            
                        └────────────▲────────────┘                            
                                     │                                         
                         ┌────────────────────────┐                            
                         │         Client         │                            
                         └────────────────────────┘                            
```

We can just use ELB and Target groups to route requests to EC2 instances. 
With this setup, there is no auto-scaling which means 
instances cannot be added or removed when your load increases/decreases.

The instances are distributed across AZs, so the solution is highly available.
