import sympy as sp

# 定义符号
A, B, C = sp.symbols('A B C')
theta = sp.symbols('theta')  # 旋转角度
x1, x2 = sp.symbols('x1 x2')

# 构建二次型的矩阵表示
Q = sp.Matrix([[A, C/2], [C/2, B]])

# 旋转矩阵
R = sp.Matrix([[sp.cos(theta), -sp.sin(theta)],
               [sp.sin(theta),  sp.cos(theta)]])

# 二次型在旋转后的新坐标系中的表示
Q_rotated = R.T * Q * R

# 展开并化简矩阵
Q_rotated_simplified = sp.simplify(Q_rotated)

# 打印结果
print(Q_rotated_simplified[0, 0])
