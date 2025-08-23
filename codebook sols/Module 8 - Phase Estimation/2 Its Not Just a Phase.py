import pennylane as qml
import numpy as np

# Exercise P2.1
def U_power_2k(unitary, k):
    """ Computes U at a power of 2k (U^2^k)
    
    Args: 
        unitary (array[complex]): A unitary matrix
    
    Returns: 
        array[complex]: the unitary raised to the power of 2^k
    """
    power = 2**k
    return np.linalg.matrix_power(unitary, power)
            

# Try out a higher power of U
U = qml.T.compute_matrix()
print(U)

U_power_2k(U, 2)

# Exercise P2.2
estimation_wires = [0, 1, 2]
target_wires = [3]

def apply_controlled_powers_of_U(unitary):
    """A quantum function that applies the sequence of powers of U^2^k to
    the estimation wires.
    
    Args: 
        unitary (array [complex]): A unitary matrix
    """

    n_estimation_wires = len(estimation_wires)
    
    for i, est_wire in enumerate(estimation_wires):
        k = n_estimation_wires - 1 - i
        U_power = U_power_2k(unitary, k)
        all_wires = [est_wire] + target_wires
        qml.ControlledQubitUnitary(U_power, wires=all_wires)

# Exercise P2.3
dev = qml.device("default.qubit", wires=4)

estimation_wires = [0, 1, 2]
target_wires = [3]

def prepare_eigenvector():
    qml.PauliX(wires=target_wires)

@qml.qnode(dev)
def qpe(unitary):
    """ Estimate the phase for a given unitary.
    
    Args:
        unitary (array[complex]): A unitary matrix.
        
    Returns:
        array[float]: Measurement outcome probabilities on the estimation wires.
    """
    for wire in estimation_wires:
        qml.Hadamard(wires=wire)
    
    prepare_eigenvector()
    apply_controlled_powers_of_U(unitary)
    qml.adjoint(qml.QFT)(wires=estimation_wires)
    
    return qml.probs(wires=estimation_wires)
    

U = qml.T.compute_matrix()
print(qpe(U))

# Exercise P2.4
estimation_wires = [0, 1, 2]
target_wires = [3]

def estimate_phase(probs):
    """Estimate the value of a phase given measurement outcome probabilities
    of the QPE routine.
    
    Args: 
        probs (array[float]): Probabilities on the estimation wires.
    
    Returns:
        float: the estimated phase   
    """
    max_idx = np.argmax(probs)
    
    # Convert index to binary representation
    n_estimation_wires = len(estimation_wires)
    bitstring = format(max_idx, f'0{n_estimation_wires}b')
    
    phase = 0
    for i, bit in enumerate(bitstring):
        phase += int(bit) / (2 ** (i + 1))
    
    return phase

U = qml.T.compute_matrix()

probs = qpe(U)


estimated_phase = estimate_phase(probs)
print(estimated_phase)

# Exercise P2.5
dev = qml.device("default.qubit", wires=4)

estimation_wires = [0, 1, 2]
target_wires = [3]

def prepare_eigenvector():
    qml.PauliX(wires=target_wires)

@qml.qnode(dev)
def qpe(unitary):
    """Estimate the phase for a given unitary.
    
    Args:
        unitary (array[complex]): A unitary matrix.
        
    Returns:
        array[float]: Probabilities on the estimation wires.
    """
    
    prepare_eigenvector()
    
    qml.QuantumPhaseEstimation(
        unitary, 
        target_wires=target_wires, 
        estimation_wires=estimation_wires
    )
    
    return qml.probs(wires=estimation_wires)


U = qml.T.compute_matrix()
probs = qpe(U)
print(estimate_phase(probs))
