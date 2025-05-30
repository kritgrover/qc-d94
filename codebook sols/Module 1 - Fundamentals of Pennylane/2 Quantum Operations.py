import pennylane as qml
import numpy as np

# Exercise 2.1
dev = qml.device("default.qubit", wires = 3)

@qml.qnode(dev)
def prep_circuit(alpha, beta, gamma):
    """
    Prepares the state alpha|001> + beta|010> + gamma|100>.
    Args:
    alpha, beta, gamma (np.complex): The coefficients of the quantum state
    to prepare.
    Returns:
    (np.array): The quantum state
    """
    qml.StatePrep(np.array([0, alpha, beta, 0, gamma, 0, 0, 0]), wires=range(3), normalize=True)
    return qml.state()

alpha, beta, gamma = 1/np.sqrt(3), 1/np.sqrt(3), 1/np.sqrt(3),

print("The prepared state is", prep_circuit(alpha, beta, gamma))

# Exercise 2.2
dev = qml.device("default.qubit", wires = 2)

@qml.qnode(dev)
def single_qubit_gates(theta, phi):
    """
    Implements the quantum circuit shown in the statement
    Args:
    - theta, phi (float): The arguments for the RX and RZ gates, respectively
    Returns:
    - (np.array): The output quantum state.
    
    """
    qml.Hadamard(wires=0)
    qml.Hadamard(wires=1)
    qml.T(wires=0)
    qml.S(wires=1)
    qml.RX(theta, wires=0)
    qml.RZ(phi, wires=1)
    return qml.state()

theta, phi = np.pi/3, np.pi/4
print("The output state of the circuit is: ", single_qubit_gates(theta, phi))

# Exercise 2.3
dev = qml.device("default.qubit", wires = 3)

@qml.qnode(dev)
def multi_qubit_gates(theta,phi):
    """
    Applies the circuit shown the figure above
    Args:
    theta, phi (float): parameters of the CRX and CRY gates, in that order.
    Returns:
    - (np.array): the quantum state
    """

    qml.Hadamard(wires=0)
    qml.CRY(phi, wires=[0,1])
    qml.CRX(theta, wires=[1,2])
    qml.S(wires=1)
    qml.T(wires=2)
    qml.Toffoli(wires=[0,1,2])
    qml.SWAP(wires=[0,2])
    return qml.state()

theta, phi = np.pi/3, np.pi/4
print("The output state is: \n", multi_qubit_gates(theta, phi))

# Exercise 2.4
dev = qml.device("default.qubit", wires = 3)

@qml.qnode(dev)
def ctrl_circuit(theta,phi):
    """Implements the circuit shown in the Codercise statement
    Args:
        theta (float): Rotation angle for RX
        phi (float): Rotation angle for RY
    Returns:
        (numpy.array): The output state of the QNode
    """
    
    qml.RY(phi, wires=0)
    qml.Hadamard(wires=1)
    qml.RX(theta, wires=2)
    qml.ctrl(qml.S, control=(0), control_values=(1))(wires=[1])
    qml.ctrl(qml.T, control=(1), control_values=(0))(wires=[2])
    qml.ctrl(qml.Hadamard, control=(2), control_values=(1))(wires=[0])
    
    return qml.state()

# Exercise 2.5
dev = qml.device("default.qubit", wires = 2)

@qml.qnode(dev)
def phase_kickback(matrix):
    """Applies phase kickback to a single-qubit operator whose matrix is known
    Args:S
    - matrix (numpy.array): A 2x2 matrix
    Returns:
    - (numpy.array): The output state after applying phase kickback
    """
    qml.Hadamard(wires=0)
    qml.ControlledQubitUnitary(matrix, control_wires=[0], wires=[1], control_values=(1))
    qml.Hadamard(wires=0)
    return qml.state()

matrix = np.array([[-0.69165024-0.50339329j,  0.28335369-0.43350413j],
    [ 0.1525734 -0.4949106j , -0.82910055-0.2106588j ]])

print("The state after phase kickback is: \n" , phase_kickback(matrix))

# Exercise 2.6
dev = qml.device("default.qubit")

def do(k):
    qml.StatePrep([1,k], wires = [0], normalize = True)

def apply(theta):
    qml.IsingXX(theta, wires = [1,2])

@qml.qnode(dev)
def do_apply_undo(k,theta):
    """
    Applies V, controlled-U, and the inverse of V
    Args: 
    - k, theta: The parameters for do and apply (V and U) respectively
    Returns:
    - (np.array): The output state of the routine
    """
    do(k)
    qml.ctrl(apply, control=(0), control_values=(1))(theta)
    qml.adjoint(do)(k)
    return qml.state()

k, theta = 0.5, 0.8

print("The output state is: \n", do_apply_undo(k, theta))