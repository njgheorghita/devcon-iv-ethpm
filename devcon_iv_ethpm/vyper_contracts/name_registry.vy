# Example contract, safe to delete
registry: address[bytes[100]]


@public
def register(name: bytes[100], owner: address):
    assert self.registry[name] == ZERO_ADDRESS  # check name has not been set yet.
    self.registry[name] = owner


@public
@constant
def lookup(name: bytes[100]) -> address:
    return self.registry[name]
