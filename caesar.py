text = "HELLO"
key = 3

encrypted = ""

for char in text:
    if char.isupper():
        encrypted += chr((ord(char) - 65 + key) % 26 + 65)
    else:
        encrypted += char

print("Original Text:", text)
print("Encrypted Text:", encrypted)

decrypted = ""

for char in encrypted:
    if char.isupper():
        decrypted += chr((ord(char) - 65 - key) % 26 + 65)
    else:
        decrypted += char

print("Decrypted Text:", decrypted)