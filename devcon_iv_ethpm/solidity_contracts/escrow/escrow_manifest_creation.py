import json
from pathlib import Path

from ethpm.tools import builder as b
from ethpm.backends.ipfs import InfuraIPFSBackend
from pytest_ethereum.plugins import twig_manifest

from devcon_iv_ethpm.setup import SOLIDITY_CONTRACTS_DIR


# CREATE A MANIFEST FROM YOUR SOLIDITY CONTRACTS
# if you run into a jam - ask us on the gitter ethpm channel!

# Here's an walkthrough of how to create a manifest for the Escrow contracts located @
# - - https://github.com/ethpm/ethpm-spec/tree/master/examples/escrow
# It should prove as a useful guide for your own solidity contracts, feel free to edit or change this file as much as you please.


# GENERATE YOUR SOLC OUTPUT
# Before we can create a manifest, you need to generate the solidity compiler standard-json output for your contracts.

# Copy and paste your solidity contract(s) into `devcon_iv_ethpm/solidity_contracts/`
# Adjust `/devcon_iv_ethpm/solidity_contracts/sample_solc_standard_json_input.json` with the applicable file paths for your contracts.

# The docs for the using the solidity compiler in this manner can be found at this link
# https://solidity.readthedocs.io/en/v0.4.24/using-the-compiler.html#compiler-input-and-output-json-description

# Every contract you wish to add in your manifest should have its own object in the "sources" field. Be sure replace "ContractOne.sol" with your contract filename and "absolute/path/to/ContractOne.sol" with the absolute filepath to your contract.


# run the following command from your terminal

# solc --allow-paths <path-to-contract-directory> --standard-json < <standard-json-input.json> > <owned_compiler_output.json>

# <path-to-contract-directory> is just any absolute path that contains the target contracts somewhere in its tree
# <standard-json-input.json> is the relative path to the standard-json compiler input you created above.
# <owned_compiler_output.json> is the relative path to where you want the compiler output to be written


# copy your solc output & contracts into `devcon_iv_ethpm/solidity_contracts` and add file name here

PACKAGE_FOLDER = SOLIDITY_CONTRACTS_DIR / "escrow"

CONTRACTS_FOLDER = PACKAGE_FOLDER / "contracts"

COMPILER_OUTPUT_PATH = PACKAGE_FOLDER / "std_output.json"

compiler_output = json.loads(COMPILER_OUTPUT_PATH.read_text())["contracts"]
ipfs_backend = InfuraIPFSBackend()

manifest = b.build(
    {},
    b.package_name("escrow"),
    b.version("1.0.0"),
    b.manifest_version("2"),
    # AUTOPOPULATES "package_name", "version", and "manifest_version"
    # b.init_manifest(<pkg_name>, <version>),
    # META FIELDS
    b.description("one super sweet escrow package"),
    b.license("MIT"),
    b.authors("Ongo Gablovian", "Brian LeFevre"),
    b.keywords("payments", "escrow", "solidity"),
    b.links(
        repo="www.github.com/path/to/source",
        documentation="www.readthedocs.com/path/to/docs",
        website="www.website.com",
    ),
    b.pin_source("Escrow", compiler_output, ipfs_backend, CONTRACTS_FOLDER),
    b.inline_source("SafeSendLib", compiler_output, CONTRACTS_FOLDER),
    b.contract_type("Escrow", compiler_output),
    b.contract_type(
        "SafeSendLib",
        compiler_output,
        abi=True,
        deployment_bytecode=True,
        runtime_bytecode=True,
    ),
    # INVALID DEPLOYMENT DATA - FOR DISPLAY USE ONLY
    # b.deployment(
    #   block_uri='blockchain://1234567890123456789012345678901234567890123456789012345678901234/block/1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef',
    # contract_instance='SafeSendLibStaging',
    # contract_type='SafeSendLib',
    # address=to_canonical_address('0x4f5b11c860b37b68de6d14fb7e7b5f18a9a1bd00'),
    # ),
    b.validate()
    # b.write_to_disk(
    # manifest_root_dir: Optional[Path],
    # manifest_name: Optional[str],
    # prettify: Optional[bool],
    # )
    # MUST BE FINAL BUILDER FN
    # b.as_package(w3)
    # b.pin_to_ipfs(backend=infura_backend),
)

print("")
print("Your beautiful manifest")
print("-----------------------")
print(json.dumps(manifest, indent=4))
