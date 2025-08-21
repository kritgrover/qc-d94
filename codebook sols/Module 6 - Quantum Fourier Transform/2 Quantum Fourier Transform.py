import pennylane as qml
import numpy as np

# Exercise F2.1
num_wires = 1
dev = qml.device("default.qubit", wires=num_wires)

@qml.qnode(dev)
def one_qubit_QFT(basis_id):
    """A circuit that computes the QFT on a single qubit. 
    
    Args:
        basis_id (int): An integer value identifying 
            the basis state to construct.
    
    Returns:
        array[complex]: The state of the qubit after applying QFT.
    """
    # Prepare the basis state |basis_id>
    bits = [int(x) for x in np.binary_repr(basis_id, width=num_wires)]
    qml.BasisState(bits, wires=[0])

    qml.Hadamard(wires=0)
    return qml.state()

# Exercise F2.2
num_wires = 2
dev = qml.device("default.qubit", wires=num_wires)

@qml.qnode(dev)
def two_qubit_QFT(basis_id):
    """A circuit that computes the QFT on two qubits using qml.QubitUnitary. 
    
    Args:
        basis_id (int): An integer value identifying the basis state to construct.
    
    Returns:
        array[complex]: The state of the qubits after the QFT operation.
    """
    
    # Prepare the basis state |basis_id>
    bits = [int(x) for x in np.binary_repr(basis_id, width=num_wires)]
    qml.BasisState(bits, wires=[0, 1])
    
    qft_matrix = 0.5 * np.array([
        [1,  1,  1,  1],
        [1,  1j, -1, -1j],
        [1, -1,  1, -1],
        [1, -1j, -1,  1j]
    ])

    qml.QubitUnitary(qft_matrix, wires=[0, 1])

    return qml.state()

# Exercise F2.3
num_wires = 2
dev = qml.device("default.qubit", wires=num_wires)

@qml.qnode(dev)
def decompose_two_qubit_QFT(basis_id):
    """A circuit that computes the QFT on two qubits using elementary gates.
    
    Args:
        basis_id (int): An integer value identifying the basis state to construct.
    
    Returns:
        array[complex]: The state of the qubits after the QFT operation.
    """
    # Prepare the basis state |basis_id>
    bits = [int(x) for x in np.binary_repr(basis_id, width=num_wires)]
    qml.BasisState(bits, wires=[0, 1])
    
    # 1. Apply Hadamard to the first qubit
    qml.Hadamard(wires=0)

    # 2. Apply a controlled-S gate
    # The S gate is a phase shift of pi/2. We control it with qubit 0.
    qml.ctrl(qml.S, control=0)(wires=1)

    # 3. Apply Hadamard to the second qubit
    qml.Hadamard(wires=1)

    # 4. Swap the qubits to reverse their order
    qml.SWAP(wires=[0, 1])
    
    return qml.state()