# encoding:utf-8
#!/usr/bin/env python3
""" Mariner-RRX -- A package manager for RingRobotX
Usage:
    marx get-rrx [--script-url=<git_url>]
    marx install <skill_name> [--mirror=<mirror_url>]
    marx uninstall <skill_name>
    marx build [skill_name]
    marx upgrade-all [--mirror=<mirror_url>]
    marx upgrade <skill_name> [--mirror=<mirror_url>]
    marx -h | --help
    marx -v | --version


Options:
    -h --help     Show Help doc.
    -v --version     Show Version.
    --mirror=<mirror_url>     Set a mirror for skills. [default: https://gitee.com/waterflames-team/mariner/raw/master/skills/]
    --script-url=<git_url>     Set a custom-script for RingRobotX. [default: https://gitee.com/waterflames-team/ring-robot-x/raw/master/install.sh]
"""
import random
__version__ = "v1.1.1"
# 版本号改我！！！
import mariner_rrx.build
import mariner_rrx.get
import mariner_rrx.install
import mariner_rrx.uninstall
import mariner_rrx.upgrade
from docopt import docopt


def run():
    args = docopt(__doc__, version=__version__)
    if args.get("get-rrx"):
        mariner_rrx.get.get(args)
    elif args.get("install"):
        mariner_rrx.install.install(args)
    elif args.get("uninstall"):
        mariner_rrx.uninstall.uninstall(args)
    elif args.get("build"):
        mariner_rrx.build.build(args)
    elif args.get("upgrade"):
        mariner_rrx.upgrade.upgrade(args)
    elif args.get("upgrade-all"):
        mariner_rrx.upgrade.upgrade_all(args)
    else:
        print("Command not found.")


if __name__ == "__main__":
    run()
