# devcon-iv-ethpm

Starter repo for the devcon iv ethpm workshop.

This repo is designed to be used with the Ropsten testnet over Infura. However, it can very easily be adapted for other testnets / local nodes.


## Quickstart

Must have python >= 3.6 installed on your machine.

You can set up your dev environment with:

```sh
git clone https://github.com/njgheorghita/devcon-iv-ethpm.git
cd devcon-iv-ethpm
python3 -m venv venv
. venv/bin/activate
pip install -e .[dev]
pip install --upgrade --force-reinstall git+https://github.com/ethereum/web3.py@pm-api
```

To interact with an on-chain registry, you must fill in the `ACCOUNT_PRIVATE_KEY` variable in `devcon_iv_ethpm/constants.py`. 

If you have a paper wallet:
- Go to [www.webqr.com](www.webqr.com).
- Give permission for site to access your webcam
- Scan your qr code
- Copy and paste your private key into the `ACCOUNT_PRIVATE_KEY` constant in `devcon_iv_ethpm/constants.py`.
- PLEASE NOT THAT THIS IS NOT A SECURE ACCOUNT, AND SHOULD NOT BE USED TO STORE REAL MAINNET ETH

If you want to use your metamask account:
- Copy your private key (for Ropsten network)
- Copy and paste your private key into the `ACCOUNT_PRIVATE_KEY` constant in `devcon_iv_ethpm/constants.py`.
- Be careful not to commit / push this private key to github if you use it on the mainnet.

`ACCOUNT_PRIVATE_KEY` should be filled in as 0x prefixed hex strings.

If you want to generate a manifest for solidity contracts, you must also have the solidity compiler installed on your machine. [Installation Guide](https://solidity.readthedocs.io/en/v0.4.24/installing-solidity.html).

If you run into this error:
SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED]
run this: `/Applications/Python\ 3.7/Install\ Certificates.command`

# OPEN CALL FOR DEVS

If you would like to hack on other Python projects in the Ethereum ecosystem, please check out the
[Ethereum Development Tactical Manual](https://github.com/pipermerriam/ethereum-dev-tactical-manual)
for information on how we do:

- Testing
- Pull Requests
- Code Style
- Documentation
