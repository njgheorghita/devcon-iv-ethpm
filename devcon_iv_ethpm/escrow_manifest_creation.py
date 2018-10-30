import json
from pathlib import Path

from ethpm.tools import builder as b
from ethpm.backends.ipfs import InfuraIPFSBackend
from pytest_ethereum.plugins import twig_manifest


# CREATE A MANIFEST FROM YOUR SOLIDITY / VYPER CONTRACTS

# full disclosure - this process has only been tested for simple contracts
# if you have complex contracts - be warned
# ask us on gitter!!

# SOLIDITY

# Here's an example of how to create a manifest for the Escrow contracts that can be found at _______.
# It should prove as a useful guide for your own contracts.?xxxx

# Step 1: Compile the contracts
# Contracts -> SOLC output

# Ingredients
# Copy and paste your contracts into `devcon_iv_ethpm/solidity_contracts/`
# Adjust `/devcon_iv_ethpm/solidity_contracts/sample_solc_standard_json_input.json` to suit your needs (XXX) what to fill in



# run the following command from your terminal
# <path-to-contract-directory> is just any absolute path that contains the target contracts somewhere in its tree
# <standard-json-input.json> is the relative path to the standard-json compiler input you created in line 21 (XXX)
# <owned_compiler_output.json> is the relative path to where you want the compiler output to be written


# solc --allow-paths <path-to-contract-directory> --standard-json < standard-json-input.json > owned_compiler_output.json


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
    # b.validate()
    # b.write_to_disk(
        # manifest_root_dir: Optional[Path],
        # manifest_name: Optional[str],
        # prettify: Optional[bool],
    # )
    # must be last option
    # b.as_package(w3)
    # must be last option
    # b.pin_to_ipfs(backend=infura_backend),
)

print('')
print('Your beautiful manifest')
print('-----------------------')
print(json.dumps(manifest, indent=4))



# 📦
# If you don't want your manifest's version (default) to be your manifest
# filename, replace the `manifest_filename` var with a string of your choice.
manifest_filename = '{0}.json'.format(manifest['version'])
manifest_file = PACKAGE_FOLDER / manifest_filename
manifest_file.write_text(json.dumps(manifest, sort_keys=True, separators=(",",":")))
