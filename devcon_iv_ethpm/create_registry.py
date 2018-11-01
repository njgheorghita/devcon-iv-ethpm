from eth_utils import to_hex
from devcon_iv_ethpm.constants import VYPER_REGISTRY_MANIFEST
from ethpm import Package
from devcon_iv_ethpm.setup import ropsten_ens_w3, tie_registry_to_ens


# Create your registry contract factory
w3 = ropsten_ens_w3()
registry_package = Package(VYPER_REGISTRY_MANIFEST, w3)
registry_factory = registry_package.get_contract_factory("registry")


# Deploy the registry
registry_txn = registry_factory.constructor().transact()


print("Transaction: {0} created".format(to_hex(registry_txn)))
tx_receipt = w3.eth.waitForTransactionReceipt(registry_txn)
registry_address = tx_receipt.contractAddress
print("Registry created at address: {0}".format(registry_address))


# to tie your registry to an ens name of your choice - fill in the variable ENS_NAME below
#   - do *not* include a tld in your name (i.e '.test' / '.eth')
#   - the `tie_registry_to_ens` function will automatically add '.test' to your ens name

# Be sure to save the contract address generated above and ens name used here, they will be used later
ENS_NAME = "ENSNAMEHERE"
tie_registry_to_ens(ENS_NAME, registry_address, w3)
