import numpy as np
from sympy.abc import rho, phi, z


def cartesian_to_polar(x, y):
    r = np.sqrt(x ** 2 + y ** 2)
    theta = np.arctan2(y, x)
    return r, theta


def test_cartesian_to_polar():
    x, y = 3, 4
    r, theta = cartesian_to_polar(x, y)
    assert np.isclose(r, 5.0), f"r={r}"
    assert np.isclose(theta, 0.93), f"theta={theta}"


def cartesian_to_cylindrical(x, y, z):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return rho, phi, z

# Example point in Cartesian coordinates
x, y, z = 3, 4, 5
rho, phi, z = cartesian_to_cylindrical(x, y, z)
print(f"Cartesian (x, y, z): ({x}, {y}, {z})")
print(f"Cylindrical (ρ, φ, z): ({rho:.2f}, {phi:.2f} radians, {z})")


def cartesian_to_spherical(x, y, z):
    r = np.sqrt(x**2 + y**2 + z**2)
    theta = np.arccos(z / r)
    phi = np.arctan2(y, x)
    return r, theta, phi

# Example point in Cartesian coordinates
x, y, z = 3, 4, 5
r, theta, phi = cartesian_to_spherical(x, y, z)
print(f"Cartesian (x, y, z): ({x}, {y}, {z})")
print(f"Spherical (r, θ, φ): ({r:.2f}, {theta:.2f} radians, {phi:.2f} radians)")


if __name__ == '__main__':
    test_cartesian_to_polar()
