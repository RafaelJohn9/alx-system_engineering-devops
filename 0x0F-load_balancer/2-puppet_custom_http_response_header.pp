# configuration of nginx

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
  ensure  => 'present',
  path    => '/etc/nginx/sites-available/default',
  content => "# Your entire file content here, including any existing content\n add_header X-Served-By \"${hostname}\";\n",
  require => Package['nginx'],  # Ensure nginx package is installed first
  notify  => Exec['restart service'],  # Trigger restart if the file changes
}

exec { 'restart service':
  command  => 'sudo service nginx restart',
  provider => shell,
}
