# -*- coding: utf-8 -*-

import os
import sys
import json


project_name = sys.argv[1:][0]
base_dir = sys.argv[1:][1]
noconf = sys.argv[1:][2]

filepath = base_dir + '/centrifugo/config.json'
filepathtmp = base_dir + '/tmp.py'
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


if noconf != "noconf":
    project_dir = base_dir + "/" + project_name
    filepath = project_dir + '/settings.py'
    f = open(filepath, "a")
    f.write("\n" + extralines + "\n")
    f.close()
