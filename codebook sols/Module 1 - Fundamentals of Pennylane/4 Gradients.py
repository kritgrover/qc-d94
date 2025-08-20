import pennylane as qml
import numpy as np

# Exercise 4.1
dev = qml.device("default.qubit", wires = 3)

@qml.qnode(dev)
def circuit_as_function(params):
    """
    Implements the circuit shown in the codercise statement.
    Args:
    - params (np.ndarray): [theta_0, theta_1, theta_2, theta_3]
    Returns:
    - (np.tensor): <Z0>
    """

    qml.RX(params[0], wires=0)
    qml.CNOT(wires=[0,1])
    qml.CNOT(wires=[1,2])
    qml.CNOT(wires=[2,0])
    qml.RX(params[1], wires=0)
    qml.RX(params[2], wires=1)
    qml.RX(params[3], wires=2)
    return qml.expval(qml.Z(0))

angles = np.linspace(0, 4 * np.pi, 200)
output_values = np.array([circuit_as_function([0.5, t, 0.5, 0.5]) for t in angles])

# Exercise 4.2
dev = qml.device("default.qubit", wires = 4)

@qml.qnode(dev)
def strong_entangler(weights):
    """
    Applies Strongly Entangling Layers to the default initial state
    Args:
    - weights (np.ndarray): The weights argument for qml.StronglyEntanglingLayers
    Returns:
    - (np.tensor): <Z0>
    """

    qml.StronglyEntanglingLayers(weights=weights, wires=range(4))
    return qml.expval(qml.PauliZ(0))

test_weights = [[[0.1,0.2,0.3],[0.4,0.5,0.6],[0.7, 0.8, 0.9],[0.0, 0.1, 0.2]],[[0.1,0.1,0.1],[0.2,0.2,0.2],[0.3,0.3,0.3],[0.4,0.4,0.4]]]

print("The output of your circuit with these weights is: ", strong_entangler(test_weights))

# Exercise 4.3
dev = qml.device("default.qubit", wires = 3)

@qml.qnode(dev)
def embedding_and_circuit(features, params):
    """
    A QNode that depends on trainable and non-trainable parameters
    Args:
    - features (np.ndarray): Non-trainable parameters in the AngleEmbedding routine
    - params (np.ndarray): Trainable parameters for the rest of the circuit
    Returns:
    - (np.tensor): <Z0>
    """

    qml.AngleEmbedding(features, wires=range(3))
    qml.CNOT(wires=[0,1])
    qml.CNOT(wires=[1,2])
    qml.CNOT(wires=[2,0])
    qml.RY(params[0], wires=0)
    qml.RY(params[1], wires=1)
    qml.RY(params[2], wires=2)
    return qml.expval(qml.Z(0))

features = np.array([0.3,0.4,0.6], requires_grad = False)
params = np.array([0.4,0.7,0.9], requires_grad = True)
print("The gradient of the circuit is:", qml.jacobian(embedding_and_circuit)(features, params))

# Exercise 4.4
dev = qml.device("default.qubit", wires = 2)

@qml.qnode(dev, diff_method = "parameter-shift", max_diff = 2)
def circuit_for_hessian(params):
    """
    Implements the circuit shown in the codercise statement
    Args:
    - params (np.ndarray): [theta_0, theta_1, theta_2, theta_3]
    Returns:
    - np.tensor: <Z0xZ1>
    """

    qml.RY(params[0], 0)
    qml.IsingXX(params[1], range(2))
    qml.RX(params[2], 0)
    qml.RX(params[3], 1)
    return qml.expval(qml.Z(0) @ qml.Z(1))

test_params = np.array([0.1,0.2,0.3,0.4], requires_grad = True)

hessian = qml.jacobian(qml.jacobian(circuit_for_hessian))(test_params)
print("The hessian of the circuit is: \n", hessian)

# Exercise 4.5a
def cost_function(params):
    """
    Computes the cost function given in the codercise, as a function of the
    parameters of circuit_as_function.
    Args:
    - params (np.ndarray): The parameters we pass to circuit_as_function
    Returns:
    - np.float: The cost function evaluated in params.
    """

    x = circuit_as_function(params)
    
    return x**3 - 0.5*x**2 + x

# Exercise 4.5b
def optimize(cost_function, init_params, steps):

    opt = qml.GradientDescentOptimizer(stepsize = 0.4)
    params = init_params

    for i in range(steps):
        params = opt.step(cost_function, params)

    return np.array([cost_function(params)])

initial_parameters = np.array([0.7, 0.3, 0.2, 0.3])
print(f"Initial parameters: {initial_parameters}")
minimum = optimize(cost_function,initial_parameters, 100)