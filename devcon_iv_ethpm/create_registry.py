import json
from pathlib import Path
import os
from eth_utils import is_address, to_hex, to_bytes
import ethpm
from web3.auto.infura.ropsten import w3
from web3.pm import PM
from devcon_iv_ethpm.constants import (
    INFURA_ROPSTEN_API_KEY,
    REGISTRY_ABI,
    REGISTRY_BYTECODE,
)


# Setup
os.environ['WEB3_INFURA_API_KEY'] = INFURA_ROPSTEN_API_KEY

# Create your registry contract factory
registry = w3.eth.contract(abi=REGISTRY_ABI, bytecode=REGISTRY_BYTECODE)

# Build your transaction to deploy the registry
nonce = w3.eth.getTransactionCount(ACCOUNT_ADDRESS)
registry_txn = registry.constructor().buildTransaction({
    'chainId': 3,
    'gas': 3000000,
    'gasPrice': w3.toWei('10', 'gwei'),
    'nonce': nonce,
})
signed_txn = w3.eth.account.signTransaction(registry_txn, PRIVATE_KEY)

# Broadcast your transaction
tx_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)

##
#
# ENS steal from carver
# test ens for play_with_registry
#


print("Transaction: {0} created".format(to_hex(tx_hash)))
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
registry_address = tx_receipt.contractAddress
print("Registry created at address: {0}".format(registry_address))
