# encoding:utf-8
#!/usr/bin/env python3
import importlib
import os
import shutil

from docopt import docopt

def uninstall(args):
    if not os.path.exists("./ring.py"):
        print("RingRobotX not found.")
    if not os.path.exists("./func_packages/"+args["skill_name"]+"/main.py"):
        print("Skill not found.")

    skill_setup=importlib.import_module("func_packages."+args["skill_name"]+".setup")

    skill_setup.remove()

    shutil.rmtree("./func_packages/"+args["skill_name"]+"/")
    print("Uninstall successful.")