#!/usr/bin/python3

"""a module that istributes an archive to your web servers,
using the function do_deploy
"""


from fabric.api import local, put, run, env
from datetime import datetime
from os.path import exists, isdir
env.hosts = ['54.226.6.57', '54.89.26.215']


def do_pack():
    """create a .tgz archive from the contents of the web_static folder"""
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_file = "versions/web_static_{}.tgz".format(date)

    try:
        if isdir("versions") is False:
            local("mkdir versions")
        local("tar -cvzf {} web_static".format(archive_file))
        return archive_file
    except Exception as e:
        return None


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        folder = archive_path.split("/")[-1]
        file_name = folder.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, file_name))
        run('tar -xzf /tmp/{} -C {}{}/'.format(folder, path, file_name))
        run('rm /tmp/{}'.format(folder))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, file_name))
        run('rm -rf {}{}/web_static'.format(path, file_name))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, file_name))
        return True
    except:
        return False


def deploy():
    """creates & distributes an archive to servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
