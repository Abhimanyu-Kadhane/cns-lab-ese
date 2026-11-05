import random

def miller_rabin(n, k=5):
    if n < 2:
        return False

    if n == 2 or n == 3:
        return True

    if n % 2 == 0:
        return False

    # Write n-1 as 2^r * d
    d = n - 1
    r = 0

    while d % 2 == 0:
        d //= 2
        r += 1

    # Perform k rounds
    for i in range(k):
        a = random.randint(2, n - 2)

        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for j in range(r - 1):
            x = pow(x, 2, n)

            if x == n - 1:
                break
        else:
            return False

    return True


# Input
n = 17

# Check primality
if miller_rabin(n):
    print(n, "is probably prime")
else:
    print(n, "is composite")