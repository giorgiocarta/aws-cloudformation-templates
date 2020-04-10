# Site uploaded from S3 

This example upload a website from s3 and serves it using apache httpd, 

Before you run the template, upload the following file to a s3 bucket of
your choice (I use a bucket named gcdataset for testing):

```bash
aws s3 cp tokio.zip  s3://gcdataset/tokio.zip
```

## Notes about the user data section

First we update yum, and install httpd. 
```bash
#! /bin/bash
sudo yum -y update
sudo yum install httpd -y
```

Then we copy the zipped website and we unpack it into the www folder.
```bash
aws s3 cp s3://gcdataset/tokyo.zip .
unzip tokyo.zip -d /var/www/html/
```

Finally we start the server
```bash
service httpd start
```