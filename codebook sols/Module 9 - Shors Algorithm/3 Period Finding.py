import pennylane as qml
import numpy as np
import fractions

# Exercise S3.1
def U():
    qml.SWAP(wires=[2, 3])
    qml.SWAP(wires=[1, 2])
    qml.SWAP(wires=[0, 1])
    for i in range(4):
        qml.PauliX(wires=i)


matrix = qml.matrix(U, wire_order=range(4))()

n_target_wires = 4
target_wires = range(n_target_wires)
n_estimation_wires = 3
estimation_wires = range(4, 4 + n_estimation_wires)


dev = qml.device("default.qubit", shots=1, wires=n_target_wires + n_estimation_wires)


@qml.qnode(dev)
def circuit(matrix):
    """Return a sample after taking a shot at the estimation wires.

    Args:
        matrix (array[complex]): matrix representation of U.

    Returns:
        array[float]: a sample after taking a shot at the estimation wires.
    """

    qml.PauliX(wires=3)
    
    qml.QuantumPhaseEstimation(
        matrix,
        target_wires=target_wires,
        estimation_wires=estimation_wires
    )

    return qml.sample(wires=estimation_wires)


def get_phase(matrix):
    binary_arr = circuit(matrix)
    print(binary_arr)
    binary = "".join([str(b) for b in binary_arr])
    return int(binary, 2) / 2**n_estimation_wires


for i in range(5):
    print(f"shot {i+1}, phase:", get_phase(matrix))


# Exercise S3.2
def U():
    qml.SWAP(wires=[2, 3])
    qml.SWAP(wires=[1, 2])
    qml.SWAP(wires=[0, 1])
    for i in range(4):
        qml.PauliX(wires=i)


matrix = qml.matrix(U, wire_order=range(4))()

target_wires = range(4)
n_estimation_wires = 3
estimation_wires = range(4, 4 + n_estimation_wires)


def get_period(matrix):
    """Return the period of the state using the already-defined
    get_phase function.

    Args:
        matrix (array[complex]): matrix associated with the operator U

    Returns:
        int: Obtained period of the state.
    """

    shots = 10

    max_period = 0

    for _ in range(shots):
        phase = get_phase(matrix)
        fraction = fractions.Fraction(phase).limit_denominator(2 ** n_estimation_wires)
        denominator = fraction.denominator
        
        if denominator > max_period:
            max_period = denominator

    return max_period


print(get_period(matrix))

# Exercise S3.3
def U():
    qml.SWAP(wires=[2, 3])
    qml.SWAP(wires=[1, 2])
    qml.SWAP(wires=[0, 1])
    for i in range(4):
        qml.PauliX(wires=i)


dev = qml.device("default.qubit", wires=4)


@qml.qnode(dev)
def circuit():
    """Apply U four times to |0001> to verify this is the period.

    Returns:
        array[float]: probabilities of each basis state.
    """

    qml.PauliX(wires=3)
    
    for _ in range(4):
        U()
    
    return qml.probs(wires=range(4))


print(circuit())
