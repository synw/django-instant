from __future__ import print_function
from django.core.management.base import BaseCommand
import os
import subprocess


class Command(BaseCommand):
    help = 'Run the Centrifugo websockets server'

    def handle(self, *args, **options):
        basepath = os.getcwd()
        c = basepath + "/centrifugo/centrifugo"
        cmd = [
            c,
            "--config", "config.json"
        ]
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        for line in p.stdout:
            msg = str(line).replace("b'", "")
            msg = msg[0:-3]
            print(msg)
        p.wait()
        return
