# ElGamal Algorithm

p = 23
g = 5
x = 6

y = pow(g, x, p)

# Encryption
msg = 10
k = 3

a = pow(g, k, p)
b = (msg * pow(y, k, p)) % p

print("Encrypted:", a, b)

# Decryption
s = pow(a, x, p)
plain = (b * pow(s, -1, p)) % p

print("Decrypted:", plain)