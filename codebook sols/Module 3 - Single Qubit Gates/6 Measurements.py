import pennylane as qml
import numpy as np

# Exercise 1.9.1
dev = qml.device("default.qubit", wires=1)


@qml.qnode(dev)
def apply_h_and_measure(state):
    """Complete the function such that we apply the Hadamard gate
    and measure in the computational basis.

    Args:
        state (int): Either 0 or 1. If 1, prepare the qubit in state |1>,
            otherwise leave it in state 0.

    Returns:
        np.array[float]: The measurement outcome probabilities.
    """
    if state == 1:
        qml.PauliX(wires=0)

    qml.H(wires=0)
    return qml.probs(wires=0)


print(apply_h_and_measure(0))
print(apply_h_and_measure(1))

# Exercise 1.9.2
def prepare_psi():
    qml.StatePrep(state=[1, np.sqrt(3)], normalize=True, wires=0)
    qml.S(wires=0)

def y_basis_rotation():
    qml.H(wires=0)
    qml.S(wires=0)

# Exercise 1.9.3
dev = qml.device("default.qubit", wires=1)

@qml.qnode(dev)
def measure_in_y_basis():
    prepare_psi()
    qml.adjoint(y_basis_rotation)()
    return qml.probs(wires=0)

print(measure_in_y_basis())