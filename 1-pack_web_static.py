#!/usr/bin/python3
# Creating an archive using Fabric

from fabric.api import local
from datetime import datetime


def do_pack():
    """Create a tgz archive from the contents of the web_static folder."""
    try:
        now = datetime.now()
        archive_file = "web_static_{}{}{}{}{}{}.tgz".format(
            now.year, now.month, now.day, now.hour, now.minute, now.second
        )

        local("mkdir -p versions")

        local("tar -czvf versions/{} web_static".format(archive_file))

        return "versions/{}".format(archive_file)
    except Exception:
        return None
