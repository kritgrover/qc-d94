import pennylane as qml
import numpy as np

# Exercise 2.1
def oracle_matrix(combo):
    """Return the oracle matrix for a secret combination.
    
    Args:
        combo (list[int]): A list of bits representing a secret combination.
         
    Returns: 
        array[float]: The matrix representation of the oracle.
    """
    index = np.ravel_multi_index(combo, [2]*len(combo)) # Index of solution
    my_array = np.identity(2**len(combo)) # Create the identity matrix

    my_array[index][index] = -1
    return my_array

# Exercise 2.2
n_bits = 4
dev = qml.device("default.qubit", wires=n_bits)

@qml.qnode(dev)
def oracle_circuit(combo):
    """Create a uniform superposition, apply the oracle, and return probabilities.
    
    Args:
        combo (list[int]): A list of bits representing a secret combination.

    Returns:
        list[float]: The output probabilities.
    """
    for i in range(n_bits):
        qml.H(i)
    mat = oracle_matrix(combo)
    qml.QubitUnitary(mat, range(n_bits))
    return qml.probs(wires=range(n_bits))