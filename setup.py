#!/usr/bin/env python
# encoding: utf-8

from setuptools import setup, find_packages

setup(
    name='zeppelin-converter',
    author='Wendy Fu',
    author_email='wfu@mozilla.com',
    description='Converts Zeppelin JSON files to Markdown',
    keywords='zeppelin converter markdown',
    url='https://github.com/comloo/python-zeppelin',
    entry_points={
    	'console_scripts': [
    		'zeppelin-convert = zeppelin.cli.convert:main',
    		'zeppelin-execute = zeppelin.cli.execute:main'
    	],
    },
    packages=find_packages(),
    setup_requires=['pytest-runner', 'cairosvg'],
    tests_require=['pytest']
)
