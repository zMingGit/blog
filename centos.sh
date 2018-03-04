sudo yum update

sudo yum install epel-release 

sudo yum install git   nginx python-pip yum-utils man-pages uwsgi

sudo yum -y groupinstall development



sudo yum -y install https://centos7.iuscommunity.org/ius-release.rpm

sudo yum -y install python36u

ln -s /usr/bin/python3.6 /usr/bin/python3



systemctl enable firewalld
systemctl start firewalld

firewall-cmd --permanent --zone=public --add-port=80/tcp
firewall-cmd --permanent --zone=public --add-port=80/udp

firewall-cmd --reload



yum install python36u-devel.x86_64

cd /root

mkdir -p /root/blog_static

mkdir -p /etc/nginx/blog

cat > /etc/nginx/blog/blog.conf << 'EOF'
upstream django {

    # server unix:///path/to/your/mysite/mysite.sock; # for a file socket
    server 127.0.0.1:8000; # for a web port socket (we'll use this first)
}

# configuration of the server
server {
    # the port your site will be served on
    listen      80 default_server;
    # the domain name it will serve for
    server_name www.zming.info; # substitute your machine's IP address or FQDN
    charset     utf-8;
    
    # max upload size
    client_max_body_size 75M;   # adjust to taste
    
    # Django media
    location /media  {
        alias /root/blog_media;  # your Django project's media files - amend as required
    }
    
    location /static {
        alias /root/blog_static; # your Django project's static files - amend as required
    }
    
    # Finally, send all non-media requests to the Django server.
    location / {
        uwsgi_pass  django;
        include     /etc/nginx/blog/uwsgi_params; # the uwsgi_params file you installed
    }
}
EOF

cat > /etc/nginx/blog/uwsgi_params << 'EOF'
uwsgi_param  QUERY_STRING       $query_string;
uwsgi_param  REQUEST_METHOD     $request_method;
uwsgi_param  CONTENT_TYPE       $content_type;
uwsgi_param  CONTENT_LENGTH     $content_length;

uwsgi_param  REQUEST_URI        $request_uri;
uwsgi_param  PATH_INFO          $document_uri;
uwsgi_param  DOCUMENT_ROOT      $document_root;
uwsgi_param  SERVER_PROTOCOL    $server_protocol;
uwsgi_param  REQUEST_SCHEME     $scheme;
uwsgi_param  HTTPS              $https if_not_empty;

uwsgi_param  REMOTE_ADDR        $remote_addr;
uwsgi_param  REMOTE_PORT        $remote_port;
uwsgi_param  SERVER_PORT        $server_port;
uwsgi_param  SERVER_NAME        $server_name;" > 
EOF

cat > /etc/nginx/nginx.cnf << 'EOF'
user root;
worker_processes auto;
error_log /var/log/nginx/error.log;
pid /run/nginx.pid;

include /usr/share/nginx/modules/*.conf;

events {
    worker_connections 1024;
}

http {
    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';
    
    access_log  /var/log/nginx/access.log  main;
    
    sendfile            on;
    tcp_nopush          on;
    tcp_nodelay         on;
    keepalive_timeout   65;
    types_hash_max_size 2048;
    
    include             /etc/nginx/mime.types;
    default_type        application/octet-stream;
    
    include /etc/nginx/con.d/*.conf;
    include /etc/nginx/blog/*.conf;

}
EOF

git clone https://github.com/zMingGit/Blog.git

cd Blog

python3 -m pip install uwsgi

python3 -m pip install -r requirements.txt 

python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py collectstatic

cd blog

uwsgi --ini uwsgi.ini

systemctl restart nginx