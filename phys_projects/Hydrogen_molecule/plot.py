import numpy as np
import matplotlib.pyplot as plt


def func_S(r):
    return (1 + r + r ** 2) * np.exp(-r)


def func_C(r):
    return (np.exp(-2 * r) * (1 + r) - 1) / r


def func_D(r):
    return - (1 + r) * np.exp(-r)


ws = np.linspace(0.01, 25, 1000)
alpha = (1 - 2 * func_D(ws) - func_C(ws)) / (1 - 2 * func_D(ws) - func_S(ws))
rs = ws / alpha

print(alpha.argmax())

i = alpha.argmax()
print(alpha[-1])

plt.figure(figsize=(5, 4), dpi=300)
plt.plot(rs, alpha, label='$\\alpha(R)$')
plt.plot(rs[i], alpha[i], '*',
         label='$R=%.3f, \\alpha_{max} = %.3f$' % (rs[i], alpha[i]))
plt.plot(rs, np.ones_like(rs), '--', label='$\\alpha=1$')
plt.xlabel('r')
plt.ylabel('$\\alpha$')
plt.legend()
plt.title('Variational LCAO $\\alpha(R)$')
plt.savefig('vLCAO.png', transparent=False)
