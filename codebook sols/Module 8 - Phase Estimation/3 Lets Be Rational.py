import pennylane as qml
import numpy as np

# Exercise P3.1
dev = qml.device("default.qubit", wires=10)

def fractional_binary_to_decimal(binary_fraction, wires):
    return float(binary_fraction/ 2 ** len(wires))

def phase_window(probs, estimation_wires):
    """ Given an array of probabilities, return the phase window of the 
    unitary's eigenvalue
    
    Args: 
        probs (array[float]): Probabilities on the estimation wires.
        estimation_wires (list[int]): List of estimation wires
    
    Returns:
        (float, float): the lower and upper bound of the phase
    """

    sorted_indices = np.argsort(probs)[::-1]
    most_likely_idx = sorted_indices[0]
    second_most_likely_idx = sorted_indices[1]
    
    def binary_to_decimal_phase(idx, n_wires):
        bitstring = format(idx, f'0{n_wires}b')
        phase = 0
        for i, bit in enumerate(bitstring):
            phase += int(bit) / (2 ** (i + 1))
        return phase
    
    n = len(estimation_wires)
    bound_1 = binary_to_decimal_phase(most_likely_idx, n)
    bound_2 = binary_to_decimal_phase(second_most_likely_idx, n)
    
    return (bound_1, bound_2)


# Test your solution

# You can increase the number of estimation wires to a maximum of range(0, 9)
estimation_wires = range(0, 3)

# The target is set to the last qubit
target_wires = [9]

# Define the unitary
U = np.array([[1, 0], [0, np.exp((2*np.pi*1j/7))]])

probs = qpe(U, estimation_wires, target_wires)

print(phase_window(probs, estimation_wires))

# MODIFY TO TRUE AFTER TESTING YOUR SOLUTION
done = True


# Exercise P3.2
dev = qml.device("default.qubit", wires=10)

def estimates_array(unitary):
    """ Given a unitary, return a list of its phase windows

    Args:
        unitary (array[complex]): A unitary matrix.

    Returns:
        [(float, float)]: a list of phase windows for 2 to 9
        estimation wires
    """
    estimates = []
    target_wires = [9]

    # Loop over number of estimation wires from 2 to 9
    for num_wires in range(2, 10):
        estimation_wires = list(range(num_wires))
        
        # Get the probabilities from QPE
        probs = qpe(unitary, estimation_wires, target_wires)
        
        # Calculate the phase window using the two most likely outcomes
        phase_bounds = phase_window(probs, estimation_wires)
        
        estimates.append(phase_bounds)

    return estimates


# Define the unitary
U = np.array([[1, 0], [0, np.exp((2*np.pi*1j/7))]])

estimates_array(U)

###################
# SUBMIT FOR PLOT #
###################
