from setuptools import setup, find_packages

setup(
    install_requires=[
        'Django==3.0.8',
        'PTable==0.9.2',
        'PyNaCl==1.3.0',
        'django-cors-headers==3.4.0',
        'djangorestframework==3.11.0',
        'pycodestyle==2.6.0',
        'requests~=2.23.0',
    ],
    name='thenewboston',
    packages=find_packages(
        exclude=['tests', 'tests.*']
    ),
    version='0.0.7',
)
