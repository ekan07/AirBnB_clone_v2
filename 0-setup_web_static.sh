#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static
if [[ ! -f "/etc/init.d/nginx" ]]; then
        apt -y update
        apt install -y nginx
fi
# create deployment folders
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
# create fake html file
echo "<html>
  <head>
  </head>
  <body>
    ALX School
  </body>
</html>" > /data/web_static/releases/test/index.html
# re-create symbol link
ln -sf /data/web_static/releases/test /data/web_static/current
# update /data ownership
chown -R ubuntu:ubuntu /data
# update nginx configuration
sed -i '53i \\tlocation \/hbnb_static {\n\t\t alias /data/web_static/current;\n\t}' /etc/nginx/sites-available/default
service nginx restart
