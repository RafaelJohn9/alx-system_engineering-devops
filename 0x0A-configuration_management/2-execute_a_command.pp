# Define a custom Puppet resource named 'kill_process'

exec { 'pkill':
  command     => 'pkill -f killmenow',
  provider    => 'shell',
}
