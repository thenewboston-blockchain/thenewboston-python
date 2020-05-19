from setuptools import setup, find_packages

setup(
    install_requires=[
        'PTable==0.9.2',
        'requests~=2.23.0'
    ],
    name='thenewboston',
    packages=find_packages(
        exclude=['tests', 'tests.*']
    ),
    version='0.0.1',
)
