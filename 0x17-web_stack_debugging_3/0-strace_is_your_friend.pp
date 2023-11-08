# Puppet manifest to fix a bug in wp-setings.php

exec { 'fix the type phpp->php':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/bin'
}