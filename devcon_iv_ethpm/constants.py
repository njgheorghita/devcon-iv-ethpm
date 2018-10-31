import json
from pathlib import Path
from web3.auto.infura.ropsten import w3


# 📦📦📦
INFURA_ROPSTEN_API_KEY = "e9befc16e92140f193f9ef140ec1b839"
ROPSTEN_ACCOUNT_ADDRESS = "0x0067D9619328A8Db708b941aD36D6565986D1c85"
ACCOUNT_PRIVATE_KEY = "0xC7E9110E69ACA7BA60DB396F8272B58763B0D576EB4233F809FD0E08AA3EFEBB"
# Replace the following variables with your metamask ropsten account/private key here....
# ROPSTEN_ACCOUNT_ADDRESS = '0x0067D961932....'
# ACCOUNT_PRIVATE_KEY = '0xC7E9110E....'


# Vyper registry setup
ASSETS_DIR = Path(__file__).parent / 'assets'
VYPER_REGISTRY_MANIFEST = json.loads((ASSETS_DIR / 'vyper_registry' / '1.0.2.json').read_text())
REGISTRY_ABI = VYPER_REGISTRY_MANIFEST['contract_types']['registry']['abi']
REGISTRY_BYTECODE = VYPER_REGISTRY_MANIFEST['contract_types']['registry']['deployment_bytecode']['bytecode']

# Vyper manfiest setup
DEVCON_IV_ETHPM_DIR = Path(__file__).parent
VYPER_FOLDER = DEVCON_IV_ETHPM_DIR / 'vyper_contracts'
MANIFEST_FOLDER = DEVCON_IV_ETHPM_DIR / 'manifests'