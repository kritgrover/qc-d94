import pennylane as qml
import numpy as np

# Exercise 1.13.1
dev = qml.device("default.qubit", wires=2)
phi, theta, omega = 1.2, 2.3, 3.4

@qml.qnode(device=dev)
def true_cz(phi, theta, omega):
    # prepare_states(phi, theta, omega)
    qml.CZ([0,1])
    return qml.state()


@qml.qnode(dev)
def imposter_cz(phi, theta, omega):
    # prepare_states(phi, theta, omega)
    qml.H(1)
    qml.CNOT([0,1])
    qml.H(1)
    return qml.state()


print(f"True CZ output state {true_cz(phi, theta, omega)}")
print(f"Imposter CZ output state {imposter_cz(phi, theta, omega)}")

# Exercise 1.13.2
dev = qml.device("default.qubit", wires=2)
phi, theta, omega = 1.2, 2.3, 3.4

@qml.qnode(dev)
def apply_swap(phi, theta, omega):
    # prepare_states(phi, theta, omega)
    qml.SWAP([0,1])
    return qml.state()


@qml.qnode(dev)
def apply_swap_with_cnots(phi, theta, omega):
    # prepare_states(phi, theta, omega)
    qml.CNOT([0,1])
    qml.CNOT([1,0])
    qml.CNOT([0,1])
    return qml.state()


print(f"Regular SWAP state = {apply_swap(phi, theta, omega)}")
print(f"CNOT SWAP state = {apply_swap_with_cnots(phi, theta, omega)}")

# Exercise 1.13.3
dev = qml.device("default.qubit", wires=3)
phi, theta, omega = 1.2, 2.3, 3.4

@qml.qnode(dev)
def no_swap(phi, theta, omega):
    # prepare_states(phi, theta, omega)
    return qml.state()


@qml.qnode(dev)
def controlled_swap(phi, theta, omega):
    # prepare_states(phi, theta, omega)
    qml.Toffoli([0,1,2])
    qml.Toffoli([0,2,1])
    qml.Toffoli([0,1,2])
    return qml.state()


print(no_swap(phi, theta, omega))
print(controlled_swap(phi, theta, omega))

# Exercise 1.13.4
dev = qml.device("default.qubit", wires=4)

@qml.qnode(dev)
def four_qubit_mcx():
    qml.H(0)
    qml.H(1)
    qml.H(2)
    qml.MultiControlledX(wires=[0, 1, 2, 3], control_values=[0, 0, 1])
    return qml.state()

print(four_qubit_mcx())

# Exercise 1.13.5
# Wires 0, 1, 2 are the control qubits
# Wire 3 is the auxiliary qubit
# Wire 4 is the target
dev = qml.device("default.qubit", wires=5)

@qml.qnode(dev)
def four_qubit_mcx_only_tofs():
    qml.PauliX(wires=0)
    qml.PauliX(wires=1)
    qml.PauliX(wires=2)

    qml.Toffoli(wires=[0, 1, 3])
    qml.Toffoli(wires=[2, 3, 4])
    qml.Toffoli(wires=[0, 1, 3])

    return qml.state()


# print(four_qubit_mcx_only_tofs())
