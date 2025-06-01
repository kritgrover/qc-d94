import pennylane as qml
import numpy as np

# Exercise 1.3.1
dev = qml.device("default.qubit", wires=1)
U = np.array([[1, 1], [1, -1]]) / np.sqrt(2)

@qml.qnode(dev)
def apply_u():
    qml.QubitUnitary(U, wires=0)
    return qml.state()

# Exercise 1.3.2
dev = qml.device("default.qubit", wires=1)

@qml.qnode(dev)
def apply_u_as_rot(phi, theta, omega):
    qml.Rot(phi, theta, omega, wires=0)
    return qml.state()