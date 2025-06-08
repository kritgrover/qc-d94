import pennylane as qml
import numpy as np

# Exercise 1.7.1
dev = qml.device("default.qubit", wires=1)

phi = np.pi/2
theta= np.pi/2
omega = np.pi/2

@qml.qnode(dev)
def hadamard_with_rz_rx():
    qml.RZ(phi, wires=0)
    qml.RX(theta, wires=0)
    qml.RZ(omega, wires=0)
    return qml.state()

# Exercise 1.7.2
dev = qml.device("default.qubit", wires=1)

@qml.qnode(dev)
def convert_to_rz_rx():

    qml.RZ(np.pi, wires=0)
    qml.RX(np.pi/2, wires=0)
    qml.RZ(np.pi, wires=0)
    qml.RZ(np.pi/2, wires=0)
    qml.RZ(-np.pi/4, wires=0)
    qml.RZ(np.pi, wires=0)
    qml.RX(np.pi, wires=0)
    return qml.state()

# Exercise 1.7.3
dev = qml.device("default.qubit", wires=1)

@qml.qnode(dev)
def unitary_with_h_and_t():

    qml.H(wires=0)
    qml.T(wires=0)
    qml.H(wires=0)
    qml.T(wires=0)
    qml.T(wires=0)
    qml.H(wires=0)
    return qml.state()