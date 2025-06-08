import pennylane as qml
import numpy as np

# Exercise 1.12.1
num_wires = 2
dev = qml.device("default.qubit", wires=num_wires)

@qml.qnode(dev)
def apply_cnot(basis_id):
    """Apply a CNOT to |basis_id>.

    Args:
        basis_id (int): An integer value identifying the basis state to construct.

    Returns:
        np.array[complex]: The resulting state after applying CNOT|basis_id>.
    """
    bits = [int(x) for x in np.binary_repr(basis_id, width=num_wires)]
    qml.BasisState(bits, wires=[0, 1])

    qml.CNOT(wires=[0,1])
    return qml.state()

cnot_truth_table = {"00": "00", "01": "01", "10": "11", "11": "10"}

print(apply_cnot(0))

# Exercise 1.12.2
dev = qml.device("default.qubit", wires=2)

@qml.qnode(dev)
def apply_h_cnot():

    qml.H(0)
    qml.CNOT([0,1])
    return qml.state()


print(apply_h_cnot())
state_status = "entangled"

# Exercise 1.12.3
dev = qml.device("default.qubit", wires=3)

@qml.qnode(dev)
def controlled_rotations(theta, phi, omega):
    """Implement the circuit above and return measurement outcome probabilities.

    Args:
        theta (float): A rotation angle
        phi (float): A rotation angle
        omega (float): A rotation angle

    Returns:
        np.array[float]: Measurement outcome probabilities of the 3-qubit
        computational basis states.
    """
    qml.H(0)
    qml.CRX(theta, [0,1])
    qml.CRY(phi, [1,2])
    qml.CRZ(omega, [2,0])
    return qml.probs(range(3))

theta, phi, omega = 0.1, 0.2, 0.3
print(controlled_rotations(theta, phi, omega))