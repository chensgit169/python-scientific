from mpmath import heunC

# 示例: 计算 HeunC(a, q, α, β, γ, δ, z)
a = 1.0
q = 0.5
alpha = 1.0
beta = 1.0
gamma = 0.5
delta = 1.0
z = 0.5

result = heunC(a, q, alpha, beta, gamma, delta, z)
print(result)
