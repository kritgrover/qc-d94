import pennylane as qml
import numpy as np

# Exercise 6.1
n_bits = 4
dev = qml.device("default.qubit", wires=n_bits)

@qml.qnode(dev)
def multisol_hoh_circuit(combos):
    """A circuit which applies Hadamard, multi-solution oracle, then Hadamard.
    
    Args:
        combos (list[list[int]]): A list of secret bit strings.

    Returns: 
        array[float]: Probabilities for observing different outcomes.
    """
    for i in range(n_bits):
        qml.H(i)
    qml.QubitUnitary(multisol_oracle_matrix(combos), range(n_bits))
    for i in range(n_bits):
        qml.H(i)
    return qml.probs(wires=range(n_bits))

# Exercise 6.2
def deutsch_jozsa(promise_var):
    """Implement the Deutsch–Jozsa algorithm and guess the promise variable.
    
    Args:
        promise_var (int): Indicates whether the function is balanced (0) or constant (1).
        
    Returns: 
        int: A guess at the promise variable.
    """
    if promise_var == 0:
        how_many = 2**(n_bits - 1)
    else:
        how_many = np.random.choice([0, 2**n_bits]) # Choose all or nothing randomly
    combos = multisol_combo(n_bits, how_many) # Generate random combinations
    if np.isclose(multisol_hoh_circuit(combos)[0],0):
        return 0
    else:
        return 1