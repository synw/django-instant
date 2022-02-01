import json
import os
import platform
import subprocess

from django.core.management.base import BaseCommand

from instant.init import generate_settings_from_conf


class Command(BaseCommand):
    help = (
        "Install the Centrifugo websockets server for Linux and Darwin"
        "and generate the Django settings"
    )

    def handle(self, *args, **options):
        centrifugo_version = "3.1.1"
        run_on = str(platform.system()).lower()
        suffix = "_linux_386"
        if run_on == "darwin":
            suffix = "_darwin_amd64"
        suffix_file = suffix + ".tar.gz"
        fetch_url = (
            "https://github.com/centrifugal/centrifugo/releases/download/v"
            + centrifugo_version
            + "/centrifugo_"
            + centrifugo_version
            + suffix_file
        )
        basepath = os.getcwd()
        subprocess.call(["mkdir", "centrifugo"])
        os.chdir(basepath + "/centrifugo")
        subprocess.call(["wget", fetch_url])
        name = "centrifugo_" + centrifugo_version + suffix
        subprocess.call(["tar", "-xzf", name + ".tar.gz"])
        subprocess.call(["rm", "-f", name + ".tar.gz"])
        subprocess.call(["chmod", "a+x", "centrifugo"])
        subprocess.call(["./centrifugo", "genconfig"])
        # set allowed origins in Centrifugo config
        filepath = basepath + "/centrifugo/config.json"
        with open(filepath, "r+") as f:
            content = f.read()
            conf = json.loads(content)
            conf["allowed_origins"] = ["*"]
            output = json.dumps(conf, indent=4)
            f.seek(0)
            f.write(output)
            f.truncate()
            f.close()
        # generate settings
        buffer = generate_settings_from_conf(conf)
        # print conf
        print("\nAppend this to your Django settings:\n")
        for line in buffer:
            print(line)
        print("\n")
        print(
            "The Centrifugo websockets server is installed. Run it with python3"
            "manage.py runws"
        )
