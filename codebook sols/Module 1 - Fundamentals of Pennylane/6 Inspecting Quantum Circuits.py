import pennylane as qml

# Exercise PF6.1
dev = qml.device("default.qubit", wires=3)


@qml.qnode(dev)
def circuit():
    """
    Implements a circuit and returns the state
    """
    qml.Hadamard(wires=0)
    qml.CRY(np.pi / 4, wires=(0, 1))
    qml.CRX(np.pi / 3, wires=(1, 2))
    qml.S(wires=1)
    qml.T(wires=2)
    qml.Toffoli(wires=(0, 1, 2))
    qml.SWAP(wires=(0, 2))
    return qml.state()


qml.draw(dev)

# Exercise PF6.2
dev = qml.device("default.qubit", wires=3)


@qml.qnode(dev)
def circuit():
    """
    Implements a circuit and returns the state
    """
    qml.Hadamard(wires=0)
    qml.CRY(np.pi / 4, wires=(0, 1))
    qml.CRX(np.pi / 3, wires=(1, 2))
    qml.Snapshot("very_important_state")
    qml.S(wires=1)
    qml.T(wires=2)
    qml.Toffoli(wires=(0, 1, 2))
    qml.Snapshot(measurement=qml.expval(qml.Z(0)))
    qml.SWAP(wires=(0, 2))
    return qml.state()


for key, val in qml.snapshots(circuit)().items(): print(key, val)
