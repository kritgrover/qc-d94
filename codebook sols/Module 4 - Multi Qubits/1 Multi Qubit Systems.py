import pennylane as qml
import numpy as np

# Exercise 1.11.1
num_wires = 3
dev = qml.device("default.qubit", wires=num_wires)


@qml.qnode(dev)
def make_basis_state(basis_id):
    """Produce the 3-qubit basis state corresponding to |basis_id>.

    Note that the system starts in |000>.

    Args:
        basis_id (int): An integer value identifying the basis state to construct.

    Returns:
        np.array[complex]: The computational basis state |basis_id>.
    """

    num = np.binary_repr(basis_id, width = num_wires)
    for i in range(len(num)):
        if num[i] == '1':
            qml.X(wires=i)
    return qml.state()

basis_id = 3
print(f"Output state = {make_basis_state(basis_id)}")

# Exercise 1.11.2
dev = qml.device("default.qubit", wires=2)

@qml.qnode(dev)
def two_qubit_circuit():
    qml.H(0)
    qml.X(1)

    return qml.expval(qml.Y(0)), qml.expval(qml.Z(1))

# Exercise 1.11.3
dev = qml.device("default.qubit", wires=2)

@qml.qnode(dev)
def create_one_minus():
    qml.X(0)
    qml.H(1)
    qml.Z(1)

    return qml.expval(qml.Z(0) @ qml.X(1))

print(create_one_minus())

# Exercise 1.11.4
dev = qml.device("default.qubit", wires=2)

@qml.qnode(dev)
def circuit_1(theta):
    """Implement the circuit and measure Z I and I Z.

    Args:
        theta (float): a rotation angle.

    Returns:
        float, float: The expectation values of the observables Z I, and I Z
    """

    qml.RX(theta, wires=0)
    qml.RY(2*theta, wires=1)
    return qml.expval(qml.Z(0)), qml.expval(qml.Z(1))


@qml.qnode(dev)
def circuit_2(theta):
    """Implement the circuit and measure Z Z.

    Args:
        theta (float): a rotation angle.

    Returns:
        float: The expectation value of the observable Z Z
    """

    qml.RX(theta, wires=0)
    qml.RY(2*theta, wires=1)
    return qml.expval(qml.Z(0) @ qml.Z(1))


def zi_iz_combination(ZI_results, IZ_results):
    """Implement a function that acts on the ZI and IZ results to
    produce the ZZ results. How do you think they should combine?

    Args:
        ZI_results (np.array[float]): Results from the expectation value of
            ZI in circuit_1.
        IZ_results (np.array[float]): Results from the expectation value of
            IZ in circuit_2.

    Returns:
        np.array[float]: A combination of ZI_results and IZ_results that
        produces results equivalent to measuring ZZ.
    """

    combined_results = np.zeros(len(ZI_results))

    combined_results = ZI_results*IZ_results
    return combined_results


theta = np.linspace(0, 2 * np.pi, 100)

circuit_1_results = np.array([circuit_1(t) for t in theta])

ZI_results = circuit_1_results[:, 0]
IZ_results = circuit_1_results[:, 1]
combined_results = zi_iz_combination(ZI_results, IZ_results)

ZZ_results = np.array([circuit_2(t) for t in theta])
