def euler_test(n, k=5):
    if n <= 2:
        return n == 2

    for a in range(2, k + 2):
        if a >= n:
            break

        result = pow(a, (n - 1) // 2, n)

        if result != 1 and result != n - 1:
            return False

    return True


# Input
n = 17

# Check primality
if euler_test(n):
    print(n, "is probably prime")
else:
    print(n, "is composite")


