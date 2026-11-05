text = "HELLO"
key = "KEY"

encrypted = ""
decrypted = ""

# Encryption
for i in range(len(text)):
    p = ord(text[i]) - 65
    k = ord(key[i % len(key)]) - 65

    encrypted += chr((p + k) % 26 + 65)

print("Original Text:", text)
print("Encrypted Text:", encrypted)

# Decryption
for i in range(len(encrypted)):
    c = ord(encrypted[i]) - 65
    k = ord(key[i % len(key)]) - 65

    decrypted += chr((c - k) % 26 + 65)

print("Decrypted Text:", decrypted)