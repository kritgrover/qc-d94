import pennylane as qml
import numpy as np

# Exercise S2.1
def nontrivial_square_root(m):
    """Return the first nontrivial square root modulo m.

    Args:
        m (int): modulus for which want to find the nontrivial square root

    Returns:
        int: the first nontrivial square root of m
    """

    for x in range(2, m):
        if (x * x) % m == 1:
            return x
    return None


print(nontrivial_square_root(391))


# Exercise S2.2
def gcd(a, b):
    """Compute the greatest common divisor of a and b using Euclidean algorithm."""
    while b != 0:
        a, b = b, a % b
    return a

def factorization(N):
    """Return the factors of N.

    Args:
        N (int): number we want to factor.

    Returns:
        array[int]: [p, q] factors of N.
    """
    x = nontrivial_square_root(N)
    if x is None:
        return None

    p = gcd(x - 1, N)
    q = gcd(x + 1, N)

    return [p, q]

N = 391
p, q = factorization(N)
print(f"{N} = {p} x {q}")

