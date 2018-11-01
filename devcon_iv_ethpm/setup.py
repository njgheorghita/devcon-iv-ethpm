from pathlib import Path
from eth_utils import to_checksum_address, to_hex, to_canonical_address
from ens import ENS
from web3.auto.infura.ropsten import w3
from web3.pm import PM
from web3.middleware import construct_sign_and_send_raw_middleware

from devcon_iv_ethpm.constants import ROPSTEN_ACCOUNT_ADDRESS, ACCOUNT_PRIVATE_KEY

SOLIDITY_CONTRACTS_DIR = Path(__file__).parent / "solidity_contracts"


def ropsten_ens_w3():
    signing_middleware = construct_sign_and_send_raw_middleware(ACCOUNT_PRIVATE_KEY)
    w3.middleware_stack.add(signing_middleware)
    w3.eth.defaultAccount = to_checksum_address(ROPSTEN_ACCOUNT_ADDRESS)
    rns = ENS(w3.providers, addr="0xbaB9717617D7e50264dE6Ee0Ef152a7CA452CF9C")
    w3.ens = rns
    PM.attach(w3, "pm")
    return w3


def tie_registry_to_ens(ens_name, registry_address, w3):
    print("ENS setup")
    ens_domain = ens_name + ".test"
    rns = w3.ens
    reg_addr = rns.address("test")
    reg_abi = [
        {
            "inputs": [
                {"name": "label", "type": "bytes32"},
                {"name": "owner", "type": "address"},
            ],
            "name": "register",
            "outputs": [],
            "payable": False,
            "stateMutability": "nonpayable",
            "constant": False,
            "type": "function",
        }
    ]
    reg = w3.eth.contract(address=to_canonical_address(reg_addr), abi=reg_abi)
    my_hash = rns.labelhash(ens_name)
    nonce_1 = w3.eth.getTransactionCount(ROPSTEN_ACCOUNT_ADDRESS)
    txn_1 = reg.functions.register(my_hash, ROPSTEN_ACCOUNT_ADDRESS).transact()
    print("waiting to mine tx 1", to_hex(txn_1))
    w3.eth.waitForTransactionReceipt(txn_1)
    print("tx1 mined")

    resolver_addr = to_canonical_address(rns.address("resolver.eth"))
    raw_ens = rns.ens._classic_contract
    nonce_2 = w3.eth.getTransactionCount(ROPSTEN_ACCOUNT_ADDRESS)
    txn_2 = raw_ens.functions.setResolver(
        rns.namehash(ens_domain), resolver_addr
    ).buildTransaction(
        {
            "chainId": 3,
            "gas": 300000,
            "gasPrice": w3.toWei("10", "gwei"),
            "nonce": nonce_2,
        }
    )

    signed_txn_2 = w3.eth.account.signTransaction(txn_2, ACCOUNT_PRIVATE_KEY)
    # Broadcast your transaction
    tx_hash_2 = w3.eth.sendRawTransaction(signed_txn_2.rawTransaction)
    print("waiting to mine tx 2", to_hex(tx_hash_2))
    w3.eth.waitForTransactionReceipt(tx_hash_2)
    print("tx 2 mined")

    resolver_abi = [
        {
            "inputs": [
                {"name": "node", "type": "bytes32"},
                {"name": "addr", "type": "address"},
            ],
            "constant": False,
            "name": "setAddr",
            "outputs": [],
            "stateMutability": "nonpayable",
            "payable": False,
            "type": "function",
        }
    ]
    resolver = w3.eth.contract(address=resolver_addr, abi=resolver_abi)
    namehash = rns.namehash(ens_domain)
    nonce_3 = w3.eth.getTransactionCount(ROPSTEN_ACCOUNT_ADDRESS)
    txn_3 = resolver.functions.setAddr(namehash, registry_address).buildTransaction(
        {
            "chainId": 3,
            "gas": 300000,
            "gasPrice": w3.toWei("10", "gwei"),
            "nonce": nonce_3,
        }
    )

    signed_txn_3 = w3.eth.account.signTransaction(txn_3, ACCOUNT_PRIVATE_KEY)
    # Broadcast your transaction
    tx_hash_3 = w3.eth.sendRawTransaction(signed_txn_3.rawTransaction)
    print("waiting to mine tx 3", to_hex(tx_hash_3))
    w3.eth.waitForTransactionReceipt(tx_hash_3)
    print("tx mined 3")

    if registry_address == rns.address(ens_domain):
        print("Congrats!")
        print("Registry @ address: {0} tied to ENS name: {1}.".format(registry_address, ens_domain))
