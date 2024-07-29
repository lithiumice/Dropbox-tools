from setuptools import setup, find_packages

import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="Dropbox-Tools",
    version="v0.0.1",
    license="WTFPL",
    author="Jensin",
    description="Dropbox utilities with offical Dropbox API",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "click",
        "tqdm",
        "dropbox",
    ],
    entry_points="""
        [console_scripts]
        dbx=dbx.cli:cli
    """
)