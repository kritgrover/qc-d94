import pennylane as qml
import numpy as np

# Exercise 1.14.1
dev = qml.device("default.qubit", wires=2)

# Starting from the state |00>, implement a PennyLane circuit
# to construct each of the Bell basis states.

@qml.qnode(dev)
def prepare_psi_plus():
    # PREPARE (1/sqrt(2)) (|00> + |11>)
    qml.H(0)
    qml.CNOT([0,1])
    return qml.state()


@qml.qnode(dev)
def prepare_psi_minus():
    # PREPARE (1/sqrt(2)) (|00> - |11>)
    qml.H(0)
    qml.CNOT([0,1])
    qml.Z(1)
    return qml.state()


@qml.qnode(dev)
def prepare_phi_plus():
    # PREPARE  (1/sqrt(2)) (|01> + |10>)
    qml.X(1)
    qml.H(0)
    qml.CNOT([0,1])
    return qml.state()


@qml.qnode(dev)
def prepare_phi_minus():
    # PREPARE  (1/sqrt(2)) (|01> - |10>)
    qml.X(1)
    qml.H(0)
    qml.CNOT([0,1])
    qml.Z(0)
    return qml.state()


psi_plus = prepare_psi_plus()
psi_minus = prepare_psi_minus()
phi_plus = prepare_phi_plus()
phi_minus = prepare_phi_minus()

# Uncomment to print results
print(f"|ψ_+> = {psi_plus}")
print(f"|ψ_-> = {psi_minus}")
print(f"|ϕ_+> = {phi_plus}")
print(f"|ϕ_-> = {phi_minus}")

# Exercise 1.14.2
dev = qml.device("default.qubit", wires=3)
# State of first 2 qubits
state = [0, 1]

@qml.qnode(device=dev)
def apply_control_sequence(state):
    # Set up initial state of the first two qubits
    if state[0] == 1:
        qml.PauliX(wires=0)
    if state[1] == 1:
        qml.PauliX(wires=1)
    qml.PauliX(wires=2)
    qml.Hadamard(wires=2)

    # IF STATE OF FIRST TWO QUBITS IS 01, APPLY X TO THIRD QUBIT
    if state[0] == 0 and state[1] == 1:
        qml.X(2)
    # IF STATE OF FIRST TWO QUBITS IS 10, APPLY Z TO THIRD QUBIT
    if state[1] == 0 and state[0] == 1:
        qml.Z(2)
    # IF STATE OF FIRST TWO QUBITS IS 11, APPLY Y TO THIRD QUBIT
    if state[0] == 1 and state[1] == 1:
        qml.Y(2)
    return qml.state()

print(apply_control_sequence(state))
