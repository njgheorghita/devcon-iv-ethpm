import json
from pathlib import Path
from web3.auto.infura.ropsten import w3
from eth_account import Account


ACCOUNT_PRIVATE_KEY = (
    "0xC7E9110E69ACA7BA60DB396F8272B58763B0D576EB4233F809FD0E08AA3EFEBB"
)

# 📦📦📦
# if you have a paper wallet (NOT SECURE - don't use to store real eth!)
# --------------------------
# go to webqr.com - allow website permission to access camera - scan your qr code - copy and paste your private key below

# if using metamask
# -----------------
# copy your private key - and paste it below

# ACCOUNT_PRIVATE_KEY = "0x6b51817ef7c1bc670db76f609a0a47c7..."
ROPSTEN_ACCOUNT_ADDRESS = Account.privateKeyToAccount(ACCOUNT_PRIVATE_KEY).address


# Vyper registry setup
ASSETS_DIR = Path(__file__).parent / "assets"
VYPER_REGISTRY_MANIFEST = json.loads(
    (ASSETS_DIR / "vyper_registry" / "1.0.2.json").read_text()
)
REGISTRY_ABI = VYPER_REGISTRY_MANIFEST["contract_types"]["registry"]["abi"]
REGISTRY_BYTECODE = VYPER_REGISTRY_MANIFEST["contract_types"]["registry"][
    "deployment_bytecode"
]["bytecode"]

# Vyper manifest setup
DEVCON_IV_ETHPM_DIR = Path(__file__).parent
VYPER_FOLDER = DEVCON_IV_ETHPM_DIR / "vyper_contracts"
MANIFEST_FOLDER = DEVCON_IV_ETHPM_DIR / "manifests"
