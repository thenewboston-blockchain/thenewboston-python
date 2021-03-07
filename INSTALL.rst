Local development environment setup
===================================

This section describes how to setup development environment for Debian-based distributions
(tested on Linux Mint 18.3 specifically)

Initial setup
-------------
Once initial setup is done only corresponding `Update`_ section should be performed
to get the latest version for development.

#. Install prerequisites::

    apt update
    apt install git

#. [if you have not configured it globally] Configure git::

    git config user.name 'Firstname Lastname'
    git config user.email 'youremail@youremail_domain.com'

#. Install prerequisites (
   as prescribed at https://github.com/pyenv/pyenv/wiki/Common-build-problems )::

    apt update &&
    apt install make build-essential libssl-dev zlib1g-dev libbz2-dev \
                libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
                libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl
    # TODO(dmu) MEDIUM: Remove those that are not really needed

#. Fork https://github.com/thenewboston-developers/thenewboston-python repository
#. Clone the fork::

    git clone git@bitbucket.org:<replace with you github name>/thenewboston-python.git

#. Add https://github.com/thenewboston-developers/thenewboston-python as upstream::

    cd thenewboston-python
    git remote add upstream git@github.com:thenewboston-developers/thenewboston-python.git
    git fetch upstream

#. Install and configure `pyenv` according to https://github.com/pyenv/pyenv#basic-github-checkout
#. Install lowest supported Python version::

    pyenv install 3.7.9
    pyenv local 3.7.9  # run from the root of this repo (`.python-version` file should appear)

#. Create and activate virtual env::

    python -m venv .venv
    source .venv/bin/activate

#. Upgrade pip::

    pip install pip==21.0.1

#. Proceed to `Update`_ section

Update
------
#. Install the library with dependencies::

    pip install -e .

Test
---
#. Test with coverage::

    pytest --cov-config=.coveragerc --cov=./src

#. Lint::

    flake8 .
