# -*- coding: utf-8 -*-
"""
@author: Rodrigo Gomes
"""
from __future__ import absolute_import, print_function, unicode_literals
from os import path
from codecs import open
from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()

setup(
        name='django-basic-view',
        version='0.0.1',
        description="Django Router",
        long_description=long_description,
        author='Rodrigo Gomes',
        url='https://github.com/rodgomes/django-router',
        classifiers=[
                    'Development Status :: 3 - Alpha',
                    'Intended Audience :: Developers',
                    'Programming Language :: Python :: 2.7',
                ],
        keywords='django urls',
        install_requires=[
                    'django>1.7.9',
                    'pyparsing',
                ],
        packages=find_packages()
)
