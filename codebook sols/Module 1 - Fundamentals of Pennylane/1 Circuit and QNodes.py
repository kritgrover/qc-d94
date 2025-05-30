import pennylane as qml # type: ignore

# Exercise 1.1a
def circuit(theta): # Write any arguments you need here
    """
    This quantum function implements the circuit shown above
    and returns the output quantum state
    """
    qml.Hadamard(wires=0)
    qml.PauliX(wires=1)
    qml.CNOT(wires = [0, 1])
    qml.RY(theta, wires=1)
    return qml.state()

# Exercise 1.1b
dev_qubit = qml.device("default.qubit", wires = ["alice", "bob"])# Define the device here
dev_mixed = qml.device("default.mixed", wires = 2)# Define the device here

@qml.qnode(dev_qubit) # Choose the device you want
def example_circuit(theta):
    
    qml.RX(theta, wires =  "bob") # Complete with wires in the device
    qml.CNOT(wires = ["alice", "bob"] ) # Complete with wires in the device
    
    return qml.state()

print(example_circuit(0.3))

# Exercise 1.1c
dev = qml.device("default.qubit", wires = 2)# Define the device

circuit_qnode = qml.QNode(circuit, dev)# Assign a QNode to circuit"

print(circuit_qnode(0.3))

# Exercise 1.2a
def subcircuit_1(angle):
    qml.RX(angle, wires=0)
    qml.PauliY(wires=1)
    

def subcircuit_2():
    qml.Hadamard(wires=0)
    qml.CNOT(wires=[0,1])
    

dev = qml.device('default.qubit', wires = 2)

@qml.qnode(dev)
def full_circuit(theta, phi):
    subcircuit_1(theta)
    subcircuit_2()
    subcircuit_1(phi)
    
    return qml.state()

# Exercise 1.2b
def subcircuit_1(angle, wire_list):
    """
    Implements the first subcircuit as a function of the RX gate angle
    and the list of wires wire_list on which the gates are applied
    """
    qml.RX(angle, wires=wire_list[0])
    qml.PauliY(wires=wire_list[1])

def subcircuit_2(wire_list):
    """
    Implements the second subcircuit as a function of the list of wires 
    wire_list on which the gates are applied
    """
    qml.Hadamard(wires=wire_list[0])
    qml.CNOT(wires=[wire_list[0], wire_list[1]])

dev = qml.device("default.qubit", wires = [0,1])

@qml.qnode(dev)
def full_circuit(theta, phi):
    """
    Builds the full quantum circuit given the input parameters
    """
    subcircuit_1(theta, [0,1])
    subcircuit_2([0,1])
    subcircuit_1(phi, [1,0])
    return qml.state()
