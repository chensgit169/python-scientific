import sympy as sp

# Define the symbolic variables and parameters
t, w = sp.symbols('t w', real=True)
a, b, w0 = sp.symbols('a b w0', real=True, positive=True, constant=True)

f_w = sp.exp(-a * (w - w0) ** 2 + sp.I * b * (w - w0) ** 2)
f_t = sp.fourier_transform(f_w, w, t/2/sp.pi)
sp.pprint(f_t)
