#!/usr/bin/python3
"""
    Preps and Deploys web_static to web1 and web2
"""

from fabric.api import *
from datetime import datetime

web1 = '35.231.129.240'
web2 = '35.196.6.217'
env.hosts = [web1, web2]


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


def do_deploy(archive_path):
    """Deploy to servers"""

    try:
        run('mkdir -p /tmp/versions/')

        zip_path = '/tmp/{}'.format(archive_path)

        put(archive_path, zip_path)

        zip_file = archive_path.split('/')[1]
        unzip_path = '/data/web_static/releases/{}'.format(zip_file[:-4])
        current_path = '/data/web_static/current'

        run('mkdir -p {}/'.format(unzip_path))
        run('tar -xzf {} -C {}/'.format(zip_path, unzip_path))
        run('rm {}'.format(zip_path))
        run('mv {}/web_static/* {}/'.format(unzip_path, unzip_path))
        run('rm -rf {}/web_static'.format(unzip_path))
        run('rm -rf {}'.format(current_path))
        run('ln -s {}/ {}'.format(unzip_path, current_path))
        return True
    except:
        return False
