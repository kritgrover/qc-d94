# Exercise S4.1
def is_coprime(a, N):
    """Determine if two numbers are coprime.

    Args:
        a (int): First number to check if is coprime with the other.
        N (int): Second number to check if is coprime with the other.

    Returns:
        bool: True if they are coprime numbers, False otherwise.
    """
    def gcd(x, y):
        while y != 0:
            x, y = y, x % y
        return x
    
    return gcd(a, N) == 1


def is_odd(r):
    """Determine if a number is odd.

    Args:
        r (int): Integer to check if is an odd number.

    Returns:
        bool: True if it is odd, False otherwise.
    """
    return r % 2 == 1


def is_not_one(x, N):
    """Determine if x is not +- 1 modulo N.

    Args:
        N (int): Modulus of the equivalence.
        x (int): Integer to check if it is different from +-1 modulo N.

    Returns:
        bool: True if it is different, False otherwise.
    """
    return (x % N != 1) and (x % N != N-1)


print("3 and 12 are coprime numbers: ", is_coprime(3, 12))
print("5 is odd: ", is_odd(5))
print("4 is not one mod 5: ", is_not_one(4, 5))

# Exercise S4.2
def gcd(a, b):
    """Calculate the Greatest Common Divisor using Euclidean algorithm."""
    while b != 0:
        a, b = b, a % b
    return a

def shor(N):
    """Return the factorization of a given integer.

    Args:
        N (int): integer we want to factorize.

    Returns:
        array[int]: [p, q], the prime factors of N.
    """
    a = 2
    attempt = 0
    
    while True:
        a = (a * 7 + 3) % (N - 3) + 2
        
        if not is_coprime(a, N):
            p = gcd(a, N)
            q = N // p
            return [p, q]
        
        matrix = get_matrix_a_mod_N(a, N)
        r = get_period(matrix, N)
        
        if is_odd(r):
            attempt += 1
            if attempt > 10:
                return None
            continue
        
        x = pow(a, r // 2, N)
        
        if is_not_one(x, N):
            p = gcd(x - 1, N)
            q = gcd(x + 1, N)
            if p > 1 and q > 1 and p < N and q < N:
                return [p, q]
        
        attempt += 1
        if attempt > 10:
            return None

print(shor(21))
