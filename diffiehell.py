
# Diffie-Hellman Key Exchange

# Publicly shared values
p = 23  # Prime number
g = 5   # Generator

# Private keys of Alice and Bob
a = 6   # Alice's private key
b = 15  # Bob's private key

# Calculate public keys
A = (g ** a) % p
B = (g ** b) % p

print("Alice's public key:", A)
print("Bob's public key:", B)

# Calculate shared secret key
alice_key = (B ** a) % p
bob_key = (A ** b) % p

print("Alice's shared key:", alice_key)
print("Bob's shared key:", bob_key)

# Verify the keys
if alice_key == bob_key:
    print("Key exchange successful!")
else:
    print("Key exchange failed!")
