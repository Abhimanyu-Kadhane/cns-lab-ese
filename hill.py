import numpy as np

text = "HELP"

key = [[3, 3],
       [2, 5]]

encrypted = ""

# Encryption
for i in range(0, len(text), 2):
    a = ord(text[i]) - 65
    b = ord(text[i+1]) - 65

    c1 = (key[0][0]*a + key[0][1]*b) % 26
    c2 = (key[1][0]*a + key[1][1]*b) % 26

    encrypted += chr(c1 + 65) + chr(c2 + 65)

print("Original Text:", text)
print("Encrypted Text:", encrypted)

# Decryption
det = (key[0][0]*key[1][1] - key[0][1]*key[1][0]) % 26
det_inv = pow(det, -1, 26)

inverse = [
    [(key[1][1]*det_inv) % 26, (-key[0][1]*det_inv) % 26],
    [(-key[1][0]*det_inv) % 26, (key[0][0]*det_inv) % 26]
]

decrypted = ""

for i in range(0, len(encrypted), 2):
    a = ord(encrypted[i]) - 65
    b = ord(encrypted[i+1]) - 65

    p1 = (inverse[0][0]*a + inverse[0][1]*b) % 26
    p2 = (inverse[1][0]*a + inverse[1][1]*b) % 26

    decrypted += chr(p1 + 65) + chr(p2 + 65)

print("Decrypted Text:", decrypted)