# encoding:utf-8
#!/usr/bin/env python3
import platform
from docopt import docopt
import os

def get(args):
    if platform.system() == 'Windows':
        print("This script is not available for this system (Linux Only).")
    else:
        script_url = args["--script-url"]
        print("Executing script: %s" % script_url)
        os.system("wget -O install.sh " + script_url + " && sudo bash install.sh")