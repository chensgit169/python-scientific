import numpy as np
import matplotlib.pyplot as plt


# Define the Landau functional potential
# 定义 Landau 自由能
def landau_free_energy(phi, a, b):
    return a * phi ** 2 + b * phi ** 4


# 定义序参量的范围
phi = np.linspace(-2, 2, 400)

# 设置不同参数
parameters = [
    {"a": 2, "b": 1, "label": "$\\mu_0^2 > 0, \\lambda > 0$"},
    {"a": -2, "b": 1, "label": "$\\mu_0^2 < 0, \\lambda > 0$"},
]

# 创建图像
plt.figure(figsize=(4.5, 3))

for params in parameters:
    a = params["a"]
    b = params["b"]
    F = landau_free_energy(phi, a, b)
    plt.plot(phi, F, label=params["label"])

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
# plt.title('$V(\\varphi)=\\frac{\\mu_0^2}{2}\\varphi^2+\\frac{\\lambda_0}{4!}\\varphi^4$')
plt.xlabel(r'$\varphi$')
plt.ylabel(r'$V(\varphi)$')
plt.legend()

plt.tight_layout()
plt.savefig('landau_functional.svg', transparent=True)
