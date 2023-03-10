# encoding:utf-8
#!/usr/bin/env python3
import os
import zipfile

def build(args):
    zip_dir="./func_packages/"+args["<skill_name>"]

    zip = zipfile.ZipFile("./code.mar", 'w', zipfile.ZIP_DEFLATED)
    for path, dirnames, filenames in os.walk(zip_dir):
        this_path = os.path.abspath('.')
        fpath = path.replace(this_path, '')
        for filename in filenames:
            zip.write(os.path.join(path, filename), os.path.join(fpath, filename))
    zip.close()

    print("Build successful! Output file: code.mar")