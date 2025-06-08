import pennylane as qml
import numpy as np


# Exercise 1.10.1
dev = qml.device("default.qubit", wires=1)

@qml.qnode(dev)
def circuit():
    qml.RX(np.pi/4, wires=0)
    qml.H(0)
    qml.Z(0)
    
    return qml.expval(qml.Y(0))

print(circuit())

# Exercise 1.10.2
shot_results = []
shot_values = [100, 1000, 10000, 100000, 1000000]
i=0

for shots in shot_values:

    dev = qml.device("default.qubit", wires=1, shots=shots)

    @qml.qnode(dev)
    def circuit():
        qml.RX(np.pi/4, wires=0)
        qml.H(0)
        qml.Z(0)
    
        return qml.expval(qml.Y(0))
    
    result = circuit()
    shot_results.append(result)

print(qml.math.unwrap(shot_results))

# Exercise 1.10.3
dev = qml.device("default.qubit", wires=1, shots=100000)

@qml.qnode(dev)
def circuit():
    qml.RX(np.pi / 4, wires=0)
    qml.Hadamard(wires=0)
    qml.PauliZ(wires=0)

    return qml.sample(qml.Y(0))


def compute_expval_from_samples(samples):
    """Compute the expectation value of an observable given a set of
    sample outputs. You can assume that there are two possible outcomes,
    1 and -1.

    Args:
        samples (np.array[float]): 100000 samples representing the results of
            running the above circuit.

    Returns:
        float: the expectation value computed based on samples.
    """

    estimated_expval = 0

    for i in range(len(samples)):
        if samples[i] == 1:
            estimated_expval += 1
        else:
            estimated_expval -= 1
    return estimated_expval / 100000

samples = circuit()
print(compute_expval_from_samples(samples))

# Exercise 1.10.4
def variance_experiment(n_shots):
    """Run an experiment to determine the variance in an expectation
    value computed with a given number of shots.

    Args:
        n_shots (int): The number of shots

    Returns:
        float: The variance in expectation value we obtain running the
        circuit 100 times with n_shots shots each.
    """

    n_trials = 100
    res = []
    dev = qml.device("default.qubit", wires=1, shots = n_shots)

    @qml.qnode(dev)
    def circuit():
        qml.Hadamard(wires=0)
        return qml.expval(qml.PauliZ(wires=0))

    for _ in range(n_trials):
        result=circuit()
        res.append(result)
    return np.var(res)


def variance_scaling(n_shots):
    """Once you have determined how the variance in expectation value scales
    with the number of shots, complete this function to programmatically
    represent the relationship.

    Args:
        n_shots (int): The number of shots

    Returns:
        float: The variance in expectation value we expect to see when we run
        an experiment with n_shots shots.
    """

    estimated_variance = 0
    estimated_variance = 1 / n_shots
    return estimated_variance


shot_vals = [10, 20, 40, 100, 200, 400, 1000, 2000, 4000]

results_experiment = [variance_experiment(shots) for shots in shot_vals]
results_scaling = [variance_scaling(shots) for shots in shot_vals]
# plot = plotter(shot_vals, results_experiment, results_scaling)