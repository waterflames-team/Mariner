import importlib
import json
import random
import shutil
import zipfile
import sys
import os

def getRandom(randomlength=16):
    number = "0123456789"
    letters = "abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return ''.join([random.choice(number +letters) for i in range(randomlength)])


def install(args):
    if not os.path.exists("./func_packages/"):
        print("RingRobotX not found.")
        return
    id=getRandom(5)
    print("Extracting skills")
    zip_file = zipfile.ZipFile(args["<skill_file_path>"])
    zip_list = zip_file.namelist()  # 得到压缩包里所有文件

    for f in zip_list:
        zip_file.extract(f, "./temp_"+id)  # 循环解压文件到指定目录

    zip_file.close()  # 关闭文件，必须有，释放内存

    now = json.loads(open("./temp_"+id+"/config.json", "r").read())

    os.rename("./temp_"+id,now["name"])

    shutil.move(now["name"],"./func_packages/"+now["name"])

    print("Executing script")

    sys.path.append(os.getcwd() + "/func_packages/" + now["name"])

    skill_setup=importlib.import_module("setup")


    skill_setup.setup()
    print("Install successful.")