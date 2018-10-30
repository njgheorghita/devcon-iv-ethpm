# devcon-iv-ethpm

[![Python versions](https://img.shields.io/pypi/pyversions/devcon-iv-ethpm.svg)](https://pypi.python.org/pypi/devcon-iv-ethpm)
   

Starter repo for the devcon iv ethpm workshop.

This repo is designed to be used with the Ropsten testnet. However, it can very easily be adapted for other testnets / local nodes. But you need to figure that out on your own.

## Quickstart

Must have python >= 3.6 installed on your machine.

You can set up your dev environment with:

install web3 pm from branch

```sh
git clone git@github.com:ethereum/devcon-iv-ethpm.git
cd devcon-iv-ethpm
python3 -m venv venv
. venv/bin/activate
pip install -e .[dev]
pip install --upgrade --force-reinstall git+https://github.com/ethereum/web3.py@pm-api
```

SETUP YOUR CONSTANTS HERE!!!

# DEVS!!

If you would like to hack on other Python projects in the Ethereum ecosystem, please check out the
[Ethereum Development Tactical Manual](https://github.com/pipermerriam/ethereum-dev-tactical-manual)
for information on how we do:

- Testing
- Pull Requests
- Code Style
- Documentation


