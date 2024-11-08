import numpy as np
import matplotlib.pyplot as plt

# 定义温度范围，从低温到高温（高于居里温度）
T = np.linspace(0, 2, 400)  # 归一化温度 T/T_C

# 定义铁磁体相变的磁化强度关系
# 这里使用一个简单的近似模型：M(T) = (1 - T/T_C)^beta
# 当 T < T_C 时，磁化强度为 (1 - T)^0.5，当 T >= T_C 时，磁化强度为 0
T_C = 1
beta = 0.5
M = np.where(T <= T_C, (1 - T/T_C)**beta / 2, 0)

# 创建图像
plt.figure(figsize=(4, 3))

plt.plot(T, M, label='Magnetization $\\langle M \\rangle$', color='b')
plt.axvline(x=T_C, color='r', linestyle='--', label='Curie Temperature $T_C$')

# 添加图例和标签
plt.title('Phase transition of a Ferromagnet')
plt.xlabel('Temperature $T/T_C$')
plt.ylabel('Magnetization $\\langle M\\rangle$')
plt.legend()


ax = plt.gca()

ax.set_xlim(0, 2)
ax.set_ylim(0, 1)
ax.tick_params(left=False, bottom=False)
# 隐藏刻度数字
ax.set_xticklabels([])
ax.set_yticklabels([])

# 显示图像
plt.tight_layout()
plt.savefig('ferromagnet.svg', transparent=True)
