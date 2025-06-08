import pennylane as qml
import numpy as np

# Exercise 1.8.1
dev = qml.device("default.qubit", wires=1)

@qml.qnode(dev)
def prepare_state():

    qml.H(wires=0)
    qml.Z(wires=0)
    qml.T(wires=0)
    return qml.state()

# Exercise 1.8.2
dev = qml.device("default.qubit", wires=1)

@qml.qnode(dev)
def prepare_state():

    qml.RX(np.pi/3, wires=0)
    return qml.state()

# Exercise 1.8.3
v = np.array([0.52889389 - 0.14956775j, 0.67262317 + 0.49545818j])
dev = qml.device("default.qubit", wires=1)

@qml.qnode(dev)
def prepare_state(state=v):
    qml.MottonenStatePreparation(v, wires=0)
    return qml.state()

print(prepare_state(v))
print()
print(qml.draw(prepare_state, level="device")(v))
