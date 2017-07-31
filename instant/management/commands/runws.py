from __future__ import print_function
from django.core.management.base import BaseCommand
import os
import subprocess
from instant.conf import CENTRIFUGO_PORT


class Command(BaseCommand):
    help = 'Run the Centrifugo websockets server'

    def handle(self, *args, **options):
        basepath = os.getcwd()
        c = basepath + "/centrifugo/centrifugo"
        conf = basepath + "/centrifugo/config.json"
        cmd = [
            c,
            "--config", conf,
            "--port", str(CENTRIFUGO_PORT)
        ]
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        for line in p.stdout:
            msg = str(line).replace("b'", "")
            msg = msg[0:-3]
            print(msg)
        p.wait()
        return
