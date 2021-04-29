#!/usr/bin/python3
"""
    Compress web_static to .tgz file
"""

from fabric.api import *
from datetime import datetime


def do_pack():
    """compress web_static"""

    try:
        local("mkdir -p versions")
        time_stamp = datetime.now().strftime('%Y%m%d%H%M%S')
        path = "versions/web_static_{}.tgz".format(time_stamp)
        local("tar -cvzf {} web_static".format(path))
        return path
    except:
        return None
