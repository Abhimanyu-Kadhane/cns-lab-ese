text = "HELLO"
key = "MONARCHY"

# Create 5x5 key matrix
alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
key = key.upper().replace("J", "I")

matrix_text = ""

for char in key + alphabet:
    if char not in matrix_text:
        matrix_text += char

matrix = [list(matrix_text[i:i+5]) for i in range(0, 25, 5)]

print("Key Matrix:")
for row in matrix:
    print(row)

# Prepare plaintext
text = text.upper().replace("J", "I")
prepared = ""
i = 0

while i < len(text):
    a = text[i]

    if i + 1 == len(text):
        prepared += a + "X"
        i += 1
    elif text[i] == text[i+1]:
        prepared += a + "X"
        i += 1
    else:
        prepared += a + text[i+1]
        i += 2

# Encryption
encrypted = ""

for i in range(0, len(prepared), 2):
    a, b = prepared[i], prepared[i+1]

    for r in range(5):
        for c in range(5):
            if matrix[r][c] == a:
                r1, c1 = r, c
            if matrix[r][c] == b:
                r2, c2 = r, c

    if r1 == r2:
        encrypted += matrix[r1][(c1+1) % 5]
        encrypted += matrix[r2][(c2+1) % 5]

    elif c1 == c2:
        encrypted += matrix[(r1+1) % 5][c1]
        encrypted += matrix[(r2+1) % 5][c2]

    else:
        encrypted += matrix[r1][c2]
        encrypted += matrix[r2][c1]

print("Original Text:", text)
print("Prepared Text:", prepared)
print("Encrypted Text:", encrypted)