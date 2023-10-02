# automate the task of creating a custom HTTP header response

$hostname = $::hostname

exec {'apt-update':
    command => '/usr/bin/apt-get update',
}
package {'nginx':
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
    match => 'listen 80 default_server',
    line  => "\n\tadd_header X-Served-By \"${hostname}\";",
}

exec { 'restart service':
    command  => 'sudo service nginx restart',
    provider => shell,
}
