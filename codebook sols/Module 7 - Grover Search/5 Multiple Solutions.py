import pennylane as qml
import numpy as np

# Exercise G5.1
n_bits = 5
query_register = list(range(n_bits))
aux = [n_bits]
all_wires = query_register + aux
dev = qml.device("default.qubit", wires=all_wires)


def oracle_multi(combos):
    """Implement multi-solution oracle using sequence of multi-controlled X gates.

    Args:
        combos (list[list[int]]): A list of solutions.
    """
    for combo in combos:
        combo_str = "".join(str(j) for j in combo)
        temp = []
        for a in combo_str:
            temp.append(int(a))
        qml.MultiControlledX(
            wires=all_wires,
            control_values=temp
        )

# Exercise G5.2a
n_bits = 5
query_register = list(range(n_bits))
aux = [n_bits]
all_wires = query_register + aux
dev = qml.device("default.qubit", wires=all_wires, shots=None)


def grover_iter_multi(combos, num_steps):
    """Run Grover search for multiple secret combinations and a number
    of Grover steps.

    Args:
        combos (list[list[int]]): The secret combination, represented as a list of bits.
        num_steps (int): The number of Grover iterations to perform.

    Returns:
        array[float]: Probability for observing different outcomes.
    """

    @qml.qnode(dev)
    def inner_circuit():
        qml.PauliX(wires=n_bits)
        qml.Hadamard(wires=n_bits)
        hadamard_transform(query_register)

        for _ in range(num_steps):
            oracle_multi(combos)
            diffusion(n_bits)
        return qml.probs(wires=query_register)

    return inner_circuit()

# Exercise G5.2b
m_list = range(3)
opt_steps = []

for m_bits in m_list:
    combos = [[int(s) for s in np.binary_repr(j, n_bits)] for j in range(2**m_bits)]
    step_list = range(1, 10)
    prob_list = []
    
    for steps in step_list:
        # Run the multi-solution Grover iteration
        probs = grover_iter_multi(combos, steps)
        total_prob = 0
        for combo in combos:
            # Convert binary list to decimal index
            combo_index = int(''.join(str(bit) for bit in combo), 2)
            total_prob += probs[combo_index]
        
        prob_list.append(total_prob)
    opt_steps.append(local_max_arg(prob_list))

print("The optimal number of Grover steps for the number of solutions in", [1, 2, 4], "is", opt_steps, ".")

# Exercise G5.3
grad = -0.5
intercept = 2.03