# devcon-iv-ethpm

Starter repo for the devcon iv ethpm workshop.

This repo is designed to be used with the Ropsten testnet over Infura. However, it can very easily be adapted for other testnets / local nodes.


## Quickstart

Must have python >= 3.6 installed on your machine.

You can set up your dev environment with:

```sh
git clone git@github.com:ethereum/devcon-iv-ethpm.git
cd devcon-iv-ethpm
python3 -m venv venv
. venv/bin/activate
pip install -e .[dev]
pip install --upgrade --force-reinstall git+https://github.com/ethereum/web3.py@pm-api
```

To interact with an on-chain registry, you must fill in these three variables in `devcon_iv_ethpm/constants.py`.

```
INFURA_ROPSTEN_API_KEY =
ACCOUNT_ADDRESS =
PRIVATE_KEY = 
```


# DEVS!!

If you would like to hack on other Python projects in the Ethereum ecosystem, please check out the
[Ethereum Development Tactical Manual](https://github.com/pipermerriam/ethereum-dev-tactical-manual)
for information on how we do:

- Testing
- Pull Requests
- Code Style
- Documentation
