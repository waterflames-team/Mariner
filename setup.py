# encoding:utf-8
from mariner_rrx import __version__
from setuptools import find_packages
from distutils.core import setup
import os
pathroot = os.path.split(os.path.realpath(__file__))[0]
setup(
    name="mariner_rrx",
    version=__version__,
    description="A package manager for RingRobotX",
    author="WaterFlames",
    packages=find_packages(),
    platforms="any",
    install_requires=[
        "requests",
        "docopt>=0.6.2"
    ],
    scripts=[pathroot+'/mariner_rrx/mar.py'],
    entry_points={
        'console_scripts': [
            'marx = mariner_rrx.mar:run',
        ],
    },
)