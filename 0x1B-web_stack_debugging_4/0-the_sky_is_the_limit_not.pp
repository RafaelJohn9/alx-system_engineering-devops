# Puppet script that changes file descipters to 4096
exec { '/usr/bin/env sed -i s/15/4096/ /etc/default/nginx': }
-> exec { '/usr/bin/env service nginx restart': }
