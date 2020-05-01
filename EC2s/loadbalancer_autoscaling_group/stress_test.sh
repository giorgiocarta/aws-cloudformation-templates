# requires httpd-tools



#$name="ab"

#[ `which $name` ] $$ echo "$name : installed" || echo "install httpd-tools"



ab -n 4000000 -c10 http://[public_dns_of_your_ELB]/