import pennylane as qml
import numpy as np

# Exercise S1.1
def is_equivalent(a, b, m):
    """Return a boolean indicating whether the equivalence is satisfied.

    Args:
        a (int): First number to check the equivalence.
        b (int): Second number to check the equivalence.
        m (int): Modulus of the equivalence.

    Returns:
        bool: True if a = b (m), False otherwise.
    """

    return (a - b) % m == 0


print(f"13 = 8 (3) is {is_equivalent(13, 8, 3)}")
print(f"13 = 7 (6) is {is_equivalent(13, 7, 6)}")

# Exercise S1.2
def has_inverse(a, m):
    """Returns a boolean indicating whether a number has an inverse modulo m.

    Args:
        a (int): Number to find the inverse modulus m.
        m (int): Modulus of the equivalence.

    Returns:
        bool: True if c exists (ac = 1 (m)), False otherwise
    """

    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    
    return gcd(a, m) == 1


print("(5,15)", has_inverse(5, 15))
print("(7,15)", has_inverse(7, 15))