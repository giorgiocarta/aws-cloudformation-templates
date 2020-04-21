# Lambda Guidelines

[Credit: Jeremy Daly](from https://www.jeremydaly.com/serverless-microservice-patterns-for-aws/)

Much like the term “serverless”, there is no formal, agreed upon definition of what a “microservice” actually consists of. However, serverless microservices should at least adhere to the following standards:

- Services should have their own private data
If your microservice is sharing a database with another service, 
either separate/replicate the data, or combine the services. 
If none of those work for you, rethink your strategy and architecture.
- Services should be independently deployable
Microservices (especially serverless ones) should be completely independent and self-contained. 
It’s fine for them to be dependent on other services or for others to rely on them, but those 
dependencies should be entirely based on well-defined communication channels between them.
- Utilize eventual consistency
Data replication and denormalization are core tenets within microservices architectures. 
Just because Service A needs some data from Service B, doesn’t mean they should be combined. 
Data can be interfaced in realtime through synchronous communication if feasible, 
or it can be replicated across services. Take a deep breath relational database people, this is okay.
- Use asynchronous workloads whenever possible
AWS Lambda bills you for every 100 ms of processing time you use. 
If you are waiting for other processes to finish, you are paying to have your functions wait.
This might be necessary for lots of use cases, but if possible,
 hand off your tasks and let them run in the background. 
 For more complicated orchestrations, use Step Functions.
- Keep services small, but valuable
It’s possible to go too small, but it is also likely that you can go too big. Your “microservices” architecture shouldn’t be a collection of small “monoliths” that handle large application components. It is okay to have a few functions, database tables, and queues as part of a single microservice. If you can limit the size, but still provide sufficient business value, you’re probably where you need to be.
