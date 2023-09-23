# Define a custom Puppet resource named 'kill_process'

exec { 'killmenow':
  command     => 'pkill -f killmenow',
  provider    => 'shell',
}
