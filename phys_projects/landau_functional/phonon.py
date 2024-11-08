import numpy as np
import matplotlib.pyplot as plt

# 定义参数
k = 1.0  # 弹性常数
m = 1.0  # 质量
a = 1.0  # 晶格常数

# 波矢范围
K = np.linspace(-np.pi/a, np.pi/a, 400)

# 角频率的色散关系
omega = 2 * np.sqrt(k / m) * np.abs(np.sin(K * a / 2))

# 创建图像
plt.figure(figsize=(5, 4))

plt.plot(K, omega, label='$\\omega(k) = 2 \\sqrt{\\frac{k}{m}} \\left| \\sin\\left(\\frac{ka}{2}\\right) \\right|$', color='b')

# 添加图例和标签
plt.title('Phonon Dispersion Relation in a Harmonic Crystal')
plt.xlabel('$k$')
plt.ylabel('$\\omega$')
plt.legend()
plt.grid(True)

# 显示图像
plt.tight_layout()
plt.savefig('phonon.svg', transparent=True)
