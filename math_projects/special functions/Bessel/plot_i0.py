import numpy as np
import matplotlib.pyplot as plt
from scipy.special import i0

# Define the range of 'a' values for plotting I0(a)
a_values = np.linspace(0, 10, 500)
I0_values = i0(a_values)

# Plotting the I0(a) function
plt.figure(figsize=(8, 6))
plt.plot(a_values, I0_values, label=r'$I_0(a)$', color='blue')
plt.title(r'Plot of the Modified Bessel Function of the First Kind, $I_0(a)$')
plt.xlabel(r'$a$')
plt.ylabel(r'$I_0(a)$')
plt.legend()
plt.grid(True)
plt.show()
