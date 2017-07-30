from __future__ import print_function
from django.core.management.base import BaseCommand
import os
import subprocess
from django.conf import settings


class Command(BaseCommand):
    help = 'Install the Centrifugo websockets server for Linux'

    def handle(self, *args, **options):
        basepath = os.getcwd()
        path = os.path.abspath(__file__)
        modpath = os.path.dirname(path)
        project_name = settings.BASE_DIR.split("/")[-1:][0]
        script = modpath + "/install.sh"
        subprocess.call([script, project_name, basepath, modpath])
        return
