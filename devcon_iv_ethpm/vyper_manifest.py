import json
from pathlib import Path
from pytest_ethereum.plugins import twig_manifest

from devcon_iv_ethpm.constants import VYPER_FOLDER, MANIFEST_FOLDER



# Running this script will ...
# - 
# - 
# -


# 📦
# This symbol represents ... 


# lookup .vy in `vyper_contracts` raise error if none found


# 📦
# If you'd like to create your manifest with a different name or version
# replace the strings below before running this script
manifest = twig_manifest(VYPER_FOLDER, name="devcon-iv-ethpm", version="1.0.0")


print('')
print('Your beautiful manifest')
print('-----------------------')
print(json.dumps(manifest, indent=4))


# 📦
# If you don't want your manifest's version (default) to be your manifest
# filename, replace the `manifest_filename` var with a string of your choice.
manifest_filename = '{0}.json'.format(manifest['version'])
manifest_file = MANIFEST_FOLDER / manifest_filename
manifest_file.write_text(json.dumps(manifest, sort_keys=True, separators=(",",":")))

print('💰⭐️💰⭐️💰⭐️💰⭐️')
print('')
print("Manifest: {0} written to {1}/{2}".format(manifest['package_name'], MANIFEST_FOLDER, manifest_filename))
print('')
print('💰⭐️💰⭐️💰⭐️💰⭐️')
