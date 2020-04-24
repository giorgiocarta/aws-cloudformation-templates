# scalable-webhook

f you’re building a webhook, the traffic can often be unpredictable. 
This is fine for Lambda, but if you’re using a “less-scalable” backend like RDS, you might just run into some bottlenecks. 
There are ways to manage this, but now that Lambda supports SQS triggers, we can throttle our workloads by queuing the requests
 and then using a throttled (low concurrency) Lambda function to work through our queue. 
Under most circumstances, your throughput should be near real time. 
If there is some heavy load for a period of time, you might experience some small delays 
as the throttled Lambda chews through the messages.

```
                                                     ┌────────────┐                          
                                                     │            │              .─────────. 
┌─────────────┐   ┌────────────┐   ┌────────────┐    │ ┌──────────┴─┐           (           )
│             │   │            │   │            │    │ │            │           │`─────────'│
│ API Gateway ├───▶   Lamba    ├───▶    SQS     ├───▶│ │  ┌─────────┴──┐  ─────▶│    DB     │
│             │   │            │   │            │    └─┤  │            │        │           │
│             │   │            │   │            │      │  │  ┌─────────┴──┐     │           │
└──────▲──────┘   └────────────┘   └────────────┘      └──┤  │            │     └───────────┘
       │                                                  │  │ Lamba CRUD │                  
 ┌─────┴────┐                                             └──┤            │                  
 │          │                                                │            │                  
 │  Client  │                                                └────┬───────┘                  
 │          │                                                     │                          
 │          │                                                     ▼                          
 └──────────┘                                                ┌────────────┐                  
                                                             │            │                  
                                                             │Dead Letter │                  
                                                             │    SQS     │                  
                                                             │            │                  
                                                             └────────────┘                  


NOTE: The code with the integration betweeen Lambda and RDS is not provided.

AWS recently introduced a new feature for lambda functions called (DBProxy)[https://aws.amazon.com/blogs/compute/using-amazon-rds-proxy-with-aws-lambda/]

This feature is still in Preview and not available yet as a resource in CloudFormation or SAM.

```