from __future__ import print_function
import os
import subprocess
import json
from django.conf import settings
from django.core.management.base import BaseCommand
import platform

class Command(BaseCommand):
    help = 'Install the Centrifugo websockets server for Linux'


    def __init__(self, *args, **options):
        self.centrifugo_version = "1.8.0"
        self.centrifugo_prefix = "centrifugo-"
        self.centrifugo_file_ext = ".zip"

        self.run_on = str(platform.system()).lower()

        if self.run_on == "linux":
            self.file_suffix = "-linux_386"

        if self.run_on == "darwin":
            self.file_suffix = "-darwin_amd64"

        if self.run_on == "Windows":
            print("Not supported")
            exit()

    def handle(self, *args, **options):

        fetch_url = "https://github.com/centrifugal/centrifugo/releases/download/v" + \
            self.centrifugo_version + "/" + self.centrifugo_prefix + \
            self.centrifugo_version + self.file_suffix + self.centrifugo_file_ext
        subprocess.call(["wget", fetch_url])
        dirname = self.centrifugo_prefix + self.centrifugo_version + self.file_suffix

        if "zip" in self.centrifugo_file_ext:
            subprocess.call(["unzip", dirname +  self.centrifugo_file_ext])
            subprocess.call(["mv", dirname, "centrifugo"])
        else:
            try:
                subprocess.call(["mkdir", "-p", "centrifugo"])
                subprocess.call(
                    ["tar", "xfvz", dirname + self.centrifugo_file_ext,
                    "-C", "centrifugo"]
                    )
            except Exception as e:
                print(str(e))
                exit()


        subprocess.call(["rm", "-f", dirname +  self.centrifugo_file_ext])
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
        extralines = ""
        project_dir = basepath + "/" + project_name
        filepath = project_dir + '/settings.py'


        content = open(filepath, 'r').read()

        if "SITE_SLUG" not in content:
            extralines += 'SITE_SLUG = "' + project_name + '"\n'

        if "SITE_NAME" not in content:
            extralines += 'SITE_NAME = SITE_SLUG\n'

        if "CENTRIFUGO_SECRET_KEY" not in content:
            extralines += 'CENTRIFUGO_SECRET_KEY = "' + key + '"\n'

        if "CENTRIFUGO_HOST" not in content:
            extralines += 'CENTRIFUGO_HOST = "http://localhost"\n'

        if "CENTRIFUGO_PORT" not in content:
            extralines += "CENTRIFUGO_PORT = 8001\n"

        if "CORS_ORIGIN_WHITELIST" not in content:
            extralines += "CORS_ORIGIN_WHITELIST = ('localhost:8001',)"


        if len(extralines)>0:
            f = open(filepath, "a")
            f.write("\n" + extralines + "\n")
            f.close()

        print("The Centrifugo websockets server is installed. Run it with python3 manage.py runws")
        return
