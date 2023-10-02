# configuration of nginx

$hostname = $::hostname

exec { 'apt_update':
  command     => 'apt-get -y update',
  path        => '/usr/bin:/bin',
  refreshonly => true,
}

package { 'nginx':
  ensure => 'installed',
}

service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx'],
}

file { '/etc/nginx/sites-available/default':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  match  => 'listen 80 default_server',
  line   => "\n\tadd_header X-Served-By \"${hostname}\";",
}

exec { 'restart service'
  command  => 'sudo service nginx restart',
  provider => shell,
}
