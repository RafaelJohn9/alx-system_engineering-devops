#!/usr/bin/python3

"""
it configures server 2 and the loadbalancer with a firewall(ufw)
"""

from fabric.api import *

env.hosts = ['18.206.207.45', '100.25.109.79', '18.209.152.192']

def rerouting():
    """
    configures in the firewall
    """
    try:
        run('echo -e "*nat\n:PREROUTING ACCEPT [0:0]\n-A PREROUTING -p tcp --dport 8080 -j REDIRECT --to-port 80\nCOMMIT" | sudo tee -a /etc/ufw/before.rules')
        run("sudo ufw reload")
        return True
    except Exception:
        return False
