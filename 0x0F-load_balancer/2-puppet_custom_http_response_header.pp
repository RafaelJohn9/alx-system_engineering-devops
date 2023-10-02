# nginx configuration file

exec { 'apt_update':
  command     => 'sudo apt-get -y update',
  provider => shell,
}

-> exec { 'nginx_install':
  command => 'sudo apt-get -y install nginx',
  provider => shell,
}

-> exec { 'replace':
  command => 'sudo sed -i "/listen 80 default_server;/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-enabled/default',
  provider => shell,
}

-> exec { 'restart':
  command => 'sudo service nginx restart',
  provider => shell,
}
