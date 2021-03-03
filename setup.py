# We need to have setup.py to make `thenewboston-python` installable in editable mode
# See https://github.com/pypa/pip/issues/6605

import sys
from setuptools import setup, find_namespace_packages


def make_dependencies(source):
    dependencies = []
    for dependency, version in source.items():
        if dependency == 'python':
            continue

        if version.startswith('^'):
            version = version[1:]

        dependencies.append(dependency + version)

    return dependencies


if len(sys.argv) > 1 and sys.argv[1] not in ('develop', '--help', '--help-commands'):
    print('Do not use the setup.py for anything other than installing '
          'in editable (development) mode.')
    print('To build a source distribution use: poetry build')
    sys.exit(1)


try:
    import toml
except ImportError:
    raise ImportError('toml dependency must be installed (pip install \'toml>=0.10.2\') '
                      'to have setup.py operational')

with open('pyproject.toml') as f:
    pyproject = toml.load(f)

poetry_cfg = pyproject['tool']['poetry']
author = poetry_cfg['authors'][0] if poetry_cfg['authors'] else None

packages = []
for package in poetry_cfg['packages']:
    packages.extend(find_namespace_packages(package.get('from', '.'),
                                            include=f"{package['include']}.*"))

# TODO(dmu) LOW: Improve the way we get package_dir to support the case of multiple dirs
assert len(poetry_cfg['packages']) == 1
package_dir = {'': poetry_cfg['packages'][0]['from']}

setup(
    name=poetry_cfg['name'],
    version=poetry_cfg['version'],
    description=poetry_cfg['description'],
    license=poetry_cfg['license'],
    author=author,
    author_email=author if '<' in author else None,
    maintainer=poetry_cfg['maintainers'][0] if poetry_cfg['maintainers'] else None,
    url=poetry_cfg['homepage'],
    long_description=f"file: {poetry_cfg['readme']}",
    long_description_content_type=(
        'text/markdown' if poetry_cfg['readme'].lower().endswith('.md') else 'text/plain'
    ),
    package_dir=package_dir,
    packages=packages,
    package_data={'': ['*']},
    python_requires=poetry_cfg["dependencies"]["python"].replace('^', '>=') + ',<4.0',
    install_requires=make_dependencies(poetry_cfg['dependencies']),
    extras_require={"dev": make_dependencies(poetry_cfg['dev-dependencies'])},
    include_package_data=True,
    zip_safe=False,
)
