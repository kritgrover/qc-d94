import numpy as np
import matplotlib.pyplot as plt
from scipy.special import hermite
from matplotlib.gridspec import GridSpec
import math

# Set up the figure and subplots
fig = plt.figure(figsize=(14, 8))
gs = GridSpec(2, 1, height_ratios=[1, 1])

ax1 = fig.add_subplot(gs[0])  # Wavefunctions
ax2 = fig.add_subplot(gs[1])  # Probability densities

# Parameters
x = np.linspace(-4, 4, 500)
n_values = range(8)  # n = 0 to 7
colors = plt.cm.viridis(np.linspace(0, 1, len(n_values)))  # Color gradient

# Common function to calculate QHO states
def qho_state(n, x, m=1.0, omega=1.0, hbar=1.0):
    coeff = 1 / np.sqrt(2**n * math.factorial(n)) * (m * omega / (np.pi * hbar))**(0.25)
    exponent = np.exp(-m * omega * x**2 / (2 * hbar))
    z = np.sqrt(m * omega / hbar) * x
    H_n = hermite(n)(z)
    return coeff * exponent * H_n

# Plot wavefunctions and probability densities
for n, color in zip(n_values, colors):
    psi = qho_state(n, x)
    prob = psi**2
    
    # Offset each wavefunction for clarity
    y_offset = 1.5 * n
    ax1.plot(x, psi + y_offset, color=color, label=f'n={n}')
    ax1.fill_between(x, y_offset, psi + y_offset, color=color, alpha=0.2)
    
    # Plot probability densities
    ax2.plot(x, prob, color=color, label=f'n={n}')
    ax2.fill_between(x, 0, prob, color=color, alpha=0.2)

# Format wavefunction plot
ax1.set_title('Wavefunctions $\psi_n(x)$ for QHO (n=0 to 7)')
ax1.set_ylabel('$\psi_n(x)$ (offset)')
ax1.set_yticks([1.5 * n for n in n_values])
ax1.set_yticklabels([f'n={n}' for n in n_values])
ax1.axhline(0, color='black', linewidth=0.5, linestyle='--')
ax1.grid(True, alpha=0.3)

# Format probability density plot
ax2.set_title('Probability Densities $|\psi_n(x)|^2$ for QHO (n=0 to 7)')
ax2.set_xlabel('Position $x$')
ax2.set_ylabel('$|\psi_n(x)|^2$')
ax2.grid(True, alpha=0.3)
ax2.set_ylim(0, 0.6)

plt.tight_layout()
plt.show()