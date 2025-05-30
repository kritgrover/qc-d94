import pennylane as qml
import numpy as np

# Exercise 3.1
dev = qml.device("default.qubit", wires = 2, shots =1)# Define a two-qubit device here

@qml.qnode(dev)
def circuit():
    """
    This quantum function implements the circuit shown above
    and should return a sample from all qubits
    """

    qml.H(wires=0)
    qml.CNOT(wires=[0,1])

    return qml.sample()

# Exercise 3.2
dev = qml.device("default.qubit", wires = 2) # Define a two-qubit device here
A = np.array([[1, 0], [0, -1]])

@qml.qnode(dev)
def circuit():
    """
    This quantum function implements a Bell state and
    should return the expectation value the observable
    corresponding to the matrix A applied to the first qubit
    """
    qml.H(wires=0)
    qml.CNOT(wires=[0,1])
    return qml.expval(qml.Hermitian(A, wires=0))

# Exercise 3.3
dev = qml.device("default.qubit", wires = 2)

@qml.qnode(dev)
def circuit():
    """
    This quantum function implements a Bell state and
    should return the probabilities for the PauliZ 
    observable on both qubits, using a single measurement
    """
    qml.H(wires=0)
    qml.CNOT(wires=[0,1])
    return qml.probs(op=qml.Z(wires=0)@qml.Z(wires=1))