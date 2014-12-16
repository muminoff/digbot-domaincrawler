#!/usr/bin/env python
"""
DigDomainCrawler
================

:copyright: (c) 2014 DigSearch
:license: Apache
"""

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import sys

for m in ('multiprocessing', 'billiard'):
    try:
        __import__(m)
    except ImportError:
        pass


install_requires = [
    'gevent==1.0.1',
    'netaddr==0.7.12'
]

setup(
    name='ddcrawler',
    version='0.0.0-DEV',
    author='DigSearch',
    author_email='rd@dig.uz',
    url='https://rd.dig.uz',
    description='Domain crawler bot',
    long_description=open('README.md').read(),
    package_dir={'': '.'},
    packages=find_packages('ddcrawler.py'),
    zip_safe=False,
    install_requires=install_requires,
    license='Apache',
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'ddcrawler = ddcrawler:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
