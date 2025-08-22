import pennylane as qml
import numpy as np

# Exercise F3.1
num_wires = 3
dev = qml.device("default.qubit", wires=num_wires)

@qml.qnode(dev)
def three_qubit_QFT(basis_id):
    """A circuit that computes the QFT on three qubits.
    
    Args:
        basis_id (int): An integer value identifying the basis state to construct.
        
    Returns:
        array[complex]: The state of the qubits after the QFT operation.
    """
    bits = [int(x) for x in np.binary_repr(basis_id, width=num_wires)]
    qml.BasisState(bits, wires=[0, 1, 2])

    # Decompose the QFT into elementary gates    
    qml.Hadamard(wires=0)
    qml.ctrl(qml.S, control=1)(wires=0)
    qml.ctrl(qml.T, control=2)(wires=0)

    # --- Operations on qubit 1 ---
    qml.Hadamard(wires=1)
    qml.ctrl(qml.S, control=2)(wires=1)

    # --- Operations on qubit 2 ---
    qml.Hadamard(wires=2)

    # --- Final SWAP layer ---
    qml.SWAP(wires=[0, 2])

    return qml.state()

# Exercise F3.2
def swap_bits(n_qubits):
    """A circuit that reverses the order of qubits, i.e.,
    performs a SWAP such that [q1, q2, ..., qn] -> [qn, ... q2, q1].
    
    Args:
        n_qubits (int): An integer value identifying the number of qubits.
    """
    for i in range(n_qubits // 2):
        qml.SWAP(wires=[i, n_qubits - i - 1])

# Exercise F3.3
def qft_rotations(n_qubits):
    """A circuit performs the QFT rotations on the specified qubits.
    
    Args:
        n_qubits (int): An integer value identifying the number of qubits.
    """
    for i in range(n_qubits):
        # 1. Apply the Hadamard gate to the target qubit i
        qml.Hadamard(wires=i)
        
        # 2. Apply controlled phase rotations to qubit i
        for j in range(i + 1, n_qubits):
            # The angle is pi / 2^(k) where k is the distance between qubits
            k = j - i
            phase = np.pi / (2**k)
            # Apply the controlled phase shift gate.
            qml.ControlledPhaseShift(phase, wires=[j, i])

# Exercise F3.4
def qft_recursive_rotations(n_qubits, wire=0):
    """A circuit that performs the QFT rotations on the specified qubits
        recursively.
        
    Args:
        n_qubits (int): An integer value identifying the number of qubits.
        wire (int): An integer identifying the wire 
                    (or the qubit) to apply rotations on.
    """

    if n_qubits == 1:
        qml.Hadamard(wires=wire)
        return

    # 1. Apply Hadamard to the current wire
    qml.Hadamard(wires=wire)

    # 2. Apply controlled rotations from subsequent qubits to the current wire
    for i in range(1, n_qubits):
        control_wire = wire + i
        phase = np.pi / (2**i)
        qml.ControlledPhaseShift(phase, wires=[control_wire, wire])

    qft_recursive_rotations(n_qubits - 1, wire + 1)

# Exercise F3.5
dev = qml.device('default.qubit', wires=4)

@qml.qnode(dev)
def pennylane_qft(basis_id, n_qubits):
    """A that circuit performs the QFT using PennyLane's QFT template.
    
    Args:
        basis_id (int): An integer value identifying 
            the basis state to construct.
        n_qubits (int): An integer identifying the 
            number of qubits.
            
    Returns:
        array[complex]: The state after applying the QFT to the qubits.
    """
    # Prepare the basis state |basis_id>
    bits = [int(x) for x in np.binary_repr(basis_id, width=n_qubits)]
    qml.BasisState(bits, wires=range(n_qubits))

    qml.QFT(wires=range(n_qubits))
    return qml.state()