# encoding:utf-8
#!/usr/bin/env python3
import importlib
import os
import shutil
import sys


def uninstall(args):
    if not os.path.exists("./func_packages/"):
        print("RingRobotX not found.")
        return
    if not os.path.exists("./func_packages/"+args["<skill_name>"]+"/main.py"):
        print("Skill not found.")
        return
    print("Executing script")

    sys.path.append(os.getcwd() + "/func_packages/" + args["<skill_name>"])

    skill_setup=importlib.import_module("setup")

    skill_setup.remove()

    print("Removing files")
    shutil.rmtree("./func_packages/"+args["<skill_name>"]+"/")
    print("Uninstall successful.")