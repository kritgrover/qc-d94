import pennylane as qml
import numpy as np

# Exercise G1.1
n_bits = 4
dev = qml.device("default.qubit", wires=n_bits)

def oracle_matrix(combo):
    """Return the oracle matrix for a secret combination.

    Args:
        combo (list[int]): A list of bits representing a secret combination.

    Returns:
        array[float]: The matrix representation of the oracle.
    """
    index = np.ravel_multi_index(combo, [2] * len(combo))  # Index of solution
    my_array = np.identity(2 ** len(combo))  # Create the identity matrix
    my_array[index, index] = -1
    return my_array

@qml.qnode(dev)
def oracle_amp(combo):
    """Prepare the uniform superposition and apply the oracle.

    Args:
        combo (list[int]): A list of bits representing the secret combination.

    Returns:
        array[complex]: The quantum state (amplitudes) after applying the oracle.
    """
    for i in range(n_bits):
        qml.Hadamard(wires=i)
    
    # Apply the oracle
    qml.QubitUnitary(oracle_matrix(combo), wires=range(n_bits))
    
    return qml.state()

# Exercise G1.2
def diffusion_matrix():
    """Return the diffusion matrix.
    
    Returns:
        array[float]: The matrix representation of the diffusion operator.
    """
    n_qubits = n_bits
    identity = np.identity(2**n_qubits)
    ones_matrix = np.ones((2**n_qubits, 2**n_qubits))
    
    return (2 / (2**n_qubits)) * ones_matrix - identity


@qml.qnode(dev)
def difforacle_amp(combo):
    """Apply the oracle and diffusion matrix to the uniform superposition.

    Args:
        combo (list[int]): A list of bits representing the secret combination.

    Returns:
        array[complex]: The quantum state (amplitudes) after applying the oracle
        and diffusion.
    """
    for i in range(n_bits):
        qml.Hadamard(wires=i)
        
    qml.QubitUnitary(oracle_matrix(combo), wires=range(n_bits))
    
    qml.QubitUnitary(diffusion_matrix(), wires=range(n_bits))
    
    return qml.state()

# Exercise G1.3
@qml.qnode(dev)
def two_difforacle_amp(combo):
    """Apply the Grover operator twice to the uniform superposition.

    Args:
        combo (list[int]): A list of bits representing the secret combination.

    Returns:
        array[complex]: The resulting quantum state.
    """
    for i in range(n_bits):
        qml.Hadamard(wires=i)
    
    for _ in range(2):
        qml.QubitUnitary(oracle_matrix(combo), wires=range(n_bits))
        qml.QubitUnitary(diffusion_matrix(), wires=range(n_bits))
        
    return qml.state()