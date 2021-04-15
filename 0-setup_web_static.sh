#!/usr/bin/env bash
# Sets up web server(s) for the web static deployment

if [ ! -x "$(command -v nginx)" ]
then
	apt-get update
	apt-get -y install nginx
fi

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

echo "Hello World!!!" > /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu:ubuntu /data/

path="/data/web_static/current/"
route="location /hbnb_static/ {\n\t\talias $path;\n\t}"
match="server_name _;"
sed -i "s|$match|$match\n\n\t$route|" /etc/nginx/sites-available/default
