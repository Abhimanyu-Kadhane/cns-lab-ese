# RSA Algorithm

p = 3
q = 11

n = p * q
phi = (p-1) * (q-1)

e = 3
d = pow(e, -1, phi)

# Encryption
msg = 5
cipher = (msg ** e) % n
print("Encrypted:", cipher)

# Decryption
plain = (cipher ** d) % n
print("Decrypted:", plain)