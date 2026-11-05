text = "HELLO"

key = "QWERTYUIOPASDFGHJKLZXCVBNM"

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

encrypted = ""

for char in text:
    if char.isupper():
        encrypted += key[alphabet.index(char)]
    else:
        encrypted += char

print("Original Text:", text)
print("Encrypted Text:", encrypted)

decrypted = ""

for char in encrypted:
    if char.isupper():
        decrypted += alphabet[key.index(char)]
    else:
        decrypted += char

print("Decrypted Text:", decrypted)