`install some package`

```
yum install libxml2-devel
yum install gcc
yum install python-devel
yum install nginx


pip install uwsgi
pip install -r requirements.txt
```

`reinstall package if error for virtual`

```
pip install --upgrade --force-reinstall <package>
```

`open firewall for test`


```
firewall-cmd --permanent --zone=public --add-port=9090/tcp
firewall-cmd --permanent --zone=public --add-port=9090/udp

firewall-cmd --reload
```



`uwsgi.ini`

```
[uwsgi]
socket = 0.0.0.0:9090
#http = 0.0.0.0:9090 # use for test

chdir=/root/blogDev/Blog/
wsgi-file=/root/blogDev/Blog/blog/wsgi.py

master = true
workers = 2
pidfile = /root/uwsgi9090.pid
daemonize = /root/uwsgi9090.log
```



`nginx.conf`

```
user root; //make sure has permission to access static file or others



http {
    ...
    server {
        listen       80 default_server;
        listen       [::]:80 default_server;
        server_name  localhost;
        root         /usr/share/nginx/html;

        # Load configuration files for the default server block.
        include /etc/nginx/default.d/*.conf;

        location / {
            include uwsgi_params;
            uwsgi_pass 0.0.0.0:9090;
            uwsgi_param UWSGI_CHDIR /root/blogDev/Blog;
            uwsgi_param UWSGI_SCRIPT blog.wsgi;
            client_max_body_size 35m;
        }

        location /static {
            alias /root/blog_static;
        }

}
```


`commond`

```
uwsgi --ini uwsgi.ini
uwsgi --stop uwsgi.pid


# if install for yum
service nginx start
service nginx stop
```
