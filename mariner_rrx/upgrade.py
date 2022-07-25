# encoding:utf-8
#!/usr/bin/env python3
import importlib
import json
import os
import sys
import zipfile

import requests
from mariner_rrx.install import getRandom


def upgrade(args):
    if not os.path.exists("./func_packages/"):
        print("RingRobotX not found.")
        return
    mirror = args["--mirror"]
    print("Getting remote version")
    response = requests.get(mirror + "/" + args["<skill_name>"] + "/index.json")
    now = json.loads(open("./config/api-version.json", "r").read())

    if float(json.loads(response.text)["RingRobotX-Ver"]) > float(now["RingRobotX"]):  # 检查技能支持最低版本
        print("This skill is not supported the RingRobotX version")
        return

    # ==========================================技能安装区==========================================

    id = getRandom(5)
    print("downloading skills...")
    open("./temp_skill_" + id + ".zip", "wb").write(
        requests.get(mirror + "/" + args["<skill_name>"] + "/code.mar").content)  # 下载mar文件
    print("Extracting skills")
    zip_file = zipfile.ZipFile("./temp_skill_" + id + ".zip")
    zip_list = zip_file.namelist()  # 得到压缩包里所有文件

    for f in zip_list:
        zip_file.extract(f, "./func_packages/" + args["<skill_name>"])  # 循环解压文件到指定目录

    zip_file.close()  # 关闭文件，必须有，释放内存
    print("Executing script")

    sys.path.append(os.getcwd() + "/func_packages/" + args["<skill_name>"])

    skill_setup = importlib.import_module("setup")

    skill_setup.upgrade()
    print("Removing temporary files")
    os.remove("./temp_skill_" + id + ".zip")
    print("Upgrade %s successful.", args["<skill_name>"])

def upgrade_all(args):
    mirror = args["--mirror"]


    path = os.path.dirname(os.getcwd()+"/func_packages/")
    mypath = os.listdir(r'' + path)
    for i in mypath:
        if os.path.isdir(path + "/" + i) and i != "__pycache__":
            jsonvero=json.loads(open("./func_packages/"+i+"/config.json", "r").read())
            print("checking for ".join(jsonvero["name"]))
            response = requests.get(mirror + "/" + jsonvero["name"] + "/index.json")

            if float(json.loads(response.text)["version"]) > float(jsonvero["version"]):
                print("Upgrade: %s",jsonvero["name"])
                upgrade({"<skill_name>":i,"--mirror":mirror})


