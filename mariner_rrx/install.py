# encoding:utf-8
#!/usr/bin/env python3
import json
import random
import shutil

import requests
import os
import sys
import zipfile
import importlib

def getRandom(randomlength=16):
    number = "0123456789"
    letters = "abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return ''.join([random.choice(number +letters) for i in range(randomlength)])

def install(args):
    if not os.path.exists("./func_packages/"):
        print("RingRobotX not found.")
        return

    mirror=args["--mirror"]

    #==========================================技能安装区==========================================

    id=getRandom(5)
    print("downloading skills...")
    open("./temp_skill_"+id+".zip","wb").write(requests.get(mirror+"/"+args["<skill_name>"]+".mar").content)# 下载mar文件
    print("Extracting skills")
    zip_file = zipfile.ZipFile("./temp_skill_"+id+".zip")
    zip_list = zip_file.namelist()  # 得到压缩包里所有文件

    for f in zip_list:
        zip_file.extract(f, "./")  # 循环解压文件到指定目录

    zip_file.close()  # 关闭文件，必须有，释放内存

    print("Getting version")
    response = open("./func_packages/" + args["<skill_name>"] + "/config.json","r").read()
    now = json.loads(open("./config/api-version.json", "r").read())

    if float(json.loads(response)["RingRobotX-Ver"]) > float(now["RingRobotX"]):  # 检查技能支持最低版本
        print("This skill is not supported the RingRobotX version")
        print("Removing temporary files")
        os.remove("./temp_skill_" + id + ".zip")
        print("Removing files")
        shutil.rmtree("./func_packages/" + args["<skill_name>"] + "/")
        return

    print("Executing script")

    sys.path.append(os.getcwd() + "/func_packages/" + args["<skill_name>"])

    skill_setup=importlib.import_module("setup")


    skill_setup.setup()

    print("Removing temporary files")
    os.remove("./temp_skill_"+id+".zip")
    print("Install successful.")