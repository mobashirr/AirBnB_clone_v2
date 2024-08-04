#!/usr/bin/python3
"""a module that generates a .tgz archives from the web_statics folder"""
import os.path
from fabric.api import local
from datetime import datetime


def do_pack():
    """create a .tgz archive from the contents of the web_static folder"""
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_file = "versions/web_static_{}.tgz".format(date)
    try:
        if os.path.isdir("versions") is False:
            local("mkdir versions")
        local("tar -cvzf {} web_static".format(archive_file))
        return archive_file
    except Exception as e:
        return None

pip3 uninstall Fabric
sudo apt-get install libffi-dev
sudo apt-get install libssl-dev
sudo apt-get install build-essential
sudo apt-get install python3.4-dev
sudo apt-get install libpython3-dev
pip3 install pyparsing
pip3 install appdirs
pip3 install setuptools==40.1.0
pip3 install cryptography==2.8
pip3 install bcrypt==3.1.7
pip3 install PyNaCl==1.3.0
pip3 install Fabric3==1.14.post1