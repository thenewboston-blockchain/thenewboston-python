from setuptools import setup, find_packages

setup(
    install_requires=[
        'Django==3.1',
        'PTable==0.9.2',
        'PyNaCl==1.3.0',
        'django-cors-headers==3.4.0',
        'djangorestframework==3.11.1',
        'factory-boy==3.0.1',
        'pycodestyle==2.6.0',
        'pytest-django==3.9.0',
        'pytest==6.0.1',
        'requests~=2.23.0',
    ],
    name='thenewboston',
    packages=find_packages(
        exclude=['tests', 'tests.*']
    ),
    version='0.0.13',
)
