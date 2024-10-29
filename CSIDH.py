from sibc.csidh import CSIDH, default_parameters
csidh = CSIDH(**default_parameters)

# alice generates a key
alice_secret_key = csidh.secret_key()
alice_public_key = csidh.public_key(alice_secret_key)

# bob generates a key
bob_secret_key = csidh.secret_key()
bob_public_key = csidh.public_key(bob_secret_key)

# if either alice or bob use their secret key with the other's respective
# public key, the resulting shared secrets are the same
shared_secret_alice = csidh.dh(alice_secret_key, bob_public_key)
shared_secret_bob = csidh.dh(bob_secret_key, alice_public_key)

print(shared_secret_alice, shared_secret_bob)

# Alice and bob produce an identical shared secret
assert shared_secret_alice == shared_secret_bob