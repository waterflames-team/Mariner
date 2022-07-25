# encoding:utf-8
#!/usr/bin/env python3
import os
import zipfile

def build(args):
    if not os.path.exists("./config.json"):
        if os.path.exists("./ring.py"):
            zip_dir="./func_packages/"+args["--skill_name"]
        else:
            zip_dir="./"+args["--skill_name"]
    else:
        zip_dir="./"

    zip = zipfile.ZipFile("./out.mar", 'w', zipfile.ZIP_DEFLATED)
    for path, dirnames, filenames in os.walk(zip_dir):
        this_path = os.path.abspath('.')
        fpath = path.replace(this_path, '')
        for filename in filenames:
            zip.write(os.path.join(path, filename), os.path.join(fpath, filename))
    zip.close()

    print("Build successful! Output file: out.mar")