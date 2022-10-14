#!/usr/bin/python3
"""A fabric script that generate a .tgz archive from the contents of
the web_static folder ofr your AirBnB clone repo"""
import os
from fabric.api import *

env.hosts = ['3.238.206.30', '3.235.172.240']
# env.user = 'ubuntu'
# env.key_filename = '~/.ssh/id_rsa'


def do_clean(number=0):
    """Deletes out-of-date archives, using the function do_clean"""

    # local_files to delete
    number = int(number)
    if number in (0, 1):
        number = 1
    # cleaup local filers
    local_files = local("ls -1t versions", capture=True)
    file_names = local_files.split("\n")
    for i in file_names[:number]:
        local("rm versions/{}".format(i))
    # clean update remote server
    # remote_pathnames = remote_paths.split("\n")
    with cd("/data/web_static/releases"):
        remote_paths = run("ls -1t").split("\n")
        remote_paths = [f for f in remote_paths if "web_static_" in f]
        for i in remote_paths[-number:]:
            sudo("rm -r {}".format(i))
