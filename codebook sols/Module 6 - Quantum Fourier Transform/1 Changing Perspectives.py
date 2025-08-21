import pennylane
import numpy as np

# Exercise F1.1
def coefficients_to_values(coefficients):
    """Returns the value representation of a polynomial
    
    Args:
        coefficients (array[complex]): a 1-D array of complex 
            coefficients of a polynomial with 
            index i representing the i-th degree coefficient

    Returns: 
        array[complex]: the value representation of the 
            polynomial 
    """
    coefficients = np.asarray(coefficients, dtype=complex)
    return np.fft.fft(coefficients)

A = [4, 3, 2, 1]
print(coefficients_to_values(A))

# Exercise F1.2
def values_to_coefficients(values):
    """Returns the coefficient representation of a polynomial
    
    Args:
        values (array[complex]): a 1-D complex array with 
            the value representation of a polynomial 

    Returns: 
        array[complex]: a 1-D complex array of coefficients
    """
    
    return np.fft.ifft(values)


A = [10.+0.j,  2.-2.j,  2.+0.j,  2.+2.j]
print(values_to_coefficients(A))

# Exercise F1.3
def nearest_power_of_2(x):
    """Given an integer, return the nearest power of 2. 
    
    Args:
        x (int): a positive integer

    Returns: 
        int: the nearest power of 2 of x
    """
    return 1 << (x - 1).bit_length()

# Exercise F1.3
def fft_multiplication(poly_a, poly_b):
    """Returns the result of multiplying two polynomials
    
    Args:
        poly_a (array[complex]): 1-D array of coefficients 
        poly_b (array[complex]): 1-D array of coefficients 

    Returns: 
        array[complex]: complex coefficients of the product
            of the polynomials
    """
    required_points = (len(poly_a) - 1) + (len(poly_b) - 1) + 1

    # Figure out the nearest power of 2 for FFT efficiency.
    n = nearest_power_of_2(required_points)

    # Pad both polynomials with zeros to match the FFT size 'n'.
    padded_a = np.pad(poly_a, (0, n - len(poly_a)))
    padded_b = np.pad(poly_b, (0, n - len(poly_b)))

    # Convert the padded polynomials to their value representation.
    values_a = coefficients_to_values(padded_a)
    values_b = coefficients_to_values(padded_b)

    # Multiply the value representations element-wise.
    product_values = values_a * values_b

    # Convert the result back to coefficient representation.
    product_coeffs = values_to_coefficients(product_values)

    return product_coeffs
