yum -y install yum-utils
yum-config-manager --enable rhui-REGION-rhel-server-extras rhui-REGION-rhel-server-optional
sudo yum install certbot-nginx
# need set 443 to default_server.
sudo certbot --nginx
sudo certbot renew --dry-run