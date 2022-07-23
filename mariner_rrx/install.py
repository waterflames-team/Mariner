# encoding:utf-8
#!/usr/bin/env python3
import json
import random
import requests
import os
import zipfile
import importlib

def getRandom(randomlength=16):
    number = "0123456789"
    letters = "abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return ''.join([random.choice(number +letters) for i in range(randomlength)])

def install(args):
    if not os.path.exists("./ring.py"):
        print("RingRobotX not found.")

    mirror=args["--mirror"]
    response = requests.get(mirror+"/"+args["skill_name"]+"/index.json")
    now=json.loads(open("./config/api-version.json","r").read())

    if float(json.loads(response.text)["RingRobotX-Ver"]) < float(now["RingRobotX"]):#检查技能支持最低版本
        print("This skill is not supported the RingRobotX version")
        return

    #==========================================技能安装区==========================================

    id=getRandom(5)
    open("./temp_skill_"+id+".zip","wb").write(requests.get(mirror+"/"+args["skill_name"]+"/code.mar").content)# 下载mar文件
    zip_file = zipfile.ZipFile("./temp_skill_"+id+".zip")
    zip_list = zip_file.namelist()  # 得到压缩包里所有文件

    for f in zip_list:
        zip_file.extract(f, "./func_packages/"+args["skill_name"])  # 循环解压文件到指定目录

    zip_file.close()  # 关闭文件，必须有，释放内存

    skill_setup=importlib.import_module("func_packages."+args["skill_name"]+".setup")

    skill_setup.setup()

    os.remove("./temp_skill_"+id+".zip")
    print("Install successful.")