# -*- coding: utf-8 -*-
import re

from setuptools import find_packages, setup

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

with open('requirements.txt', encoding='utf-8') as f:
    requirements = f.read().splitlines()

with open('src/thenewboston/__init__.py', encoding='utf8') as f:
    version = re.search(r'__version__ = \'(.*?)\'', f.read()).group(1)

setup(
    install_requires=requirements,
    long_description=long_description,
    long_description_content_type='text/markdown',
    name='thenewboston',
    packages=find_packages(
        exclude=['tests', 'tests.*']
    ),
    version=version,
)
