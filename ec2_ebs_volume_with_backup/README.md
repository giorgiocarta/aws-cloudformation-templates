## EC2 instance with EBS volume and lifecycle policy for backup

Creates an EC2 instance with an EBS volume attached, and a 24 hours snapshot policy.


This policy will create a snapshot of all tagged volumes with
 
- `Backuo` : `Daily` 

every 24 hours starting at 13:00 UTC. 
A maximum of 1 snapshots will be retained of a target volume. 
The oldest snapshot retained will be <= 24 hours old.




SSH access is enabled using pem key.

Before you can load this stack, you need to create the life policy default role.
This is done only once manually with the command below, or the first time
you create a lifecycle manually using the aws portal.

```bash
aws dlm create-default-role
```
