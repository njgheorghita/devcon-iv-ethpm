from eth_utils import to_checksum_address, to_canonical_address
from devcon_iv_ethpm.setup import ropsten_ens_w3


# If you haven't created a vyper registry on the ropsten checkout `create_registry.py`
w3 = ropsten_ens_w3()


# 📦📦📦
# If you want to interact with your own registry, and not the pre-loaded workshop registry,
# copy and paste its Ropsten address here.
WORKSHOP_REGISTRY_ADDRESS = to_canonical_address(
    "0xe7D683c671A5D5879de8858B1ac292920E6A2578"
)


# If you created your registry with ens (in create_registry.py), you can use that name here
# remove `WORKSHOP_REGISTRY_ADDRESS` and replace it with "yourensnamehere.test"

w3.pm.set_registry(WORKSHOP_REGISTRY_ADDRESS)


# # # THIS SECTION IS FOR DEMO PURPOSES ONLY # # #

escrow_package = w3.pm.get_package(b"escrow", b"1.0.3")
escrow_factory = escrow_package.get_contract_factory("Escrow")
safe_send_lib_factory = escrow_package.get_contract_factory("SafeSendLib")
# # TRY
# escrow_factory.constructor(w3.eth.defaultAccount).transact()
# tx = safe_send_lib_factory.constructor().transact()
# receipt = w3.eth.waitForTransactionReceipt(tx)
# linked_escrow_factory = escrow_factory.link_bytecode({"SafeSendLib": to_canonical_address(receipt.contractAddress)})
# tx_2 = linked_escrow_factory.constructor(w3.eth.defaultAccount).transact()
# receipt_2 = w3.eth.waitForTransactionReceipt(tx_2)
# print(receipt_2.contractAddress)

# # # END DEMO SECTION # # #

# SCAVENGER HUNT
# you will need to use the registry loaded at WORKSHOP_REGISTRY_ADDRESS to win the hunt
# clue = "snakecharmer"
# first person to yell out the secret phrase as loud as possible wins a snakecharmer hat!

# run `ipython -i devcon_iv_ethpm/play_with_registry.py`
print("you should have a w3 instance available, fully loaded with the PM module")
