import pennylane as qml
import numpy as np

# Exercise 5.1
n_bits = 4
dev = qml.device("default.qubit", wires=n_bits)

@qml.qnode(dev)
def hoh_circuit(combo):
    """A circuit which applies Hadamard-oracle-Hadamard and returns probabilities.
    
    Args:
        combo (list[int]): A list of bits representing a secret combination.

    Returns:
        list[float]: Measurement outcome probabilities.
    """

    for i in range(n_bits):
        qml.H(i)
    qml.QubitUnitary(oracle_matrix(combo), range(n_bits))
    for i in range(n_bits):
        qml.H(i)
    return qml.probs(wires=range(n_bits))

