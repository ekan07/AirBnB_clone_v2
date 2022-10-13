#!/usr/bin/python3
"""A fabric script that generate a .tgz archive from the contents of
the web_static folder ofr your AirBnB clone repo"""
from datetime import datetime
import os.path
from fabric.api import *

env.hosts = ['3.238.206.30', '3.235.172.240']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_pack():
    """Function to compress files"""

    archived_file_path = "versions/web_static_{}.tgz".format(
        datetime.strftime(datetime.now(), "%Y%m%d%H%M%S"))
    if not os.path.exists('versions'):
        os.mkdir('versions')

    # Create TAR file
    t_gzip_archive = local(
        'tar  -cvzf {} {}'.format(archived_file_path, 'web_static'))
    if t_gzip_archive.failed:
        return None

    return t_gzip_archive


def do_deploy(archive_path):
    """Deploy web files to server
    """
    if not (os.path.exists(archive_path)):
        return False
    # remote_archive = /tmp/web_static_20221011142737.tgz
    remote_archive = '/tmp/' + os.path.basename(archive_path)
    # remote_to_xfolder = /data/web_static/releases/web_static_20221011142737/
    remote_to_xfolder = '/data/web_static/releases/'
    remote_to_xfolder += os.path.splitext(os.path.basename(archive_path))[0]
    # upload archive
    # extract archive file to '/data/web_static/releases/<arch. file no ext.>
    put(local_path=archive_path, remote_path=remote_archive)

    # create target dir and uncompress archive and delete .tgz
    r = sudo('mkdir -p {} && tar -xvf {} -C {}'.format(
        remote_to_xfolder, remote_archive, remote_to_xfolder))
    if r.stderr:
        return False
    # remove remote archive file
    r = sudo('rm ' + remote_archive)
    if r.stderr:
        return False
    # delete pre-existing sym link
    sudo('rm -rf /data/web_static/current')
    # re-establish symbolic link
    sudo('ln -s {} {}'.format(
        remote_to_xfolder + '/web_static', '/data/web_static/current'))
    
    # return True on success
    print('New version deployed!')
    return True


def deploy():
    """Create and distributes an archive to your web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False

    return do_deploy(archive_path)
