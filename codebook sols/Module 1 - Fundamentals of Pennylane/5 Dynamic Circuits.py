import pennylane as qml
import numpy as np

# Exercise PF5.1
n_shots = 10000
dev = qml.device("default.qubit", shots=n_shots)
np.random.seed(0)

@qml.qnode(dev)
def circuit():
    """
    Implements the Elitzur-Vaidman bomb tester with the correct conditional
    logic to model the non-unitary explosion event.
    """
    qml.PauliX(wires=1)
    qml.Hadamard(wires=0)
    qml.CNOT(wires=[0, 1])
    m_bomb = qml.measure(1, reset=True)

    qml.cond(m_bomb == 0, qml.PauliX)(wires=0)
    qml.cond(m_bomb == 0, qml.PauliX)(wires=0)

    def reset_photon():
        qml.measure(0, reset=True)
        return 0

    qml.cond(m_bomb == 1, qml.Hadamard)(wires=0)
    m_det = qml.measure(0)
    return qml.counts((m_bomb, m_det), all_outcomes=True)

# --- Run and Analyze ---
results = circuit()

favorable_cases = results.get("11", 0)
prob_suc = favorable_cases / n_shots

print(f"Counts ((m_bomb, m_det)): {results}")
print(f"The success probability is {prob_suc}")


# Exercise PF5.2
n_shots = 10000
dev = qml.device("default.qubit", shots=n_shots)
np.random.seed(0)

@qml.qnode(dev)
def circuit():
    """
    This quantum function implements an improved version of 'bomb tester'
    and returns relevant statistics with qml.counts
    """
    # 1. Initialize a "live" bomb on qubit 1
    qml.PauliX(wires=1)

    # 2. Put the photon (qubit 0) into a superposition of paths
    qml.Hadamard(wires=0)

    # 3. Photon interacts with the bomb
    qml.CNOT(wires=[0, 1])

    # 4. Measure the bomb's state mid-circuit
    m_bomb = qml.measure(1, reset=True)

    # 5. Apply second beam-splitter conditionally (only if bomb didn't explode)
    qml.cond(m_bomb == 1, qml.Hadamard)(wires=0)

    # 6. First measurement of photon detector
    m_det = qml.measure(0)

    # 7. For inconclusive cases (m_bomb=1, m_det=0), try again
    # This is where we boost the success rate!
    qml.cond((m_bomb == 1) & (m_det == 0), qml.PauliX)(wires=1)  # Reset bomb to live
    qml.cond((m_bomb == 1) & (m_det == 0), qml.Hadamard)(wires=0)  # Superposition
    qml.cond((m_bomb == 1) & (m_det == 0), qml.CNOT)(wires=[0, 1])  # Interact
    qml.cond((m_bomb == 1) & (m_det == 0), qml.Hadamard)(wires=0)  # Second beam splitter

    # 8. Second measurement (only relevant for inconclusive retests)
    m_det_2 = qml.measure(0)

    return qml.counts(op=[m_bomb, m_det], all_outcomes=True), qml.counts(op=[m_det, m_det_2], all_outcomes=True)

results = circuit()  # array of two dictionaries

prob_suc_1 = results[0].get("11", 0) / n_shots  # First round successes
prob_suc_2 = results[1].get("01", 0) / n_shots  # Second round successes from retests

prob_suc = prob_suc_1 + prob_suc_2
print("The success probability is", prob_suc)
