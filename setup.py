"""The python wrapper for X8 option API package setup."""
from setuptools import (setup, find_packages)
from x8api.version_control import api_version

setup(
    name="x8api",
    version=api_version,
    packages=find_packages(),
    install_requires=["pylint", "requests", "websocket-client==0.56"],
    include_package_data=True,
    description="Best X8 option API for python",
    long_description="Best X8 option API for python",
    url="https://github.com/hnomkeng/x8api",
    author="Rafael Faria",
    zip_safe=False
)
