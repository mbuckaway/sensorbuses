#!/usr/bin/env python3
from setuptools import setup

setup(
    name = 'sensorbuses',
    version = '1.0',
    description = 'Installs modules and activates drivers/devices in i2c, spi, and 1 wire sensor buses using kernel drivers',
    author='Mark Buckaway',
    author_email='mark@buckaway.ca',
    url='http://github.com/mbuckaway/sensorbusess',
    license = 'MIT',
    packages = ['sensorbuses'],
    entry_points = {'console_scripts': ['sensorbuses = sensorbuses.py',],},
)
