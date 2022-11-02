#!/usr/bin/python3
# run on terminal:
# fab -f 2-do_deploy_web_static.py
#  do_deploy:archive_path=versions/web_static_20221011142737.tgz
#  -i my_ssh_private_key -u ubuntu
"""Generates a .tgz archive from the
contents of the web_static folder
Distributes an archive to a web server"""

from datetime import datetime
import os.path
from fabric.api import *

env.hosts = ['3.238.206.30', '3.235.172.240']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """Deploy web files to server
    """
    if not (os.path.exists(archive_path)):
        return False
    # os.path.basename gets the base name of the specified path
    # E.g 'web_static_20221011142737.tgz'
    # remote_archive = /tmp/web_static_20221011142737.tgz
    remote_archive = '/tmp/' + os.path.basename(archive_path)
    # os.path.splitext splits the archive_path into root and ext pair and
    # get the root: '/data/web_static/releases/' + 'web_static_20221011142737'
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
    
    # move contents into remote web_static
    # eg: mv /data/web_static/releases/web_static_20221011142737/web_static/* 
    # r = sudo('mv {}/web_static/* {}/'.format(remote_to_xfolder, remote_to_xfolder))
    # if r.stderr:
    #     print('No move')
    #     return False
    # eg: rm -rf /data/web_static/releases/web_static_20221011142737/web_static
    # r = sudo('rm -rf {}/web_static'.format(remote_to_xfolder))
    # if r.stderr:
    #     print('No remove')
    #     return False

    # delete pre-existing sym link
    sudo('rm -rf /data/web_static/current')
    # re-establish symbolic link
    # ln -s /data/web_static/releases/web_static_20221011142737/web_static /data/web_static/current
    sudo('ln -s {} {}'.format(
        remote_to_xfolder + '/web_static', '/data/web_static/current'))
    
    # return True on success
    print('New version deployed!')
    return True
