# Highly available VPC configuration for Web Server

This stack configure a VPC designed to serve a web application
with high availability.

```
  ┌─────────────┐                                                              
┌─┤ 10.0.0.0/16 ├────────────────────────────────────────────────┬────────────┐
│ └─────────────┘                                                │            │
│    ┌─────────────┐                 ┌─────────────┐             │    Nat     │
│   ┌┤ 10.0.1.0/24 ├─────────┐     ┌─┤ 10.0.2.0/24 ├────────┐    │  Gateway   │
│   │└─────────────┘         │     │ └─────────────┘        │    │            │
│   │                        │     │                        │    ├────────────┘
│   │     ┌──────────────┐   │     │  ┌──────────────┐      │    │             
│   │     │              │   │     │  │              │      │    │             
│   │     │  WebServerA  │   │     │  │  WebServerB  │      │    │             
│   │     │              │   │     │  │              │      │    │             
│   │     └──────────────┘   │     │  └──────────────┘      │    │             
│   │                        │     │                        │    │             
│   │                        │     │                        │    │             
│   │┌────────┐              │     │             ┌────────┐ │    │             
│   ││Private │              │     │             │Private │ │    │             
│   │└────────┘              │     │             └────────┘ │    │             
│   └────────────────────────┘     └────────────────────────┘    │             
│                                                                │             
│    ┌─────────────┐                  ┌─────────────┐            │             
│   ┌┤ 10.0.3.0/24 ├─────────┐      ┌─┤ 10.0.4.0/24 ├────────┐   │             
│   │└─────────────┘         │      │ └─────────────┘        │   │             
│   │                        │      │                        │   │             
│   │                        │      │                        │   │             
│   │           ┌────────────┴──────┴─────────────┐          │   │             
│   │           │                                 │          │   │             
│   │           │                                 │          │   │             
│   │           │          Load Balancer          │          │   │             
│   │           │                                 │          │   │             
│   │           │                                 │          │   │             
│   │ ┌────────┐└────────────┬──△───┬─────────────┘┌────────┐│   │             
│   │ │ Public │             │  │   │              │ Public ││   │             
│   │ └────────┘             │  │   │              └────────┘│   │             
│   └────────────────────────┘  │   └────────────────────────┘   │             
│                               │                                │             
└───────────────────────────────┼────────────────────────────────┘             
                                │                                              
                                │                                              
                           ┌─────────┐                                         
                           │  Users  │                                         
                           └─────────┘                                         
```

1. The webserver are only accessible through the load balancer and only accept  TCP on 80 and 443
2. Traffic between the subnets is allowed by default route tables
3. The only route to the internet for the web servers is tunnelled through a Nat Gateway with EIP
4. The load balancer sits between two publich Subnets and AZs
5. The webservers are indentical, but located into two separate AZs and subnet. 
6. If one AZ fails, everything is still served because ELB and EC2 are replicated into 2 different AZs.
7. Security groups on EC2 instances only allow web traffic from private ips in the VPC.