# Site uploaded from S3 with CloudWatch logs

This example upload a website from s3, uses apache as a server, 
and stream the access logs to cloudwatch.

Before you run the template, upload the following file to a s3 bucket of
your choice (I use a bucket named gcdataset for testing):

```bash

aws s3 cp access_log.conf s3://gcdataset/access_log.conf
aws s3 cp httpd.conf s3://gcdataset/httpd.conf
aws s3 cp tokio.zip  s3://gcdataset/tokio.zip
```

## PEM & SSH access
This example allow a SSH connection on port 22 to the server. You
need to create a AWS KEY and saved it locally. I usually keep these
keys in `~/pem/`. The one used in the `create_stack.sh` is a personal
pem key I created for the Ireland region.


## Notes about the user data section

Update yum and install some packages we need
```bash
sudo yum -y update
sudo yum install -y awslogs
sudo yum -y install jq
sudo yum install httpd -y
```

Grab the current region this EC2 instance is deployed and store in a variable called $$region
```bash
region=`curl http://169.254.169.254/latest/dynamic/instance-identity/document | jq -r .region`
```

The standard that comes with awslogs uses the us region. We need to replace it with our
region so we can see the logs.
```bash
sudo sed -i "s/region =.*/region = $region /" /etc/awslogs/awscli.conf
```

Next we need to change the format apache uses for the access logs. Remember to 
to copy the httpd.conf into a bucket or your choice. Here `gcdataset` is 
the bucket I use.
```bash
sudo aws s3 cp s3://gcdataset/httpd.conf /etc/httpd/conf/httpd.conf
```

Now we tell awslogd to start monitoring the apache log. As before, remember to 
copy access_log.conf into a s3 bucket of your choice.
```bash
sudo aws s3 cp s3://gcdataset/access_log.conf - >> /etc/awslogs/awslogs.conf
```

We upload the website and unpack it:
```bash
aws s3 cp s3://gcdataset/tokyo.zip .
unzip tokyo.zip -d /var/www/html/
```

We start both awslogd, which will tail access_log and pass it cloudwatch:
```bash
sudo systemctl start awslogsd
```

And we start the apache server:
```
service httpd start
```


## Other Notes


Apache log configuration is usually located in

```
/etc/httpd/conf/httpd.conf
```

Cloudwatch default format is json, in it the Apache world, that is: 
```
 LogFormat "{ \"time\":\"%{%Y-%m-%d}tT%{%T}t.%{msec_frac}tZ\", \"process\":\"%D\",\"filename\":\"%f\", \"remoteIP\":\"%a\", \"host\":\"%V\", \"request\":\"%U\",\"query\":\"%q\",\"method\":\"%m\", \"status\":\"%>s\",\"userAgent\":\"%{User-agent}i\",\"referer\":\"%{Referer}i\"}" cloudwatch
```

The switch the access_log to use this format, we need to change the access log line to:
```
CustomLog "logs/access_log" cloudwatch
```

You can verify the httpd.conf file with
```bash 
httpd -M -f /etc/httpd/conf/httpd.conf
```

The awslogd configuration is located here:
```
cat /etc/awslogs/awscli.conf
```