# AutoScalingGroup with Notifications

```
                                  ┌──────────────────┐ ┌──────────────────┐ ┌──────────────────┐
                                  │                  │ │                  │ │                  │
                                  │                  │ │                  │ │                  │
┌──────────────────────────┐      │  ┌────────────┐  │ │  ┌────────────┐  │ │  ┌────────────┐  │
│                          │      │  │            │  │ │  │            │  │ │  │            │  │
│                          │      │  │            │  │ │  │            │  │ │  │            │  │
│                          │      │  │            │  │ │  │            │  │ │  │            │  │
│     Instance Factory     │────▶ │  │   EC2 A    │  │ │  │   EC2 B    │  │ │  │   EC2 C    │  │
│        (launcher)        │      │  │            │  │ │  │            │  │ │  │            │  │
│                          │      │  │            │  │ │  │            │  │ │  │            │  │
│                          │      │  │            │  │ │  │            │  │ │  │            │  │
│                          │      │  └────────────┘  │ │  └────────────┘  │ │  └────────────┘  │
└──────────────────────────┘      │                  │ │                  │ │                  │
                                  │                  │ │                  │ │                  │
                                  │                  │ │                  │ │                  │
                                  │                  │ │                  │ │                  │
                                  │                  │ │                  │ │                  │
                                  │    ┌────────┐    │ │   ┌────────┐     │ │    ┌────────┐    │
                                  │    │  AZ1   │    │ │   │  AZ2   │     │ │    │  AZ3   │    │
                                  │    └────────┘    │ │   └────────┘     │ │    └────────┘    │
                                  └──────────────────┘ └──────────────────┘ └──────────────────┘
                                                                                                
                                           ▲                    ▲                    ▲          
                                           │                    │                    │          
┌─────────────────────────┐       ┌────────┴────────────────────┴────────────────────┴─────────┐
│         SnS/SQS         │       │                      AutoScalingGroup                      │
│                         │◀──────│               [keep three instances running]               │
└─────────────────────────┘       └────────────────────────────────────────────────────────────┘
```

In this template I create:

1. Launcher configuration: this works like a template for to create an individual EC2 instance. 
   Is essentially a EC2 factory. Does not create per se an instance, rather describe how to create
   one
2. An autoscaling group: this uses the launcher and keeps the fleet of EC2 instance to 
   the desired number and state.

3. The austoscaling group will send notification to SQS and SnS topic when EC2 instances
   are scaling up or down.
   