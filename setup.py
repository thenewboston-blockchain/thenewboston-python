from os import path

from setuptools import find_packages, setup

with open(path.join(path.abspath(path.dirname(__file__)), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    install_requires=[
        'Django==3.1.1',
        'PTable==0.9.2',
        'PyNaCl==1.3.0',
        'channels-redis==2.4.2',
        'channels==2.4.0',
        'django-cors-headers==3.4.0',
        'djangorestframework==3.11.1',
        'factory-boy==3.0.1',
        'pycodestyle==2.6.0',
        'pytest-asyncio==0.14.0',
        'pytest-cov==2.10.1',
        'pytest-django==3.10.0',
        'pytest==6.0.2',
        'requests~=2.24.0',
        'sentry-sdk==0.18.0'
    ],
    long_description=long_description,
    long_description_content_type='text/markdown',
    name='thenewboston',
    packages=find_packages(
        exclude=['tests', 'tests.*']
    ),
    version='0.0.23',
)
