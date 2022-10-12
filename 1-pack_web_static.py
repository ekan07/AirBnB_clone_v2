#!/usr/bin/python3
"""Generates a .tgz archive from the
contents of the web_static folder"""
from fabric.operations import local
from datetime import datetime
import os.path


def do_pack():
    """Function to compress files"""

    archived_file_path = "versions/web_static_{}.tgz".format(
        datetime.strftime(datetime.now(), "%Y%m%d%H%M%S"))

    if not os.path.exists('versions'):
        os.mkdir('versions')

    print('Packing web_static to ' + archived_file_path)

    # Create TAR file
    t_gzip_archive = local(
        'tar  -cvzf {} {}'.format(archived_file_path, 'web_static'))
    if t_gzip_archive.failed:
        return None

    file_stats = os.stat(archived_file_path)
    print('web_static packed: {} -> {}Bytes'.format(
        archived_file_path, file_stats.st_size))

    return t_gzip_archive
