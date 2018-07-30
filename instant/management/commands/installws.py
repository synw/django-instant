from __future__ import print_function
import os
import subprocess
import json
from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Install the Centrifugo websockets server for Linux'

    def handle(self, *args, **options):
        centrifugo_version = "1.8.0"
        fetch_url = "https://github.com/centrifugal/centrifugo/releases/download/v" + \
            centrifugo_version + "/centrifugo-" + centrifugo_version + "-linux-386.zip"
        subprocess.call(["wget", fetch_url])
        dirname = "centrifugo-" + centrifugo_version + "-linux-386"
        subprocess.call(["unzip", dirname + ".zip"])
        subprocess.call(["mv", dirname, "centrifugo"])
        subprocess.call(["rm", "-f", dirname + ".zip"])
        subprocess.call(["centrifugo/centrifugo", "genconfig"])
        subprocess.call(["mv", "config.json", "centrifugo"])
        # generate settings
        print("Updating settings")
        basepath = os.getcwd()
        project_name = settings.BASE_DIR.split("/")[-1:][0]
        filepath = basepath + '/centrifugo/config.json'
        filepathtmp = basepath + '/tmp.py'
        with open(filepath) as f:
            content = f.read()
        f = open(filepath, "r")
        f2 = open(filepathtmp, "w+")
        conf = json.loads(content)
        conf["anonymous"] = "true"
        key = conf["secret"]
        res = json.dumps(conf, indent=4).replace('"true"', 'true')
        f2.write(res)
        f2.close()
        os.remove(filepath)
        os.rename(filepathtmp, filepath)
        # settings.py
        extralines = 'SITE_SLUG = "' + project_name + '"\n'
        extralines = extralines + 'SITE_NAME = SITE_SLUG\n'
        extralines = extralines + 'CENTRIFUGO_SECRET_KEY = "' + key + '"\n'
        extralines = extralines + 'CENTRIFUGO_HOST = "http://localhost"\n'
        extralines = extralines + "CENTRIFUGO_PORT = 8001\n"
        project_dir = basepath + "/" + project_name
        filepath = project_dir + '/settings.py'
        f = open(filepath, "a")
        f.write("\n" + extralines + "\n")
        f.close()
        print("The Centrifugo websockets server is installed. Run it with python3 manage.py runws")
        return
