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

To interact with an on-chain registry, you must fill in these three variables in `devcon_iv_ethpm/constants.py`. If you do not have an Infura API key for Ropsten, you can sign up for one [here](https://infura.io). If you do not have a Ropsten account, you can use [MetaMask](https://metamask.io) to set one up, which will also generate a private key for you to use. If you do not have any Ropsten testnet ether, you can acquire some via this [faucet](https://faucet.ropsten.be/)

Both `ROPSTEN_ACCOUNT_ADDRESS` and `ACCOUNT_PRIVATE_KEY` should be filled in as 0x prefixed hex strings.

```
INFURA_ROPSTEN_API_KEY =
ROPSTEN_ACCOUNT_ADDRESS =
ACCOUNT_PRIVATE_KEY = 
```

If you want to generate a manifest for solidity contracts, you must also have the solidity compiler installed on your machine. [Installation Guide](https://solidity.readthedocs.io/en/v0.4.24/installing-solidity.html).

# DEVS!!

If you would like to hack on other Python projects in the Ethereum ecosystem, please check out the
[Ethereum Development Tactical Manual](https://github.com/pipermerriam/ethereum-dev-tactical-manual)
for information on how we do:

- Testing
- Pull Requests
- Code Style
- Documentation
