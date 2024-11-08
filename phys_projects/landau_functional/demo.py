import numpy as np
import matplotlib.pyplot as plt


# 定义 Landau 自由能
def landau_free_energy(phi, a, b):
    return a * phi ** 2 + b * phi ** 4


# 定义序参量的范围
phi = np.linspace(-2, 2, 400)

# 设置不同参数
parameters = [
    {"a": 2, "b": 1, "label": "a > 0, b > 0"},
    {"a": -2, "b": 1, "label": "a < 0, b > 0"},
]

# 创建图像
plt.figure(figsize=(6, 4))

for params in parameters:
    a = params["a"]
    b = params["b"]
    F = landau_free_energy(phi, a, b)
    plt.plot(phi, F, label=params["label"])

# 添加图例和标签
plt.title('Landau Functional $F(\\phi)=a(T)\\phi^2+b(T)\\phi^4$')
plt.xlabel('Order Parameter ($\\phi$)')
plt.ylabel('Free Energy (F)')
plt.legend()
# plt.grid(True)

# 显示图像
plt.tight_layout()
plt.savefig('landau_functional.svg', transparent=True)
