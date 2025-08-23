import pennylane as qml
import numpy as np

# Exercise G3.1
n_bits = 5
query_register = list(range(n_bits))
aux = [n_bits]
all_wires = query_register + aux
dev = qml.device("default.qubit", wires=all_wires)


def oracle(combo):
    """Implement an oracle using a multi-controlled X gate.

    Args:
        combo (list): A list of bits representing the secret combination.
    """
    combo_str = "".join(str(j) for j in combo)
    
    qml.MultiControlledX(
        wires=all_wires,
        control_values=combo
    )

# Exercise G3.2
def hadamard_transform(my_wires):
    """Apply the Hadamard transform on a given set of wires.

    Args:
        my_wires (list[int]): A list of wires on which the Hadamard transform will act.
    """
    for wire in my_wires:
        qml.Hadamard(wires=wire)


def diffusion():
    """Implement the diffusion operator using the Hadamard transform and
    multi-controlled X."""

    hadamard_transform(query_register)
    qml.MultiControlledX(
        wires=query_register + aux,
        control_values=[0] * len(query_register)
    )
    hadamard_transform(query_register)

# Exercise G3.3
@qml.qnode(dev)
def grover_circuit(combo):
    """Apply the MultiControlledX Grover operator and return probabilities on
    query register.

    Args:
        combo (list[int]): A list of bits representing the secret combination.

    Returns:
        array[float]: Measurement outcome probabilities.
    """
    hadamard_transform(query_register)
    qml.X(aux)
    qml.H(aux)

    oracle(combo)
    diffusion()
    
    return qml.probs(wires=query_register)