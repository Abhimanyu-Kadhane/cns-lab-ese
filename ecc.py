
# Elliptic Curve Cryptography (ECC)

p = 17
a = 2
G = (5, 1)  # Generator point

# Point addition
def add(P, Q):
    if P is None: return Q
    if Q is None: return P

    x1, y1 = P
    x2, y2 = Q

    if x1 == x2 and (y1 + y2) % p == 0:
        return None

    if P == Q:
        m = (3*x1*x1 + a) * pow(2*y1, p-2, p) % p
    else:
        m = (y2-y1) * pow((x2-x1) % p, p-2, p) % p

    x3 = (m*m - x1 - x2) % p
    y3 = (m*(x1-x3) - y1) % p

    return (x3, y3)

# Scalar multiplication
def multiply(k, P):
    R = None
    while k:
        if k & 1:
            R = add(R, P)
        P = add(P, P)
        k >>= 1
    return R

# Private keys
alice = 5
bob = 7

# Public keys
A = multiply(alice, G)
B = multiply(bob, G)

# Shared secret keys
key1 = multiply(alice, B)
key2 = multiply(bob, A)

print("Alice's public key:", A)
print("Bob's public key:", B)
print("Alice's shared key:", key1)
print("Bob's shared key:", key2)

if key1 == key2:
    print("ECC Key Exchange Successful!")
