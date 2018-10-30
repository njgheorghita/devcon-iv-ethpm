# if you haven't created a vyper registry on the ropsten checkout `create_registry.py`

import os
import json
from pathlib import Path
from eth_utils import to_checksum_address, to_hex, to_canonical_address
from web3.pm import PM
from web3.auto.infura.ropsten import w3
from web3.middleware import construct_sign_and_send_raw_middleware

from devcon_iv_ethpm.constants import REGISTRY_ABI, ACCOUNT_ADDRESS, PRIVATE_KEY, INFURA_ROPSTEN_API_KEY

os.environ['WEB3_INFURA_API_KEY'] = INFURA_ROPSTEN_API_KEY
os.environ['ETHPM_IPFS_BACKEND_CLASS'] = "ethpm.backends.ipfs.LocalIPFSBackend"


REGISTRY_ADDRESS = to_checksum_address('0xe7D683c671A5D5879de8858B1ac292920E6A2578')

PM.attach(w3, 'pm')

w3.pm.set_registry(REGISTRY_ADDRESS)
signing_middleware = construct_sign_and_send_raw_middleware(PRIVATE_KEY)
registry = w3.eth.contract(address=to_canonical_address(REGISTRY_ADDRESS), abi=REGISTRY_ABI)
w3.middleware_stack.add(signing_middleware)
w3.eth.defaultAccount = to_checksum_address(ACCOUNT_ADDRESS)

# continue escrow example? 
# show off some linking?

ENS = w3.ens.fromWeb3(w3, to_checksum_address("0x112234455c3a32fd11230c42e7bccd4a84e02010"))

# run `ipython -i devcon_iv_ethpm/play_with_registry.py`
