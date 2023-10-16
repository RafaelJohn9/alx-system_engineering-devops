#!/usr/bin/python3

"""
it configures server 2 and the loadbalancer with a firewall(ufw)
"""

from fabric.api import *

env.hosts = ['100.25.109.79', '18.209.152.192']

def firewall():
    """
    configures in the firewall
    """
    try:
        run("sudo apt-get -y install ufw")
        run("sudo ufw allow 22/tcp")
        run("sudo ufw allow 443/tcp")
        run("sudo ufw allow 80/tcp")
        run("sudo ufw enable")
        return True
    except Exception:
        return False
