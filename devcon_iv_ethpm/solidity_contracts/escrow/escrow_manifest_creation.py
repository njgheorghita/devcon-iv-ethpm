import json
from pathlib import Path

from ethpm.tools import builder as b
from ethpm.backends.ipfs import InfuraIPFSBackend
from pytest_ethereum.plugins import twig_manifest


# CREATE A MANIFEST FROM YOUR SOLIDITY CONTRACTS
# if you run into a jam - ask us on the gitter ethpm channel!

# Here's an example of how to create a manifest for the Escrow contracts that can be found at
# - - https://github.com/ethpm/ethpm-spec/tree/master/examples/escrow
# It should prove as a useful guide for your own solidity contracts, feel free to edit or change this file as much as you please.
# Before we can create a manifest, you need to generate the solidity standard-json output for your contracts.


# GENERATE YOUR SOLC OUTPUT

# Copy and paste your solidity contract(s) into `devcon_iv_ethpm/solidity_contracts/`
# Adjust `/devcon_iv_ethpm/solidity_contracts/sample_solc_standard_json_input.json` with the applicable file paths for your contracts.

# The docs for the using the solidity compiler in this manner can be found at this link
# https://solidity.readthedocs.io/en/v0.4.24/using-the-compiler.html#compiler-input-and-output-json-description

# Every contract you wish to add in your manifest should have its own object in the "sources" field. Be sure replace "ContractOne.sol" with your contract filename and "absolute/path/to/ContractOne.sol" with the absolute filepath to your contract.


# run the following command from your terminal

# solc --allow-paths <path-to-contract-directory> --standard-json < standard-json-input.json > owned_compiler_output.json

# <path-to-contract-directory> is just any absolute path that contains the target contracts somewhere in its tree
# <standard-json-input.json> is the relative path to the standard-json compiler input you created above.
# <owned_compiler_output.json> is the relative path to where you want the compiler output to be written




# copy your solc output & contracts into `devcon_iv_ethpm/solidity` and add file name here
# COMPILER_OUTPUT_PATH = Path(__file__).parent / 'solidity' / '<solc_output_file_name_here>.json'

SOLIDITY_FOLDER = Path(__file__).parent / 'solidity_contracts'

PACKAGE_FOLDER = SOLIDITY_FOLDER / 'escrow'

COMPILER_OUTPUT_PATH = PACKAGE_FOLDER / 'std_output.json'

compiler_output = json.loads(COMPILER_OUTPUT_PATH.read_text())['contracts']
infura_backend = InfuraIPFSBackend()

manifest = b.build(
    {},
    b.package_name("escrow"),
    b.version("1.0.0"),
    b.manifest_version("2"),
    # META FIELDS
    # b.description("one super sweet escrow package"),
    # b.license("MIT"),
    # b.authors("Ongo Gablovian", "Brian LeFevre"),
    # b.keywords("payments", "escrow", "solidity"),
    # b.links(
        # repo="www.github.com/path/to/source",
        # documentation="www.readthedocs.com/path/to/docs",
        # website="www.website.com",
    # ),
    # autopopulates manifest_version
    # b.init_manifest(<pkg_name>, <version>),
    # pinner
    # inline source
    b.pin_source("Escrow", compiler_output, infura_backend, PACKAGE_FOLDER),
    b.pin_source("SafeSendLib", compiler_output, infura_backend, PACKAGE_FOLDER),
    b.contract_type("Escrow", compiler_output),
    b.contract_type("SafeSendLib", compiler_output),
    # b.deployment()
    # w/ deployment type
    # if you add a deployment with link_refs, then you have to make sure to add them - hint look in the runtime bytecode of the contract type
    # b.validate()
    # b.write_to_disk(
        # manifest_root_dir: Optional[Path],
        # manifest_name: Optional[str],
        # prettify: Optional[bool],
    # )
    # must be last option
    # b.as_package(w3)
    # b.pin_to_ipfs(backend=infura_backend),
)

print('')
print('Your beautiful manifest')
print('-----------------------')
print(json.dumps(manifest, indent=4))
