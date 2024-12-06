import numpy as np
import sympy as sp


def g_inv(g_ab):
    """
    Compute the inverse of the metric tensor g_ab
    """
    g_up = sp.Matrix(g_ab).inv()  # g^ab (sympy)
    return np.array(g_up)  # g^ab (numpy)


def christoffel_symbols(coords: list, g_ab: np.array):
    """
    Compute Christoffel symbols Γ^ρ_{μν} = g^ρσ Γ_{σμν}

    :param coords: coordinates x^μ, a list of sympy symbols
    :param g_ab: metric tensor g_ab
    :return:
    """
    d = len(coords)
    if not g_ab.shape == (d, d):
        raise ValueError("The shape of the metric tensor is not consistent with the dimension of the coordinates.")

    g_up = g_inv(g_ab)  # g^ab

    def diff_x(x):
        return [sp.diff(coef, x) for coef in g_ab.flatten()]

    # g_ab,c
    g_ab_c = np.array([diff_x(x) for x in coords]).reshape(d, d, d)
    g_ab_c = g_ab_c.transpose(1, 2, 0)

    # Γ^ρ_{μν} = g^ρσ Γ_{σμν}
    gamma_temp = (g_ab_c + g_ab_c.transpose(0, 2, 1) - g_ab_c.transpose(2, 1, 0)) / 2
    gamma = np.tensordot(g_up, gamma_temp, axes=(0, 0))
    return gamma


def curvature_tensor(coords: list, g_ab: np.array):
    """
    Compute Riemann curvature tensor R^ρ_{σμν}
    """
    gamma = christoffel_symbols(coords, g_ab)  # Γ^ρ_{μν}
    d = len(coords)
    assert gamma.shape == (d, d, d), f"Illegal shape of Christoffel symbols: {gamma.shape} during computing."

    def diff_x(x):
        return [sp.diff(_g, x) for _g in gamma.flatten()]

    # Γ^ρ_{μν},c
    gamma_c = np.array([diff_x(x) for x in coords]).reshape(d, d, d, d)
    gamma_c = gamma_c.transpose(1, 2, 3, 0)

    # R^ρ_{σμν} = (Γ^ρ_{σν},μ + Γ^ρ_{μλ}Γ^λ_{σν}) - (Γ^ρ_{σμ},ν  + Γ^ρ_{νλ}Γ^λ_{σμ})
    _gamma_gamma = np.tensordot(gamma, gamma, axes=(0, 1))  # Γ^ρ_{μλ}Γ^λ_{σν}
    riemann_temp = gamma_c.transpose(0, 1, 3, 2) + _gamma_gamma.transpose(2, 0, 3, 1)
    riemann = riemann_temp - riemann_temp.transpose(0, 1, 3, 2)  # utilize antisymmetry
    return riemann


# 3. 计算曲率张量和 Ricci 张量
def ricci_tensor(coords: list, g_ab: np.array):
    """
    Compute Ricci tensor R_{μν} = R^ρ_{μρν}

    :return:
    """
    d = len(coords)
    riemann = curvature_tensor(coords, g_ab)
    assert riemann.shape == (d, d, d, d), \
        f"Illegal shape of Riemann curvature tensor: {riemann.shape} during computing."

    # Ricci tensor R_{μν} = R^ρ_{μρν}
    ricci = np.einsum('abac->bc', riemann)

    # Ricci scalar R = g^μν R_{μν}
    g_up = g_inv(g_ab)
    r = np.tensordot(g_up, ricci, axes=([0, 1], [0, 1]))
    return ricci, r


def spherical_metric():
    """
    Compute the metric tensor of the 2-sphere in spherical coordinates
    """
    # Define the spherical coordinates
    r, theta, phi = sp.symbols('r theta phi')
    coords = [1, theta, phi]

    # Define the metric tensor
    g_ab = np.diag([sp.Integer(1), r ** 2, r ** 2 * sp.sin(theta) ** 2])
    return coords, g_ab


def schwarzschild_metric():
    """
    Compute the metric tensor of the Schwarzschild spacetime in spherical coordinates
    """
    # Define the Schwarzschild coordinates
    t, r, theta, phi = sp.symbols('t r theta phi')
    coords = [t, r, theta, phi]

    # Define the metric tensor
    g_ab = np.diag([-(1 - 2 / r), 1 / (1 - 2 / r), r ** 2, r ** 2 * sp.sin(theta) ** 2])
    return coords, g_ab


def schwarzschild_form_metric():
    """
    Compute the metric tensor of the Schwarzschild spacetime in spherical coordinates
    """
    # Define the Schwarzschild coordinates
    t, r, theta, phi = sp.symbols('t r theta phi')

    coords = [t, r, theta, phi]

    V = sp.Function('V')(r, t)
    lambda_ = sp.Function('lambda')(r, t)

    g_ab = np.diag([sp.exp(V), sp.exp(-lambda_), r ** 2, r ** 2 * sp.sin(theta) ** 2])
    return coords, g_ab


def test_christoffel_symbols():
    coords, g_ab = spherical_metric()
    print("Ricci scalar of 2D-Sphere:", ricci_tensor(coords[1:], g_ab[1:, 1:])[1])


def test_schwarzschild_metric():
    coords, g_ab = schwarzschild_metric()
    r = ricci_tensor(coords, g_ab)[1]
    print(type(r.sum()))
    print("Ricci scalar of Schwarzschild spacetime:", r.sum().simplify())


if __name__ == '__main__':
    test_christoffel_symbols()
    test_schwarzschild_metric()
