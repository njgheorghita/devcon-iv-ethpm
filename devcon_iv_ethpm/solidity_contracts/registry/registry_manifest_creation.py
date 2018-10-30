import json
from pathlib import Path

from ethpm.tools import builder as b
from ethpm.backends.ipfs import InfuraIPFSBackend
from pytest_ethereum.plugins import twig_manifest


# CREATE A MANIFEST FROM YOUR SOLIDITY / VYPER CONTRACTS

# SOLIDITY

# Step 1: Compile the contracts
# Contracts -> SOLC output

# Ingredients
# create a new directory with your package name under `devcon_iv_ethpm/solidity_contracts/`
# Copy and paste your contracts into the directory you just created
# Adjust `/devcon_iv_ethpm/solidity_contracts/sample_solc_standard_json_input.json` to suit your needs (XXX) what to fill in


# TO CREATE YOUR OWN SOLC OUTPUT
# .. instructions .. 
# once everything (contracts/solc_output) is in place

# solc --allow-paths <path-to-contract-directory> --standard-json < standard-json-input.json > owned_compiler_output.json



# COMPILER_OUTPUT_PATH = Path(__file__).parent / 'solidity' / '<solc_output_file_name_here>.json'

SOLIDITY_FOLDER = Path(__file__).parent / 'solidity_contracts' / 'registry'
COMPILER_OUTPUT_PATH = SOLIDITY_FOLDER / 'registry_output.json'

compiler_output = json.loads(COMPILER_OUTPUT_PATH.read_text())['contracts']

manifest = b.build(
    {},
    b.package_name("escrow"),
    b.version("1.0.0"),
    b.manifest_version("2"),
    b.pin_source("IndexedOrderedSetLib", compiler_output, InfuraIPFSBackend(), SOLIDITY_FOLDER),
    b.pin_source("Owned", compiler_output, InfuraIPFSBackend(), SOLIDITY_FOLDER),
    b.pin_source("PackageDB", compiler_output, InfuraIPFSBackend(), SOLIDITY_FOLDER),
    b.pin_source("PackageRegistry", compiler_output, InfuraIPFSBackend(), SOLIDITY_FOLDER),
    b.pin_source("PackageRegistryInterface", compiler_output, InfuraIPFSBackend(), SOLIDITY_FOLDER),
    b.pin_source("ReleaseDB", compiler_output, InfuraIPFSBackend(), SOLIDITY_FOLDER),
    b.pin_source("ReleaseValidator", compiler_output, InfuraIPFSBackend(), SOLIDITY_FOLDER),
    b.contract_type("IndexedOrderedSetLib", compiler_output),
    b.contract_type("Owned", compiler_output),
    b.contract_type("PackageDB", compiler_output),
    b.contract_type("PackageRegistry", compiler_output),
    b.contract_type("PackageRegistryInterface", compiler_output),
    b.contract_type("ReleaseDB", compiler_output),
    b.contract_type("ReleaseValidator", compiler_output),
)

print('')
print('Your beautiful manifest')
print('-----------------------')
print(json.dumps(manifest, indent=4))



# 📦
# If you don't want your manifest's version (default) to be your manifest
# filename, replace the `manifest_filename` var with a string of your choice.
manifest_filename = '{0}.json'.format(manifest['version'])
manifest_file = SOLIDITY_FOLDER / manifest_filename
manifest_file.write_text(json.dumps(manifest, sort_keys=True, separators=(",",":")))

