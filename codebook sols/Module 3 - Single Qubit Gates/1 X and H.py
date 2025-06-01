import pennylane as qml
import numpy as np

# Exercise 1.4.1
dev = qml.device("default.qubit", wires=1)
U = np.array([[1, 1], [1, -1]]) / np.sqrt(2)

@qml.qnode(dev)
def varied_initial_state(state):
    """Complete the function such that we can apply the operation U to
    either |0> or |1> depending on the input argument flag.

    Args:
        state (int): Either 0 or 1. If 1, prepare the qubit in state |1>,
            otherwise, leave it in state 0.

    Returns:
        np.array[complex]: The state of the qubit after the operations.
    """
    if state==1:
        qml.X(wires=0)
    qml.QubitUnitary(U, wires=0)
    return qml.state()

# Exercise 1.4.2
dev = qml.device("default.qubit", wires=1)

@qml.qnode(dev)
def apply_hadamard():
    qml.H(wires=0)
    return qml.state()

# Exercise 1.4.3
dev = qml.device("default.qubit", wires=1)

@qml.qnode(dev)
def apply_hadamard_to_state(state):
    """Complete the function such that we can apply the Hadamard to
    either |0> or |1> depending on the input argument flag.

    Args:
        state (int): Either 0 or 1. If 1, prepare the qubit in state |1>,
            otherwise, leave it in state 0.

    Returns:
        np.array[complex]: The state of the qubit after the operations.
    """
    if state==1:
        qml.X(wires=0)
    qml.H(wires=0)

    return qml.state()

print(apply_hadamard_to_state(0))
print(apply_hadamard_to_state(1))

# Exercise 1.4.4
dev = qml.device("default.qubit", wires=1)

@qml.qnode(dev)
def apply_hxh(state):
    if state == 1:
        qml.X(wires=0)
    qml.H(wires=0)
    qml.X(wires=0)
    qml.H(wires=0)
    return qml.state()

print(apply_hxh(0))
print(apply_hxh(1))
