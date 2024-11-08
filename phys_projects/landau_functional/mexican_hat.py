import numpy as np
import matplotlib.pyplot as plt


# Define the Landau potential (Mexican hat potential) in 3D
def landau_potential_3d(phi, psi):
    return (phi ** 2 + psi ** 2) ** 2 - 2 * (phi ** 2 + psi ** 2)


# Generate phi and psi values
radius = 1.3

phi = np.linspace(-radius, radius, 400)
psi = np.linspace(-radius, radius, 400)
phi, psi = np.meshgrid(phi, psi)

# Calculate the potential values
potential_3d = landau_potential_3d(phi, psi)

# Plot the 3D Landau functional (Mexican hat potential)
fig = plt.figure(figsize=(5, 4))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(phi, psi, potential_3d, cmap='viridis')

ax.set_xlabel(r'$\varphi_1$')
ax.set_ylabel(r'$\varphi_2$')
ax.set_zlabel(r'$V(\varphi_1, \varphi_2)$')
ax.set_title('"Mexican Hat" Potential')

ax.view_init(elev=30, azim=60)

plt.tight_layout()
plt.savefig('mexican_hat.svg', transparent=True)
