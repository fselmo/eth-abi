# Ethereum Contract Interface (ABI) Utility

[![Join the conversation on Discord](https://img.shields.io/discord/809793915578089484?color=blue&label=chat&logo=discord&logoColor=white)](https://discord.gg/GHryRvPB84)
[![Build Status](https://circleci.com/gh/ethereum/eth-abi.svg?style=shield)](https://circleci.com/gh/ethereum/eth-abi)
[![PyPI version](https://badge.fury.io/py/eth-abi.svg)](https://badge.fury.io/py/eth-abi)
[![Python versions](https://img.shields.io/pypi/pyversions/eth-abi.svg)](https://pypi.python.org/pypi/eth-abi)
[![Docs build](https://readthedocs.org/projects/eth-abi/badge/?version=latest)](https://eth-abi.readthedocs.io/en/latest/?badge=latest)
   

Python utilities for working with Ethereum ABI definitions, especially encoding and decoding

Read more in the [documentation on ReadTheDocs](https://eth-abi.readthedocs.io/). [View the change log](https://eth-abi.readthedocs.io/en/latest/release_notes.html).

## Quickstart

```sh
pip install eth_abi
```

## Developer Setup

If you would like to hack on eth-abi, please check out the [Snake Charmers
Tactical Manual](https://github.com/ethereum/snake-charmers-tactical-manual)
for information on how we do:

- Testing
- Pull Requests
- Code Style
- Documentation

### Development Environment Setup

You can set up your dev environment with:

```sh
git clone git@github.com:ethereum/eth-abi.git
cd eth-abi
virtualenv -p python3 venv
. venv/bin/activate
pip install -e ".[dev]"
```

### Release setup

To release a new version:

```sh
make release bump=$$VERSION_PART_TO_BUMP$$
```

#### How to bumpversion

The version format for this repo is `{major}.{minor}.{patch}` for stable, and
`{major}.{minor}.{patch}-{stage}.{devnum}` for unstable (`stage` can be alpha or beta).

To issue the next version in line, specify which part to bump,
like `make release bump=minor` or `make release bump=devnum`. This is typically done from the
master branch, except when releasing a beta (in which case the beta is released from master,
and the previous stable branch is released from said branch).

If you are in a beta version, `make release bump=stage` will switch to a stable.

To issue an unstable version when the current version is stable, specify the
new version explicitly, like `make release bump="--new-version 4.0.0-alpha.1 devnum"`
