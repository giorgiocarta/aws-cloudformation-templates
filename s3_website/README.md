## Public S3 bucket serving a static website content

Execute the stack with 

```bash
./create_stack.sh
```

When stack is completed, issue: 

```bash
./describe bucket 
```

Take note of of the 
- bucket name (`BuckeName`)
- website url (`WebsiteURL`)

Manually copy website content:
```bash
aws s3 sync www s3://<YOUR BUCKET NAME HERE>
```

View the website by visiting the `WebsiteUrl`

### Notess:

Before you can delete the stack, you first need to delete the objects from s3:

```bash
aws s3 rm s3://<YOUR BUCKET NAME HERE> --recursive
```