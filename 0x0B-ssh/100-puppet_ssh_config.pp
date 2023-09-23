# Define SSH client configuration file path
$ssh_config_file = '/etc/ssh/ssh_config'

# Ensure the SSH client configuration uses the private key ~/.ssh/school
file_line { 'Set SSH Identity File':
  path   => $ssh_config_file,
  line   => '    IdentityFile ~/.ssh/school',
  match  => '^ *IdentityFile.*$',
  ensure => present,
}

# Ensure the SSH client configuration refuses password authentication
file_line { 'Disable Password Authentication':
  path   => $ssh_config_file,
  line   => '    PasswordAuthentication no',
  match  => '^ *PasswordAuthentication.*$',
  ensure => present,
}
