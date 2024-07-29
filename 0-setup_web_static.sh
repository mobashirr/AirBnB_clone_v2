#!/usr/bin/env bash

# Exit on any error
set -e

# Function to install Nginx if it is not already installed
install_nginx() {
    if ! command -v nginx > /dev/null; then
        sudo apt update
        sudo apt install -y nginx
    fi
}

# Function to create a directory if it doesn't already exist
create_dir_if_not_exists() {
    if [ ! -d "$1" ]; then
        sudo mkdir -p "$1"
    fi
}

# Function to create a fake HTML file for testing
create_fake_html() {
    sudo tee /data/web_static/releases/test/index.html > /dev/null << EOF
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
EOF
}

# Function to set up symbolic link
setup_symbolic_link() {
    if [ -L /data/web_static/current ]; then
        sudo rm /data/web_static/current
    fi
    sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
}

# Function to set ownership of /data/ to ubuntu user and group
set_ownership() {
    sudo chown -R ubuntu:ubuntu /data/
}

# Function to update Nginx configuration
update_nginx_config() {
    sudo tee /etc/nginx/sites-available/default > /dev/null << EOF
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location / {
        try_files \$uri \$uri/ =404;
    }

    location /hbnb_static {
        alias /data/web_static/current/;
    }
}
EOF
    sudo systemctl restart nginx
}

# Main script execution
install_nginx
create_dir_if_not_exists "/data/"
create_dir_if_not_exists "/data/web_static/"
create_dir_if_not_exists "/data/web_static/releases/"
create_dir_if_not_exists "/data/web_static/shared/"
create_dir_if_not_exists "/data/web_static/releases/test/"
create_fake_html
setup_symbolic_link
set_ownership
update_nginx_config

echo "Web server setup complete"
