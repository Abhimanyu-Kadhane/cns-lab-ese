import random

def fermat_test(n, k=5):
    if n <= 1:
        return False

    for i in range(k):
        a = random.randint(2, n - 2)

        if pow(a, n - 1, n) != 1:
            return False

    return True


# Input
n = 17

# Check primality
if fermat_test(n):
    print(n, "is probably prime")
else:
    print(n, "is composite")


# How it works:
# 1. Fermat's Little Theorem states that if n is prime, then \(a^{n-1} \mod n = 1\), where a and n are coprime.
# 2. We randomly select k values of a.
# 3. If even one test fails, n is composite.
# 4. If all tests pass, n is probably prime.

# Note: Fermat Test can incorrectly classify Carmichael numbers (like 561) as prime. 
# Hence, the result is called probably prime, not definitely prime.