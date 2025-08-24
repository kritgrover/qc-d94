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
