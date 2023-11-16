# puppet file that changes file discriptors for user holberton
exec {
    'replace the hard limit':
    command => 'sed -i "s/holberton hard nofile 5/holberton hard nofile 1500/" /etc/security/limits.conf',
    path    => ['/bin/','/usr/bin/']
}

exec {
    'replace the soft limit':
    command => 'sed -i "s/holberton soft nofile 4/holberton hard nofile 1000/" /etc/security/limits.conf',
    path    => ['/bin/','/usr/bin/']
}